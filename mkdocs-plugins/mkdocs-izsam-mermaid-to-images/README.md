# MkDocs IZSAM Mermaid to images

This plugin processes each page's Markdown content, finds Mermaid code blocks, converts them to images using `mermaid.cli`, and replaces the code blocks with image references. The image format can be specified in the `mkdocs.yml` configuration file.

## Installation

Install dependencies:

```bash
npm install -g @mermaid-js/mermaid-cli
```

Install the package with pip:

```bash
pip install mkdocs-izsam-mermaid-to-images
```

Enable the plugin in the `mkdocs.yml` file:

```yaml
plugins:
  - search
  - mkdocs-izsam-mermaid-to-images:
        output_dir: mermaid_images # Optional, defaults to 'mermaid_images'
        image_format: svg # Optional, defaults to 'svg'
        image_class: mmd  # Optional, defaults to 'mmd'
        scale: 3 # Optional, defaults to '1'
        mermaid_config:
            theme: default
            fontFamily: "Arial, sans-serif"
            fontSize: 16
```

> See how to use [MkDocs Plugins](https://www.mkdocs.org/dev-guide/plugins/#using-plugins)