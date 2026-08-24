# al-math

`al_math` provides math runtime loading for `al-folio` v1.x.

## Installation

```ruby
gem 'al_math'
```

```yaml
plugins:
  - al_math
```

## Usage

Render assets:

```liquid
{% al_math_styles %}
{% al_math_scripts %}
```

TikZJax runtime is loaded from CDN config when a page sets `tikzjax: true`.

```yaml
third_party_libraries:
  tikzjax:
    url:
      css: https://cdn.jsdelivr.net/npm/@planktimerr/tikzjax@1.0.8/dist/fonts.css
      js: https://cdn.jsdelivr.net/npm/@planktimerr/tikzjax@1.0.8/dist/tikzjax.js
    integrity:
      css: <optional-sri-hash>
      js: <optional-sri-hash>
```

## Ecosystem context

- Starter wiring/docs live in `al-folio`.
- Math runtime ownership lives in this plugin.

## Contributing

Math runtime provider/config behavior changes should be proposed in this repository.
