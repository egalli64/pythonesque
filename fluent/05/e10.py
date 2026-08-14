"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Positional Class Patterns
"""
from e09 import City, cities


def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            # positional class pattern
            case City('Asia'):
                results.append(city)
    return results


print(match_asian_cities_pos())


def match_asian_countries_pos():
    results = []
    for city in cities:
        match city:
            # local binding, the positional way
            case City('Asia', _, country):
                results.append(country)
    return results


print(match_asian_countries_pos())
