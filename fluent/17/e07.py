"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

A self-documenting simple generator
"""


def a_generator():
    """A generator that yields two values"""
    # first call to next
    print("start")
    yield 1

    # second call to next
    print("continue")
    yield 2

    # third call to next
    print("end")


if __name__ == '__main__':
    for i in a_generator():
        print(i)
