#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
License: Apache 2.0
Description: Installer for cPyparsing.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import setuptools

from Cython.Build import cythonize

#-----------------------------------------------------------------------------------------------------------------------
# CONSTANTS:
#-----------------------------------------------------------------------------------------------------------------------

pyparsing_version = "2.2.0"
development_version = "1"

version = pyparsing_version + "-post_dev" + development_version

#-----------------------------------------------------------------------------------------------------------------------
# SETUP:
#-----------------------------------------------------------------------------------------------------------------------

setuptools.setup(
    ext_modules=cythonize("cPyparsing.pyx"),
    packages=setuptools.find_packages(),
    version=version,
    name="cPyparsing",
    description="Cython implementation of PyParsing for use in Coconut.",
    url="https://github.com/evhub/cpyparsing",
    author="Evan Hubinger",
    author_email="evanjhub@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
    ],
)
