# Changelog

## [Unreleased]

## [0.3.0]
- Drop support for Python 2, Django 1.11 and Django Rest Framework 3.8
- Fix rendering of lazy strings from Django

## [0.2.5]
- Changed project internals - we are using poetry now
- Add support for Django 3.0

## [0.2.4]
- Added `json_underscoreize` to `CamelCaseJSONParser` as class attribute to support variables with and without an underscore before a number in the same project
- Fixed import of six in combination with DRF 3.10

## [0.2.3]
## Fixed
- Fixed missing CHANGELOG.md in package on pypi

## [0.2.2]
### Changed
- Update README

### Removed
- Old README.rst and HISTORY.rst

## [0.2.1]
### Added
- Support for generators and other iterables
- JSON_UNDERSCOREIZE option to change behaviour of underscoize function

### Changed
- Changed name of the package and README

## [0.1.0] - 2013-12-20
- First release on PyPI.
