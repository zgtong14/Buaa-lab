"""Offline checks for publication data safety; no requests to Google Scholar."""

import importlib.util
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location(
    "scholar_sync", Path(__file__).resolve().parents[1] / "bin/sync_scholar_publications.py"
)
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

ORIGINAL = """---
---
@article{handwritten,
  title = {An AI-Assisted 48V-to-1V Converter},
  author = {Tong, Zhiguo},
  journal = {IEEE Journal of Solid-State Circuits},
  year = {2026},
  doi = {10.1234/example},
  pdf = {custom.pdf},
  selected = {true}
}
"""
NEW = {
    "ENTRYTYPE": "article", "ID": "remote",
    "title": "A New Converter", "author": "Tong, Zhiguo and Lu, Yan",
    "journal": "IEEE Journal of Solid-State Circuits", "year": "2027",
}
PUBLICATION = {"author_pub_id": "profile:paper", "pub_url": "https://example.org/paper"}


class ScholarSyncTests(unittest.TestCase):
    def existing(self):
        return sync.ExistingPapers(sync.parse_bibtex(ORIGINAL).entries)

    def test_dedup_normalizes_math_punctuation_and_session_number(self):
        self.assertTrue(self.existing().contains("21.8 An AI Assisted $48V$ to 1V Converter"))
        self.assertTrue(self.existing().contains("Different title", "https://doi.org/10.1234/EXAMPLE"))

    def test_append_preserves_curated_bytes_and_is_idempotent(self):
        existing = self.existing()
        entry = sync.prepare_entry(NEW, PUBLICATION, "profile", existing)
        updated = sync.append_entries(ORIGINAL, [entry])
        self.assertTrue(updated.startswith(ORIGINAL))
        entries = sync.parse_bibtex(updated).entries
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]["pdf"], "custom.pdf")
        self.assertEqual(entries[0]["selected"], "true")
        self.assertEqual(entries[1]["selected"], "false")
        self.assertEqual(entries[1]["abbr"], "JSSC")
        self.assertIsNone(sync.prepare_entry(NEW, PUBLICATION, "profile", existing))
        self.assertEqual(sync.append_entries(updated, []), updated)

    def test_missing_inline_voltage_does_not_duplicate_existing_paper(self):
        title = "A 2D-Extendable 48V-1V Ladder-Series-Capacitor Buck Converter for Computing Power Delivery"
        existing = sync.ExistingPapers([dict(NEW, title=title)])
        self.assertTrue(existing.contains(title.replace("48V", "")))
        self.assertFalse(existing.contains(title.replace("48V", "24V")))

    def test_rejects_incomplete_record_and_wrong_profile(self):
        for broken in (dict(NEW, year=""), dict(NEW, author=""), dict(NEW, journal="")):
            with self.assertRaises(ValueError):
                sync.prepare_entry(broken, PUBLICATION, "profile", self.existing())
        with self.assertRaises(ValueError):
            sync.prepare_entry(NEW, PUBLICATION, "another-profile", self.existing())

    def test_preserves_unstructured_citation_without_guessing_journal(self):
        record = dict(NEW, journal="", pub_year=2027, citation="Example Journal 7 (2), 123, 2027")
        entry = sync.prepare_entry(record, PUBLICATION, "profile", self.existing())
        self.assertEqual(entry["ENTRYTYPE"], "misc")
        self.assertEqual(entry["note"], record["citation"])
        self.assertNotIn("journal", entry)

    def test_fetch_failure_does_not_write_partial_results(self):
        first = {**PUBLICATION, "bib": NEW}
        second = {"author_pub_id": "profile:second", "bib": {"title": "Another new paper"}}
        def fill(item, **kwargs):
            if "sections" in kwargs:
                return {"scholar_id": "profile", "publications": [first, second]}
            if item is second:
                raise RuntimeError("blocked")
            return item

        client = SimpleNamespace(search_author_id=lambda _: {}, fill=fill)
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "papers.bib"
            file.write_bytes(ORIGINAL.encode())
            with patch.dict("sys.modules", {"scholarly": SimpleNamespace(scholarly=client)}):
                with self.assertRaises(RuntimeError):
                    sync.sync(file, "profile")
            self.assertEqual(file.read_bytes(), ORIGINAL.encode())


if __name__ == "__main__":
    unittest.main()
