# Change log

## [1.0.8] - 2024-09-18

### Scale factor option
Added a scale factor option in order to generate better quality png images. Please consider that only when the output format is set to be a png the scale factor will be applied.

## [1.0.7] - 2024-09-17

### Added support to Mermaid configuration options
Needed to import json module

## [1.0.6] - 2024-09-17

### Added support to Mermaid configuration options

## [1.0.5] - 2024-09-17

### Added class for generate img tag
Added a class to the generated <img> tag and made it configurable by the user, default is 'mmd'.

## [1.0.4] - 2024-09-17

### Changed the way images directory are generated
Images directory now is generated in the same directory as the HTML file where the Mermaid diagrams are declared. This way, the image paths will be relative to the page, avoiding problems with paths.

## [1.0.3] - 2024-09-17

### Fix on image paths
The plugin was generating the image paths relative to the current page, but it should generate them relative to the root of the site.

## [1.0.2] - 2024-09-17

### Fix on image paths
Generated image files are not being found at the expected paths.

## [1.0.1] - 2024-09-17

### Setup bug fix and README changes
Bug fix for setup entry_points section; fix for error in configuration instructions.

## [1.0] - 2024-09-17

### First release
