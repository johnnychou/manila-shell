#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import manilaShell

setup(
    name='manila-shell',
    version=manilaShell.__version__,
    description='Infortrend Cloud Storage Shell for Manila Driver',

    author='Infortrend',
    url='http://www.infortrend.com',
    author_email='tsd@infortrend.com',

    platforms='any',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'manila-shell = manilaShell.__main__:run'
        ]
    },

    setup_requires=[
        'flake8>=2.4.1',
        'regex>=2015.10.29'
    ],
)
