# mkdocs-search-izsam

This is an MkDocs plugin that extends native search plugin in order to allow searches work locally. It will write two .js files (one storing a variable for `config` and one storing a variable for `docs`) that can be loaded in the theme using:

```html
<script src="{{ 'search/search_config.js'|url }}"></script>
<script src="{{ 'search/search_docs.js'|url }}"></script>
```

This will allow to avoid CORS problem caused by `loadJSON` functions and native `worker.js` model.

#### Important!

To use .js features and bypass the native `worker.js` model, the theme should be configured to use the `search_index_only` option as `true`:

```yaml
theme:
  name: null
  custom_dir: your_custom_theme
  include_search_page: true
  search_index_only: true
```

and then manage search with your favourite js library (in our project we still use `lunr.js` loaded in a script tag in the theme). For additional information please refer to [https://www.mkdocs.org/dev-guide/themes/#search-and-themes](https://www.mkdocs.org/dev-guide/themes/#search-and-themes).

## Setup

Install the plugin using pip:

`pip install mkdocs-izsam-search`

Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - izsam-search
```

It is possible to use same config options of the native search plugin:

```yaml
- izsam-search:
        lang: en
```

More information about plugins in the [MkDocs documentation][mkdocs-plugins].

## See Also

[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/
[mkdocs-template]: https://www.mkdocs.org/user-guide/custom-themes/#template-variables
[mkdocs-block]: https://www.mkdocs.org/user-guide/styling-your-docs/#overriding-template-blocks
