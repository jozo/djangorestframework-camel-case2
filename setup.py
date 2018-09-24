#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
import djangorestframework_camel_case2

setup(
    name='djangorestframework-camel-case2',
    version=djangorestframework_camel_case2.__version__,
    description='Camel case JSON support for Django REST framework.',
    long_description=readme + '\n\n' + history,
    author='fadawar',
    author_email='fadawar@gmail.com',
    url='https://github.com/fadawar/djangorestframework-camel-case2',
    packages=[
        'djangorestframework_camel_case2',
    ],
    package_dir={'djangorestframework_camel_case2': 'djangorestframework_camel_case2'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='djangorestframework_camel_case2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
)
