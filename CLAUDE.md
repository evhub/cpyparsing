# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

cPyparsing is a Cython implementation of PyParsing 2.4.7, created for use in [Coconut](http://coconut-lang.org/). It supports Python 2.6+ and 3.3+. There are no plans to support pyparsing 3.x features.

## Build & Test Commands

```bash
# Install and run tests
make full-test

# Install (cleans, updates constants, builds Cython extension, installs)
make install-debug

# Run tests (sets COCONUT_PURE_PYTHON=TRUE, runs tests/cPyparsing_test.py)
make test

# Run a single test directly
COCONUT_PURE_PYTHON=TRUE python ./tests/cPyparsing_test.py

# Clean all build artifacts (.pyc, .c, .so, .pyd, build/, dist/)
make clean
```

## Architecture

### Single-file Cython module

The entire library is a single Cython file: **`cPyparsing.pyx`** (~8200 lines). This is a modified fork of pyparsing 2.4.7 with cPyparsing-specific modifications marked by `[CPYPARSING]` comments throughout.

### Key files

- **`cPyparsing.pyx`** — The sole source file. Contains all parser elements, parse results, exceptions, and helpers.
- **`cPyparsing.c`** — Generated C code (committed for fallback when Cython is unavailable).
- **`constants.py`** — Version management and Cython compiler directives. Also a script: running `python constants.py` updates version/line-number constants in `cPyparsing.pyx` before compilation.
- **`setup.py`** — Build configuration. Falls back to bundled `.c` file if Cython is not installed.
- **`tests/cPyparsing_test.py`** — Main test suite.
- **`tests/mock_c_as_py/`** and **`tests/mock_py_as_c/`** — Mock packages for cross-testing cPyparsing vs pyparsing compatibility.

### Versioning

Version = `pyparsing_version.development_version`. Both are defined in `constants.py`. Incompatibilities with prior Coconut versions require a major or minor bump to `development_version`.

### cPyparsing-specific features (not in upstream pyparsing)

- **Incremental parsing** (`ParserElement.enableIncremental()`) — Reuses caches across parses of strings with common prefixes/suffixes. Does not fully preserve parse exception error messages.
- **Hybrid incremental mode** — Variant of incremental parsing enabled via `hybrid_mode=True`.
- Additional diagnostic flags: `warn_on_incremental_multiline_regex`, `warn_on_undefined_ParseResults_name`.

### Class hierarchy (key base classes)

- `ParserElement` — Abstract base for all parsers
- `Token` → `Literal`, `Keyword`, `Regex`, `Word`, `QuotedString`, etc.
- `ParseExpression` → `And`, `Or`, `MatchFirst`, `Each`
- `ParseElementEnhance` → `Optional`, `ZeroOrMore`, `OneOrMore`, `Suppress`, `Forward`, etc.
- `ParseResults` — Structured parse output
- `ParseBaseException` → `ParseException`, `ParseFatalException`, `ParseSyntaxException`
