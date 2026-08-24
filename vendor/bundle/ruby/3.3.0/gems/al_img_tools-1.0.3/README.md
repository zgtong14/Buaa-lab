# al-img-tools

`al_img_tools` provides image/gallery tooling for `al-folio` v1.x and compatible Jekyll sites.

## Features

- Image comparison sliders
- Lightbox-style galleries (vanilla adapter for `data-lightbox` markup)
- Medium zoom
- Image sliders
- PhotoSwipe galleries
- Spotlight galleries
- VenoBox galleries

## Installation

```ruby
gem 'al_img_tools'
```

```yaml
plugins:
  - al_img_tools
```

## Usage

Per-page front matter example:

```yaml
---
layout: page
title: Gallery
images:
  lightbox2: true
  compare: true
  slider: true
  photoswipe: true
  spotlight: true
  venobox: true
  medium_zoom: true
---
```

Render plugin assets:

```liquid
{% al_img_tools_styles %}
{% al_img_tools_scripts %}
```

## Ecosystem context

- Starter examples/docs live in `al-folio`.
- Gallery/lightbox runtime behavior is owned here.

## Contributing

Image runtime/adapter behavior changes should be proposed in this repository.
