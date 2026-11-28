"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Using a generator expression
"""
from typing import Generator

from e07 import a_generator

if __name__ == '__main__':
    # a list comprehension using (eagerly) a chatty generator
    res1 = [x * 3 for x in a_generator()]
    for i in res1:
        print('-->', i)

    # creating a generator from another generator (not consumed)
    res2 = (x * 3 for x in a_generator())

    print("res2 is a Generator:", isinstance(res2, Generator))
    # when consuming the external generator, the internal one is consumed too
    for i in res2:
        print('-->', i)
