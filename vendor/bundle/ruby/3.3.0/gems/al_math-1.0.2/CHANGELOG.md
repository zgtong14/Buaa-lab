# Changelog

## 1.0.2 - 2026-07-24

### Security / hygiene

- Stopped emitting the `polyfill.io` (`es6`) `<script>` from the MathJax path. The polyfill.io service was taken over in a June 2024 supply-chain attack and is unnecessary for MathJax 3 on modern browsers. The tag no longer reads `third_party_libraries.polyfill`, so the corresponding starter `_config.yml` entry can be dropped as follow-up cleanup.

## 1.0.1 - 2026-02-17

- Switched TikZJax CSS/JS loading from vendored plugin files to pinned CDN URLs in `third_party_libraries.tikzjax`.
- Removed bundled TikZJax assets from the gem package.

## 0.1.0 - 2026-02-07

- Initial gem release.
- Added standalone math script/style tags and assets (MathJax, pseudocode, TikZJax).
