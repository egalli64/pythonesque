"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Simple Class Patterns
"""
def do_something_with(x):
    print("x is", x)


def match_example(x):
    match x:
        case float():
            do_something_with(x)
        case _:
            print(f"{x}, {type(x)}, is not matched")


match_example(1)
match_example("1")
match_example(1.0)
