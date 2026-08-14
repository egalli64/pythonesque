"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Keyword Class Patterns
"""
import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City('Asia', 'Tokyo', 'JP'),
    City('Asia', 'Delhi', 'IN'),
    City('North America', 'Mexico City', 'MX'),
    City('North America', 'New York', 'US'),
    City('South America', 'São Paulo', 'BR'),
]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            # filter by continent
            case City(continent='Asia'):
                results.append(city)
    return results


print(match_asian_cities())


def match_asian_countries():
    results = []
    for city in cities:
        match city:
            # filter by continent and capture its country attribute into the country local binding
            # here is pretty useless, using just city.country in the following code is more readable
            case City(continent='Asia', country=country):
                results.append(country)
    return results


print(match_asian_countries())
