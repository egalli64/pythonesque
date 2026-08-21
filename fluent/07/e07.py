"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Keyword only parameters
"""


def f(a, *, b):
    """b is a keyword only argument"""
    return a, b


print("both parameter by keyword:", f(a=1, b=2))
print("only second parameter by keyword:", f(1, b=2))
try:
    print(f(1, 2))
except TypeError as e:
    print(f"After * just kwargs! {e!r}")


def g(a=24, *, b=42):
    """b is a keyword only argument"""
    return a, b


print("no changes for default values:", g())
