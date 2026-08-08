"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Unpacking Mappings
"""


def as_dict(**kwargs):
    """
    notice that each keyword passed in should be a string, and no duplicated is allowed

    the keyword arguments are packed into a dictionary - traditionally named kwargs

    return a dict with the collected key/value pairs
    """
    return kwargs


print(as_dict(a=1, b=2, c=3))

# unpacking in a dict literal - duplicated keys are discarded
a_dict = {"a": 0, **{"x": 1}, "y": 2, **{"z": 3, "x": 4}}
print(a_dict)

# unpacking in a function call
print(as_dict(**{'x': 1}, y=2, **{'z': 3}))
