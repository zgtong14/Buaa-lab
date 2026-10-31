#!/usr/bin/env python3
"""Append new Scholar publications without rewriting curated bibliography entries."""

import argparse
from difflib import SequenceMatcher
import hashlib
import html
import os
from pathlib import Path
import re
import sys
import unicodedata

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
import yaml


ROOT = Path(__file__).resolve().parents[1]
VENUES = (
    ("international solid-state circuits conference", "ISSCC"),
    ("journal of solid-state circuits", "JSSC"),
    ("symposium on vlsi", "VLSI Symp."),
    ("custom integrated circuits conference", "CICC"),
    ("applied power electronics conference", "APEC"),
    ("international symposium on circuits and systems", "ISCAS"),
    ("open journal of the solid-state circuits society", "OJSSCS"),
    ("transactions on circuits and systems i:", "TCAS-I"),
    ("transactions on power electronics", "TPEL"),
    ("asian solid-state circuits conference", "A-SSCC"),
    ("integrated circuits, technologies and applications", "ICTA"),
    ("solid-state & integrated circuit technology", "ICSICT"),
    ("solid-state and integrated circuit technology", "ICSICT"),
    ("journal of semiconductors", "J. Semicond."),
)


def normalize_title(value):
    value = html.unescape(value).casefold()
    value = re.sub(r"\\[a-z]+", "", value)
    value = re.sub(r"^\s*\d+(?:\.\d+)?\s+", "", value)
    value = unicodedata.normalize("NFKD", value)
    return "".join(c for c in value if c.isalnum())


def normalize_doi(value):
    return re.sub(r"^(?:https?://(?:dx\.)?doi.org/|doi:\s*)", "", value.strip().lower())


def parse_bibtex(text):
    # Keep nonstandard entry types and literal field values, including Jekyll flags.
    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    return bibtexparser.loads(text, parser=parser)


class ExistingPapers:
    def __init__(self, entries):
        self.titles = set()
        self.dois = set()
        self.ids = set()
        self.keys = {entry["ID"] for entry in entries}
        for entry in entries:
            self.add(entry)

    def contains(self, title, doi="", scholar_id=""):
        normalized = normalize_title(title)
        # Scholar may omit an inline math fragment (e.g. 48V) from a title.
        # Only accept a missing numeric fragment, not arbitrary fuzzy matches.
        damaged_math_match = False
        if len(normalized) >= 60:
            for known in self.titles:
                changes = [
                    (tag, known[j1:j2])
                    for tag, i1, i2, j1, j2 in SequenceMatcher(
                        None, normalized, known, autojunk=False
                    ).get_opcodes()
                    if tag != "equal"
                ]
                if len(changes) == 1 and changes[0][0] == "insert":
                    damaged_math_match = bool(re.fullmatch(r"\d+[a-z]*", changes[0][1]))
                    if damaged_math_match:
                        break
        return (
            normalized in self.titles
            or damaged_math_match
            or bool(doi and normalize_doi(doi) in self.dois)
            or bool(scholar_id and scholar_id in self.ids)
        )

    def add(self, entry):
        if entry.get("title"):
            self.titles.add(normalize_title(entry["title"]))
        if entry.get("doi"):
            self.dois.add(normalize_doi(entry["doi"]))
        if entry.get("google_scholar_id"):
            self.ids.add(entry["google_scholar_id"])


def prepare_entry(entry, publication, scholar_user_id, existing):
    entry = dict(entry)
    if entry.get("conference") and not entry.get("booktitle"):
        entry["booktitle"] = entry["conference"]
    year = str(entry.get("year") or entry.get("pub_year") or "")
    if not re.fullmatch(r"\d{4}", year):
        raise ValueError("Publication is missing a valid year")
    if not entry.get("title") or not entry.get("author"):
        raise ValueError("Publication is missing its title or authors")
    if not entry.get("journal") and not entry.get("booktitle") and not entry.get("citation"):
        raise ValueError(f"Publication is missing its source: {entry['title']}")
    author_pub_id = publication.get("author_pub_id", "")
    if not author_pub_id.startswith(scholar_user_id + ":"):
        raise ValueError("Publication does not belong to the configured Scholar profile")
    scholar_id = author_pub_id.split(":", 1)[1]
    if existing.contains(entry["title"], entry.get("doi", ""), scholar_id):
        return None
    allowed = {"title", "author", "year", "journal", "booktitle", "volume", "number", "pages", "publisher", "doi", "url"}
    result = {key: str(value) for key, value in entry.items() if key in allowed and value}
    result["year"] = year
    if entry.get("journal"):
        result["ENTRYTYPE"] = "article"
    elif entry.get("booktitle"):
        result["ENTRYTYPE"] = "inproceedings"
    else:
        # Scholar sometimes provides only a citation string instead of a journal
        # field. Preserve it verbatim rather than inventing publication metadata.
        result["ENTRYTYPE"] = "misc"
        result["note"] = str(entry["citation"])
    digest = hashlib.sha256(author_pub_id.encode()).hexdigest()[:16]
    key = "scholar_" + digest
    if key in existing.keys:
        raise ValueError("Generated bibliography key collides with an existing entry")
    result.update(ID=key, bibtex_show="true", selected="false", google_scholar_id=scholar_id)
    venue = result.get("journal", result.get("booktitle", result.get("note", ""))).lower().replace("–", "-")
    for name, abbreviation in VENUES:
        if name in venue:
            result["abbr"] = abbreviation
            break
    # Do not invent a DOI or copy an unverified PDF link from Scholar.
    if result.get("doi"):
        result["doi"] = normalize_doi(result["doi"])
        result["website"] = "https://doi.org/" + result["doi"]
    elif publication.get("pub_url", "").startswith("https://"):
        result["website"] = publication["pub_url"]
    existing.keys.add(key)
    existing.add(result)
    return result


def append_entries(original, entries):
    if not entries:
        return original
    database = bibtexparser.bibdatabase.BibDatabase()
    database.entries = entries
    writer = BibTexWriter()
    writer.indent = "  "
    writer.order_entries_by = None
    rendered = bibtexparser.dumps(database, writer=writer)
    # Validate before changing the file. Existing bytes, comments and front matter stay intact.
    if len(parse_bibtex(rendered).entries) != len(entries):
        raise ValueError("Generated bibliography failed round-trip validation")
    return original + "\n\n" + rendered


def sync(path, user_id, dry_run=False):
    from scholarly import scholarly

    original_bytes = path.read_bytes()
    original = original_bytes.decode("utf-8")
    existing = ExistingPapers(parse_bibtex(original).entries)
    author = scholarly.fill(scholarly.search_author_id(user_id), sections=["publications"])
    if author.get("scholar_id") != user_id or not author.get("publications"):
        raise ValueError("Scholar returned an empty or incorrect profile; no files changed")
    additions = []
    for publication in author["publications"]:
        title = publication.get("bib", {}).get("title", "")
        if existing.contains(title):
            continue
        filled = scholarly.fill(publication)
        # Author-profile records may lack pub_type/bib_id; scholarly.bibtex()
        # requires those fields. Use the filled record rather than guessing them.
        entry = prepare_entry(filled["bib"], filled, user_id, existing)
        if entry:
            additions.append(entry)
            print("New publication:", entry["title"])
    updated = append_entries(original, additions)
    if additions and not dry_run:
        if path.read_bytes() != original_bytes:
            raise RuntimeError("Bibliography changed during sync; rerun to avoid overwriting it")
        temporary = path.with_suffix(".bib.tmp")
        try:
            temporary.write_bytes(updated.encode("utf-8"))
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)
    print(f"{'Would add' if dry_run else 'Added'} {len(additions)} publication(s).")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as output:
            output.write(f"Scholar sync: {len(additions)} new publication(s).\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Fetch and report without writing files")
    args = parser.parse_args()
    with (ROOT / "_data/socials.yml").open(encoding="utf-8") as config:
        user_id = yaml.safe_load(config).get("scholar_userid")
    if not user_id:
        raise ValueError("Set scholar_userid in _data/socials.yml first")
    sync(ROOT / "_bibliography/papers.bib", user_id, args.dry_run)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Scholar sync failed; bibliography left unchanged: {error}", file=sys.stderr)
        sys.exit(1)
