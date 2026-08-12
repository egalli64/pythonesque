"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Basic data class
"""


class Coordinate:
    """A supersimple data class"""

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


moscow = Coordinate(55.76, 37.62)
print("standard __repr__ is pretty useless:", moscow)

location = Coordinate(55.76, 37.62)
if location != moscow:
    print("Comparison is pretty useless too")

if (location.lat, location.lon) == (moscow.lat, moscow.lon):
    print("At least a workaround is almost bearable")
