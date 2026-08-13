"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Typed Named Tuples
"""
from typing import NamedTuple


class Coordinate(NamedTuple):
    """
    Every instance field must be annotated with a type
    Any instance field could have a default value (following the usual rules)
    """
    lat: float
    lon: float
    reference: str = "WGS84"


print("a NamedTuple class is a tuple:", issubclass(Coordinate, tuple))

# hints: documentation that can be verified by IDEs and type checkers
trash = Coordinate("Ni!", None)
# we could have a warning from IDE/type checker, but Python does not mind about them
print(trash)
