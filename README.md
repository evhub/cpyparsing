# cPyparsing

Cython implementation of PyParsing for use in Coconut.

Just `pip install cpyparsing` then `import cPyparsing as pyparsing` or otherwise use `cPyparsing` however you would normally use `pyparsing`.

The only difference between the `cPyparsing` and `pyparsing` API is that the `include` keyword of `SkipTo` is now `includeMatch` instead (since `include` is a Cython keyword).
