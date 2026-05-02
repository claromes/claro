# Claro Pelican Theme

Claro is a custom Pelican theme built for [claromes.com](https://claromes.com). It started from Matt McManus' Brutalist theme and was adapted into a lighter, reading-focused layout with a minimal navigation structure.

## Overview

The theme combines a warm light color palette with two type systems:

- `iA Writer Quattro` for navigation, metadata, and interface elements
- `Roboto` for article content

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
- `TEMPLATE.md` serves as the writing template for new posts

## Development

### Requirement

Sass v1.99.0

### Style

- Edit `theme/claro/sass/main.sass` and the partials in `theme/claro/sass/` when changing the visual design

  ```bash
  sass --watch theme/claro/sass/main.sass:theme/claro/static/css/main.css --style compressed --no-source-map
  ```

- Treat `theme/claro/static/css/main.css` as the compiled output, not the source of truth
