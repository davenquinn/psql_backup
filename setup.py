#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "pathlib",
    "flask",
    "arrow",
    "click"
    ]

setup(
    name='psql-backup',
    version='0.1.0',
    description="psql-backup provides a simple command-line interface for backing up and restoring a PostgreSQL database.",
    long_description=readme + '\n\n' + history,
    author="Daven Quinn",
    author_email='dev@davenquinn.com',
    url='https://github.com/davenquinn/psql-backup',
    packages=[
        'psql_backup',
    ],
    package_dir={'psql_backup':
                 'psql_backup'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='psql-backup',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ])
