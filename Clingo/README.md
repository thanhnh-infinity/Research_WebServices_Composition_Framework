# Clingo: A grounder and solver for logic programs

Clingo is part of the [Potassco](https://potassco.org) project for *Answer Set
Programming* (ASP).  ASP offers a simple and powerful modeling language to
describe combinatorial problems as *logic programs*.  The *clingo* system then
takes such a logic program and computes *answer sets* representing solutions to
the given problem.  To get an idea, check our [Getting
Started](https://potassco.org/doc/start/) page and the [online
version](https://potassco.org/clingo/run/) of clingo.

Please consult the following resources for further information:

  - [**Downloading source and binary releases**](https://github.com/potassco/clingo/releases)
  - [Changes between releases](CHANGES.md)
  - [Documentation](http://sourceforge.net/projects/potassco/files/guide/)
  - [Potassco clingo page](https://potassco.org/clingo/)


## Contents of MacOS Binary Release

The `clingo` and `gringo` binaries are compiled with Lua 5.3 but without Python
2.7 support.  The `clingo-python` and `gringo-python` executables are
additionally build with Python 2.7 support.

- `clingo`: solver for non-ground programs
- `clingo-python`: solver for non-ground programs with Python support
- `gringo`: grounder
- `gringo-python`: grounder with Python support
- `clasp`: solver for ground programs
- `reify`: reifier for ground programs
- `lpconvert`: translator for ground formats
- `c-api/`: headers and library of clingo C and C++ API
- `python-api/`: clingo Python 2.7 module
  - to use the module either copy it into the Python path or point the
    [PYTHONPATH](https://docs.python.org/2/using/cmdline.html#envvar-PYTHONPATH)
    to the `python-api` directory
