# cPyparsing

[Cython](http://cython.org/) implementation of [PyParsing](https://github.com/pyparsing/pyparsing) created for use in [Coconut](http://coconut-lang.org/) and [Undebt](https://github.com/Yelp/undebt).

Just [`pip install cpyparsing`](https://pypi.org/project/cPyparsing) then `import cPyparsing as pyparsing` or otherwise use `cPyparsing` however you would normally use `pyparsing`.

`cPyparsing` is currently only up-to-date with `pyparsing==2.4.7`—`cPyparsing` has no current plans to support any `pyparsing>=3` features. `cPyparsing` supports Python `2.6+` on Python 2 and Python `3.3+` on Python 3.

Additionally, `cPyparsing` supports an incremental mode that can be enabled with `ParserElement.enableIncremental()`. In incremental mode, if the same grammar is used to first parse some string, then later parse another string that shares a common prefix or suffix, incremental mode will produce substantial performance improvements. Note that incremental mode does not fully preserve parse exception error messages.
