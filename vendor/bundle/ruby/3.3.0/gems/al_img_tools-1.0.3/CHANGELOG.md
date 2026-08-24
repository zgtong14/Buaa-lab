# Changelog

## 1.0.3 - 2026-07-24

### Security

- Bumped Swiper from `11.0.5` to `12.1.2` to remediate a prototype-pollution vulnerability (CVE-2026-27212 / GHSA-hmx5-qpq5-p643, CVSS 9.4) affecting Swiper `>= 6.5.1, < 12.1.2`. Updated the pinned CDN version and the CSS / JS / source-map SRI integrity hashes to match the new release. The image slider consumes the `swiper-element` Web Component bundle, whose `<swiper-container>` custom-element API is unchanged across this major bump, so no template or setup-script changes are required.

## 1.0.2 - 2026-02-17

- Finalized plugin-owned lightbox runtime by shipping a vanilla Lightbox2-compatible adapter path.
- Ensured static asset generator picks up all plugin runtime assets under `lib/assets/al_img_tools/**`.
- Added test coverage for adapter CSS/JS packaging contracts.
- Reduced noisy static-file logging by treating unchanged asset copies as debug-level skips.

## 1.0.1 - 2026-02-17

- Replaced Lightbox2 CDN runtime dependency with a plugin-owned vanilla lightbox adapter.
- Added plugin-owned lightbox adapter CSS/JS assets and static asset registration.
- Removed jQuery dependency from medium zoom initialization.

## 0.1.0 - 2026-02-07

- Initial gem release.
- Added standalone image tooling tags and assets (zoom, gallery, sliders, lightboxes).
