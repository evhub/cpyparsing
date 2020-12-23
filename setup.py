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
    base_name,
    c_name,
    requirements,
)

#-----------------------------------------------------------------------------------------------------------------------
# SETUP:
#-----------------------------------------------------------------------------------------------------------------------

try:
    from Cython.Build import cythonize
except ImportError:
    ext_modules = [setuptools.Extension(str(base_name), [str(c_name)])]
else:
    ext_modules = cythonize(
        str(file_name),
        force=True,
        compiler_directives={
            "language_level": 3,
            "overflowcheck": True,
            "cdivision": True,
            "infer_types": True,
        },
    )

setuptools.setup(
    name=base_name,
    version=version,
    ext_modules=ext_modules,
    packages=setuptools.find_packages(exclude=[
        "tests",
    ]),
    setup_requires=requirements,
    include_package_data=True,
    zip_safe=False,
    description="Cython implementation of PyParsing for use in Coconut.",
    url="https://github.com/evhub/cpyparsing",
    author="Evan Hubinger",
    author_email="evanjhub@gmail.com",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        "License :: OSI Approved :: Apache Software License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
