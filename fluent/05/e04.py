"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

The @dataclass decoration
"""
from dataclasses import dataclass


@dataclass
class DemoDataClass:
    a: int
    b: float = 1.1
    c = "spam"  # class attribute


dc = DemoDataClass(9)
print("a dataclass object:", dc)
print("attribute access:", dc.a, dc.b, dc.c)
