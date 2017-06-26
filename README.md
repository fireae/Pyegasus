![logo](/resources/pyegasus@256x256.png)

# Pyegasus

_Pyegasus_ is an implementation of the Python programming language, **written
entirely in Python**. It uses the
[coreVM language runtime framework](https://github.com/yanzhengli/coreVM)
as its core runtime component, with implementation of the language's builtin
functions, types, and facilities that are tailored for _coreVM_. At runtime,
the [compiler/](compiler/) toolchain compiles both the
[language implementation source](src/) and target source into a format that is
executable by the _coreVM_ runtime. Read about the blog article
[here](https://medium.com/corevm-official-blog/python-corevm-pyegasus-73eab7c695f7).

The structure of this repository can be summarized as follows:

* [src/](src/) - source of _Pyegasus_'s Python language implementation.
  This encompasses all the builtin functions, types, definitions and facilities
  that form the language.
* [tests/](tests/) - a test suite for _Pyegasus_ that checks language
  conformance and implementation correctness.
* [compiler/](compiler/) - a compiler toolchain that's responsible for
  end-to-end compilation from Python source code to coreVM bytecode.
* [pyegasus.py](pyegasus.py) - command-line tool that executes individual Python
  source file using _Pyegasus_, by compiling raw Python source code followed up
  passing the output to the _coreVM_ client. To execute individual Python source
  file, such as [tests/int.py](tests/int.py) run `python pyegasus.py tests/int.py`.
* [bootstrap_tests.py](bootstrap_tests.py) - tool that bootstraps the entire
  test suite in the [tests/](tests/) directory. To run the entire Python test
  suite, run `python bootstrap_tests.py`.


## Demos

Pre-requisite: build `coreVM` project before running _Pyegasus_ with:
`cd coreVM && make`

**A simple hello world demo.**
![simple demo](/resources/aux/hello_world_demo.png)

**Compute Fibonacci sequence.**
![Fibonacci demo](/resources/aux/fibonacci_demo.png)

**Run test suite under [tests/](tests/).**
![Run test suite](/resources/aux/bootstrap_tests_demo.png)


## Progress

Currently only a tiny subset of the Python 2.7 language features are supported.
Supports for additional language features will be added down the road as the
development of _Pyegasus_ and _coreVM_ complements each other.

Below is a non-exhaustive list of all the language features supported at the
time of this writing:

- Language syntax and semantics
  - Unary and binary expressions
  - Conditional expressions
  - `for` and `while` loops
  - Subscripts and slicing
  - Comprehension syntax
  - Function definitions
  - Nested function definitions and closures.
  - Class definitions
  - `assert` statements
  - `print` statements
  - `with` statements
  - `try-except-finally` statements
- Advanced language features
  - Iterators
  - Generators
  - Arguments packing and unpacking
  - Exception handling
  - Decorators
  - `staticmethod` keyword
  - Context management semantics
- Builtin types
  - [`int`](https://docs.python.org/2/library/functions.html#int)
  - [`float`](https://docs.python.org/2/library/functions.html#float)
  - [`bool`](https://docs.python.org/2/library/functions.html#bool)
  - [`str`](https://docs.python.org/2/library/functions.html#str)
  - [`list`](https://docs.python.org/3.6/library/functions.html#func-list)
  - [`tuple`](https://docs.python.org/2/library/functions.html#tuple)
  - [`set`](https://docs.python.org/2/library/functions.html#func-set)
  - [`dict`](https://docs.python.org/2/library/functions.html#func-dict)
  - [`frozenset`](https://docs.python.org/2/library/functions.html#func-frozenset)
  - [`NoneType`](https://docs.python.org/2/library/types.html#types.NoneType)
  - [`complex`](https://docs.python.org/2/library/functions.html#complex)
- Builtin functions
  - [`abs`](https://docs.python.org/2/library/functions.html#abs)
  - [`all`](https://docs.python.org/2/library/functions.html#all)
  - [`bin`](https://docs.python.org/2/library/functions.html#bin)
  - [`chr`](https://docs.python.org/2/library/functions.html#chr)
  - [`cmp`](https://docs.python.org/2/library/functions.html#cmp)
  - [`divmod`](https://docs.python.org/2/library/functions.html#divmod)
  - [`delattr`](https://docs.python.org/2/library/functions.html#delattr)
  - [`exit`](https://docs.python.org/2/library/constants.html#exit)
  - [`filter`](https://docs.python.org/2/library/functions.html#filter)
  - [`getattr`](https://docs.python.org/2/library/functions.html#getattr)
  - [`hasattr`](https://docs.python.org/2/library/functions.html#hasattr)
  - [`hash`](https://docs.python.org/2/library/functions.html#hash)
  - [`hex`](https://docs.python.org/2/library/functions.html#hex)
  - [`id`](https://docs.python.org/2/library/functions.html#id)
  - [`iter`](https://docs.python.org/2/library/functions.html#iter)
  - [`len`](https://docs.python.org/2/library/functions.html#len)
  - [`map`](https://docs.python.org/2/library/functions.html#map)
  - [`max`](https://docs.python.org/2/library/functions.html#max)
  - [`min`](https://docs.python.org/2/library/functions.html#min)
  - [`next`](https://docs.python.org/2/library/functions.html#next)
  - [`oct`](https://docs.python.org/2/library/functions.html#oct)
  - [`pow`](https://docs.python.org/2/library/functions.html#pow)
  - [`range`](https://docs.python.org/2/library/functions.html#range)
  - [`reduce`](https://docs.python.org/2/library/functions.html#reduce)
  - [`reversed`](https://docs.python.org/2/library/functions.html#reversed)
  - [`round`](https://docs.python.org/2/library/functions.html#round)
  - [`setattr`](https://docs.python.org/2/library/functions.html#setattr)
  - [`sorted`](https://docs.python.org/2/library/functions.html#sorted)
  - [`sum`](https://docs.python.org/2/library/functions.html#sum)
  - [`zip`](https://docs.python.org/2/library/functions.html#zip)

P.S. Wish everyone happy hacking 😊
