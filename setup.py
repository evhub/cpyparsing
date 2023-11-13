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
import warnings

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from constants import (
    version,
    file_name,
    base_name,
    c_name,
    requirements,
    compiler_directives,
)

#-----------------------------------------------------------------------------------------------------------------------
# SETUP:
#-----------------------------------------------------------------------------------------------------------------------

try:
    from Cython.Build import cythonize
except ImportError:
    warnings.warn("cPyparsing couldn't find Cython; falling back to bundled cPyparsing.c")
    ext_modules = [setuptools.Extension(str(base_name), [str(c_name)])]
else:
    ext_modules = cythonize(
        str(file_name),
        force=True,
        compiler_directives=compiler_directives,
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
    long_description="""
See cPyparsing's GitHub_ for more information.

.. _GitHub: https://github.com/evhub/cpyparsing
""",
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
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
