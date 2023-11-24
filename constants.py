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
from io import open
from datetime import datetime
from warnings import warn

# -----------------------------------------------------------------------------------------------------------------------
# UTILITIES:
# -----------------------------------------------------------------------------------------------------------------------


def get_bool_env_var(env_var, default=False):
    """Get a boolean from an environment variable."""
    boolstr = os.getenv(env_var, "").lower()
    if boolstr in ("true", "yes", "on", "1", "t"):
        return True
    elif boolstr in ("false", "no", "off", "0", "f"):
        return False
    else:
        if boolstr not in ("", "none", "default"):
            warn("{env_var} has invalid value {value!r} (defaulting to {default})".format(env_var=env_var, value=os.getenv(env_var), default=default))
        return default


#-----------------------------------------------------------------------------------------------------------------------
# BASE CONSTANTS:
#-----------------------------------------------------------------------------------------------------------------------

# when releasing a new version, create a release on github
#  and make upload-current on all platforms
pyparsing_version = "2.4.7"

# any incompatibility with prior Coconut versions must lead
#  to a minor or major version increment
development_version = "2.3.0"

wrap_call_line = "                ret = func(*args[limit[0]:])"

file_name = "cPyparsing.pyx"

requirements = [
    "cython>=0.29.21",
]

debug_mode = get_bool_env_var("CPYPARSING_DEBUG")

base_compiler_directives = {
    "language_level": 3,
    "overflowcheck": True,
    "cdivision": True,
    "cpow": True,
    "infer_types": True,
    "embedsignature": True,
    "c_api_binop_methods": True,
}

debug_compiler_directives = {
    "profile": True,
    "emit_code_comments": True,
}

#-----------------------------------------------------------------------------------------------------------------------
# DERIVED CONSTANTS:
#--------------------------------------------------------------------------

compiler_directives = base_compiler_directives.copy()
if debug_mode:
    warn("CPYPARSING_DEBUG mode enabled, using debug compilation parameters")
    compiler_directives.update(debug_compiler_directives)

version = pyparsing_version + "." + development_version

base_name = os.path.splitext(file_name)[0]
c_name = base_name + ".c"

version_time = datetime.utcnow().strftime("%d %b %Y %X")[:-3] + " UTC"

#-----------------------------------------------------------------------------------------------------------------------
# UPDATE FILE:
#-----------------------------------------------------------------------------------------------------------------------

def update_file():
    """Update constants in main Cython file."""

    print("Updating " + file_name + " constants...")
    with open(file_name, "r+", encoding="utf-8") as f:

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
                line = '__version__ = "' + version + '"\n'
                if seen_version:
                    f.truncate()
                    raise IOError("repeated __version__ in " + file_name)
                seen_version = True
            elif line.startswith("__versionTime__ ="):
                line = '__versionTime__ = "' + version_time + '"\n'
            elif line.startswith("_FILE_NAME ="):
                line = '_FILE_NAME = "' + file_name + '"\n'
            elif line.startswith("_WRAP_CALL_LINE_NUM ="):
                line = "_WRAP_CALL_LINE_NUM = " + repr(wrap_call_line_num) + "\n"
            new_lines.append(line)

    with open(file_name, "w", encoding="utf-8") as f:
        f.seek(0)
        f.truncate()
        f.write("".join(new_lines))

    print("Constants in " + file_name + " updated.")


if __name__ == "__main__":
    update_file()
