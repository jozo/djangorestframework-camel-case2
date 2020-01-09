#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy

from djangorestframework_camel_case2.util import camelize, underscoreize
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.wsgi import get_wsgi_application


class TestUnderscoreToCamel:
    def test_under_to_camel_keys(self):
        data = {
            "two_word": 1,
            "long_key_with_many_underscores": 2,
            "only_1_key": 3,
            "only_one_letter_a": 4,
            "b_only_one_letter": 5,
            "only_c_letter": 6,
            "mix_123123a_and_letters": 7,
            "no_underscore_before123": 8
        }
        output = {
            "twoWord": 1,
            "longKeyWithManyUnderscores": 2,
            "only1Key": 3,
            "onlyOneLetterA": 4,
            "bOnlyOneLetter": 5,
            "onlyCLetter": 6,
            "mix123123aAndLetters": 7,
            "noUnderscoreBefore123": 8
        }
        assert camelize(data) == output

    def test_tuples(self):
        data = {
            "multiple_values": (1, 2),
            "data": [1, 3, 4]
        }
        output = {
            "multipleValues": [1, 2],
            "data": [1, 3, 4]
        }
        assert camelize(data) == output

    def test_camel_to_under_input_untouched_for_sequence(self):
        data = [
            {'firstInput': 1},
            {'secondInput': 2},
        ]
        reference_input = deepcopy(data)
        camelize(data)
        assert data == reference_input

    def test_translation(self):
        settings.configure(USE_I18N=True)
        app = get_wsgi_application()
        data = {
            "two_word": _('Example'),
        }
        output = {
            "twoWord": "Example",
        }
        assert camelize(data) == output


class TestCamelToUnderscore:
    def test_camel_to_under_keys(self):
        data = {
            "twoWord": 1,
            "longKeyWithManyUnderscores": 2,
            "only1Key": 3,
            "onlyOneLetterA": 4,
            "bOnlyOneLetter": 5,
            "onlyCLetter": 6,
            "mix123123aAndLetters": 7,
        }
        output = {
            "two_word": 1,
            "long_key_with_many_underscores": 2,
            "only_1_key": 3,
            "only_one_letter_a": 4,
            "b_only_one_letter": 5,
            "only_c_letter": 6,
            "mix_123123a_and_letters": 7
        }
        assert underscoreize(data) == output

    def test_camel_to_under_keys_with_no_underscore_before_number(self):
        data = {'noUnderscoreBefore123': 1}
        output = {'no_underscore_before123': 1}
        options = {'no_underscore_before_number': True}
        assert underscoreize(data, **options) == output

    def test_under_to_camel_input_untouched_for_sequence(self):
        data = [
            {'first_input': 1},
            {'second_input': 2},
        ]
        reference_input = deepcopy(data)
        underscoreize(data)
        assert data == reference_input


class TestNonStringKey:
    def test_non_string_key(self):
        data = {1: "test"}
        assert underscoreize(camelize(data)) == data


class TestGeneratorAsInput:
    def _underscore_generator(self):
        yield {'simple_is_better': 'than complex'}
        yield {'that_is': 'correct'}

    def _camel_generator(self):
        yield {'simpleIsBetter': 'than complex'}
        yield {'thatIs': 'correct'}

    def test_camelize_iterates_over_generator(self):
        data = self._underscore_generator()
        output = [
            {'simpleIsBetter': 'than complex'},
            {'thatIs': 'correct'},
        ]
        assert camelize(data) == output

    def test_underscoreize_iterates_over_generator(self):
        data = self._camel_generator()
        output = [
            {'simple_is_better': 'than complex'},
            {'that_is': 'correct'},
        ]
        assert underscoreize(data) == output
