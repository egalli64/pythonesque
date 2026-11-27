"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

A simple generator
"""
from types import FunctionType, GeneratorType
from typing import Iterable


def a_generator():
    """A generator that yields three values"""
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    print("a_generator is a function:", isinstance(a_generator, FunctionType))
    g = a_generator()
    print("The object returned by a_generator is a Generator:", isinstance(g, GeneratorType))
    print("A Generator is an Iterable:", isinstance(g, Iterable))

    # use the generator as in iterator, let the for loop consume it
    for i in g:
        print(i)
    print("--")

    # create a new generator and consume it by next(), to see it raising a StopIteration
    g = a_generator()
    for i in range(4):
        print(next(g))
