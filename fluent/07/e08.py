"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Positional-Only Parameters
"""


def div_mod(a, b, /):
    """divmod built-in emulation - both arguments are positional only"""
    return a // b, a % b


print("both parameter by position:", div_mod(10, 3))
try:
    print(div_mod(10, b=3))
except TypeError as e:
    print(f"can't specify parameter by keyword! {e!r}")
