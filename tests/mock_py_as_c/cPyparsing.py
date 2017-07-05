"""
Mock of Python pyparsing as cPyparsing for the sake of timing comparison.
"""

print("cPyparsing -> pyparsing mock loaded")

from pyparsing import *
from pyparsing import __version__, _trim_arity

class SkipTo(SkipTo):
    def __init__(self, other, includeMatch=False, ignore=None, failOn=None):
        super(SkipTo, self).__init__(other, includeMatch, ignore, failOn)
