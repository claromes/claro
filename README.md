# Claro Pelican Theme

Claro is a custom Pelican theme built for [claromes.com](https://claromes.com). It started from Matt McManus' Brutalist theme and was adapted into a lighter, reading-focused layout with a minimal navigation structure.

## Overview

The theme combines a warm light color palette with two type systems:

- [`iA Writer Quattro`](https://github.com/iaolo/iA-Fonts) for navigation, metadata, and interface elements
- [`Roboto`](https://github.com/googlefonts/roboto-3-classic) for article content

Its templates are designed for a personal blog with:

- a simple top navigation
- article lists with support for pinned posts
- dedicated article, page, tag, and pagination templates
- metadata for feeds, Open Graph, favicon, and fediverse identity
- sharing links for published posts

## Structure

- `theme/claro/templates/` contains the Jinja templates used by Pelican
- `theme/claro/static/css/main.css` contains the compiled theme styles
- `theme/claro/sass/` contains the source Sass files
- `.pelican_templates/POST.md` serves as the writing template for new posts
- `.pelican_templates/pelicanconf.py` contains the base Pelican settings used by the project
- `.pelican_templates/publishconf.py` contains the publish-time overrides, such as the production `SITEURL` and `RELATIVE_URLS = False`

## Post template note

`.pelican_templates/POST.md` includes the `custom_css` field because the article template injects it directly into the cover image element. This makes it possible to apply one-off inline styling, such as borders, width adjustments, or alignment tweaks for a specific post image, without changing the global theme stylesheet.

## Assets

According to `.pelican_templates/pelicanconf.py`, Pelican uses `PATH = "content"` and `STATIC_PATHS = ["images", "extras/_redirects"]`.

- Store `SITEIMAGE` and `FAVICON` files in `content/images/`
- Set `SITEIMAGE` and `FAVICON` in `.pelican_templates/pelicanconf.py` using the filename only
- In the generated site, those files are exposed under `/images/`

For example, if `FAVICON = "favicon.png"` and `SITEIMAGE = "cover.png"`, the theme will resolve them from `/images/favicon.png` and `/images/cover.png`

## Pelican Configuration

The base configuration in `.pelican_templates/pelicanconf.py` enables these plugins:

- `gzip_cache`
- `share_post`
- `sitemap`

The sitemap plugin is also configured there with article, page, and index priorities and daily change frequencies.

## Development

### Requirement

Sass v1.99.0

### Style

- Edit `theme/claro/sass/main.sass` and the partials in `theme/claro/sass/` when changing the visual design

  ```bash
  sass --watch theme/claro/sass/main.sass:theme/claro/static/css/main.css --style compressed --no-source-map
  ```

- Treat `theme/claro/static/css/main.css` as the compiled output, not the source of truth
