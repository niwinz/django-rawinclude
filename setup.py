#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'django-rawinclude',
    version = ":versiontools:rawinclude:",
    description = "Small module for django that gives the ease of loading templates in raw.",
    long_description = "",
    keywords = 'django, template, javascript',
    author = 'Andrei Antoukh',
    author_email = 'niwi@niwi.be',
    url = 'https://github.com/niwibe/django-rawinclude',
    license = 'BSD',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[
        'distribute',
    ],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    classifiers = [
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
