#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import djangorestframework_camel_case2

with open('README.md', 'r') as fh:
    readme = fh.read()

with open('CHANGELOG.md', 'r') as fh:
    changelog = fh.read()

setup(
    name='djangorestframework-camel-case2',
    version=djangorestframework_camel_case2.__version__,
    url='https://github.com/fadawar/djangorestframework-camel-case2',
    description='Camel case JSON support for Django REST framework',
    license='BSD',
    long_description=readme + '\n\n' + changelog,
    long_description_content_type='text/markdown',
    author='fadawar',
    author_email='fadawar@gmail.com',
    packages=find_packages(exclude=['tests*']),
    keywords='djangorestframework_camel_case2',
    classifiers=[
        'Development Status :: 4 - Beta',
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
