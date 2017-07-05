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

import sys
import os.path
import setuptools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from constants import (
    version,
    file_name,
)

from Cython.Build import cythonize

#-----------------------------------------------------------------------------------------------------------------------
# SETUP:
#-----------------------------------------------------------------------------------------------------------------------

setuptools.setup(
    ext_modules=cythonize(
        file_name,
        compiler_directives={
            "language_level": 3,
        },
    ),
    packages=setuptools.find_packages(),
    include_package_data=True,
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
