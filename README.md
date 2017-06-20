![logo](/resources/pyegasus@256x256.png)

# Pyegasus

Python programming language implementation based on the [coreVM language runtime framework](https://github.com/yanzhengli/coreVM).

_Pyegasus_ is an implementation of the Python programming language. It makes use
of [coreVM](https://github.com/yanzhengli/coreVM) as its core runtime component,
plus implementation of the language's builtin functions, types, and facilities
that are tailored for _coreVM_. Finally, a compiler tool chain is available to
compile raw Python source code into a format that is executable by coreVM.

This directory contains all the source code, tests, and tools for _Pyegasus_.
The structure of the directory can be summarized as follows:

* [src/](src/) - source of the Python language implementation. This encompasses
  all the builtin functions, types, definitions and facilities that form the
  language.
* [tests/](tests/) - a test suite for _Pyegasus_ that checks language
  conformance and implementation correctness.
* [compiler/](compiler/) - a compiler tool chain that's responsible for
  end-to-end compilation from Python source code to coreVM bytecode.
* [pyegasus.py](pyegasus.py) - command-line tool that executes individual Python
  source file using _Pyegasus_. To execute individual Python source file, such as
  [tests/int.py](tests/int.py) run `python pyegasus.py tests/int.py`.
* [bootstrap_tests.py](bootstrap_tests.py) - tool that bootstraps the entire
  test suite in the [tests/](tests/) directory. To run the entire Python test
  suite, run `python bootstrap_tests.py`.


## Demos and Playground

Pre-requisite: build `coreVM` project before running _Pyegasus_ with:
`cd coreVM && make`

**A simple hello world demo.**
![simple demo](/resources/aux/hello_world_demo.png)

**Compute Fibonacci sequence.**
![Fibonacci demo](/resources/aux/fibonacci_demo.png)

**Run test suite under tests/.**
![Run test suite](/resources/aux/bootstrap_tests_demo.png)


## Progress

Currently only a tiny subset of the Python language features is supported. As
the development of _Pyegasus_ and coreVM complements each other, the language
implementation matures as coreVM grows with more versatility and capabilities.

Below is a non-exhaustive list of all the language features supported at the
time of this writing:

- Language syntax and semantics
  - Unary and binary expressions
  - Conditional expressions
  - Loops
  - Subscripts and slicing
  - Comprehension syntax
  - Function definitions
  - Class definitions
  - Assert statements
  - Print statements
  - With statements
  - Try-except-finally statements
- Advanced language features
  - Iterators
  - Generators
  - Arguments packing and unpacking
  - Exception handling
  - Decorators
  - `staticmethod` keyword
  - Context management semantics
- Builtin types
  - `int`
  - `float`
  - `bool`
  - `str`
  - `list`
  - `tuple`
  - `set`
  - `dict`
  - `frozenset`
  - `NoneType`
  - `complex`
- Builtin functions
  - `abs`
  - `all`
  - `bin`
  - `chr`
  - `cmp`
  - `divmod`
  - `delattr`
  - `exit`
  - `filter`
  - `getattr`
  - `hasattr`
  - `hash`
  - `hex`
  - `id`
  - `iter`
  - `len`
  - `map`
  - `max`
  - `min`
  - `next`
  - `oct`
  - `pow`
  - `range`
  - `reduce`
  - `reversed`
  - `round`
  - `setattr`
  - `sorted`
  - `sum`
  - `zip`

P.S. Wish everyone happy hacking.

