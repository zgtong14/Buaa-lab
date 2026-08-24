# al-cookie

`al_cookie` is the cookie-consent plugin for `al-folio` v1.x.

## What it owns

- Cookie consent runtime setup and UI wiring
- Consent-related includes/assets previously owned by monolithic theme code
- Consent theme synchronization hooks used by `al-folio`

## Installation

```ruby
gem 'al_cookie'
```

Enable in `_config.yml`:

```yaml
plugins:
  - al_cookie
```

## Usage

Render assets/scripts where your layout expects consent support:

```liquid
{% al_cookie_styles %}
{% al_cookie_scripts %}
```

Use your existing consent config keys in `_config.yml`.

## Ecosystem context

- Starter/orchestration: `al-folio`
- Theme runtime contracts: `al_folio_core`
- Consent gating integrations (for example analytics) are consumed via plugin boundaries.

## Contributing

Changes to consent behavior should be proposed in this repository (not `al-folio` starter), unless the change is strictly starter documentation/demo content.
