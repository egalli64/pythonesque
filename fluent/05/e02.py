"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Classic Named Tuples
"""
from collections import namedtuple
import json

# define the namedtuple class by the namedtuple factory function
City = namedtuple('City', 'name country population coordinates')
print("a namedtuple class is a tuple:", issubclass(City, tuple))

# create a namedtuple object passing the values for each field
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print("a namedtuple object:", tokyo)

print(f"accessing fields by name: population is {tokyo.population}, coordinates are {tokyo.coordinates}")
print(f"accessing fields by position: 1 is {tokyo[1]}, 3-0 is {tokyo[3][0]}")

# helper: the city fields
print("the City fields:", City._fields)

Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))

# create a namedtuple passing an iterable - with the expected values
delhi = City._make(delhi_data)

# see a namedtuple as a dict - useful, for instance, to interact with other modules, as json
print("Dehli as dict:", delhi._asdict())
print("Dehli as JSON:", json.dumps(delhi._asdict()))

# providing default values for the _last_ elements:
Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=[0, 'WGS84'])
print("the coordinate field default values:", Coordinate._field_defaults)
print("a coordinate with defaults:", Coordinate(0))
