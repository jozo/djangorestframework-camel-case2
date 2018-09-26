# Django REST Framework JSON CamelCase

[![Build Status](https://travis-ci.org/fadawar/djangorestframework-camel-case2.svg?branch=master)](https://travis-ci.org/fadawar/djangorestframework-camel-case2)
[![PyPI](https://img.shields.io/pypi/v/djangorestframework-camel-case2.svg)](https://pypi.org/project/djangorestframework-camel-case2/)

Camel case JSON support for Django REST framework.

_Note: This is a replacement for
[djangorestframework-camel-case](https://github.com/vbabiy/djangorestframework-camel-case)
which seems currently unmaintained._

## Installation

At the command line::
```bash
$ pip install djangorestframework-camel-case2
```

Add the render and parser to your django settings file.

```python
REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case2.render.CamelCaseJSONRenderer',
        # Any other renders
    ),

    'DEFAULT_PARSER_CLASSES': (
        'djangorestframework_camel_case2.parser.CamelCaseJSONParser',
        # Any other parsers
    ),
}
```

## Swapping Renderer

By default the package uses `rest_framework.renderers.JSONRenderer`. If you want
to use another renderer (the only possible alternative is
`rest_framework.renderers.UnicodeJSONRenderer`, only available in DRF < 3.0), you must specify it in your django
settings file.

```python
# ...
JSON_CAMEL_CASE = {
    'RENDERER_CLASS': 'rest_framework.renderers.UnicodeJSONRenderer'
}
# ...
```

## Underscoreize Options

As raised in https://github.com/krasa/StringManipulation/issues/8#issuecomment-121203018
there are two conventions of snake case.

```
# Case 1 (Package default)
v2Counter -> v_2_counter
fooBar2 -> foo_bar_2

# Case 2
v2Counter -> v2_counter
fooBar2 -> foo_bar2
```

By default, the package uses the first case. To use the second case, specify it in your django settings file.

```python
REST_FRAMEWORK = {
    # ...
    'JSON_UNDERSCOREIZE': {
        'no_underscore_before_number': True,
    },
    # ...
}
```

## Running Tests

To run the current test suite, execute the following from the root of the project

```bash
$ python -m unittest discover
```
