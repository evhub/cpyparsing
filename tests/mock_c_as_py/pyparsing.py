"""
Mock of cPyparsing as Python pyparsing for the sake of timing comparison.
"""

print("pyparsing -> cPyparsing mock loaded")

from cPyparsing import *
from cPyparsing import __version__, _trim_arity

class SkipTo(SkipTo):
    def __init__(self, other, include=False, ignore=None, failOn=None):
        super(SkipTo, self).__init__(other, include, ignore, failOn)
