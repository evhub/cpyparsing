# cPyparsing

Cython implementation of PyParsing for use in Coconut.

Just `pip install cpyparsing` then `import cPyparsing as pyparsing` or however else you would normally use `pyparsing`.

The only difference between the `cPyparsing` and `pyparsing` API is that the `include` keyword of `SkipTo` is now `includeMatch` instead.
