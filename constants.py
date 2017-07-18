#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------------------------------------------------
# INFO:
#-----------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
License: Apache 2.0
Description: Constants for cPyparsing.
"""

#-----------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-----------------------------------------------------------------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import os.path

#-----------------------------------------------------------------------------------------------------------------------
# BASE CONSTANTS:
#-----------------------------------------------------------------------------------------------------------------------

pyparsing_version = "2.2.0"
development_version = "1.1.1"

wrap_call_line = "                ret = func(*args[limit:])"

file_name = "cPyparsing.pyx"

#-----------------------------------------------------------------------------------------------------------------------
# DERIVED CONSTANTS:
#--------------------------------------------------------------------------

version = pyparsing_version + "." + development_version

base_name = os.path.splitext(file_name)[0]
c_name = base_name + ".c"

#-----------------------------------------------------------------------------------------------------------------------
# UPDATE FILE:
#-----------------------------------------------------------------------------------------------------------------------


def update_file():
    """Update constants in main Cython file."""

    print("Updating " + file_name + " constants...")
    with open(file_name, "r+") as f:

        wrap_call_line_num = None
        for i, line in enumerate(f):
            if line.startswith(wrap_call_line):
                wrap_call_line_num = i + 1
        if wrap_call_line_num is None:
            raise IOError("failed to find " + repr(wrap_call_line) + " in " + file_name)

        f.seek(0)

        new_lines = []
        seen_version = False
        for line in f:
            if line.startswith("__version__ ="):
                line = '__version__ = "' + pyparsing_version + '"\n'
                if seen_version:
                    f.truncate()
                    raise IOError("repeated __version__ in " + file_name)
                seen_version = True
            elif line.startswith("_FILE_NAME ="):
                line = '_FILE_NAME = "' + file_name + '"\n'
            elif line.startswith("_WRAP_CALL_LINE_NUM ="):
                line = "_WRAP_CALL_LINE_NUM = " + repr(wrap_call_line_num) + "\n"
            new_lines.append(line)

    with open(file_name, "w") as f:
        f.seek(0)
        f.truncate()
        f.write("".join(new_lines))

    print("Constants in " + file_name + " updated.")


if __name__ == "__main__":
    update_file()
