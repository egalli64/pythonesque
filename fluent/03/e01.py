"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/03-dict-set/03-dict-set.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

dict Comprehensions
"""

dial_codes_iterable = [
    (880, "Bangladesh"),
    (55, "Brazil"),
    (86, "China"),
    (91, "India"),
    (62, "Indonesia"),
    (81, "Japan"),
    (234, "Nigeria"),
    (92, "Pakistan"),
    (7, "Russia"),
    (1, "United States"),
]

# map each dial code with its country
dial_code = dict(dial_codes_iterable)
print(dial_code)

# map each country with its dial code
country_dial = {country: code for code, country in dial_codes_iterable}
print(country_dial)

# dict-comp: sort - filter by code - reverse key-value - uppercase the country name
a_dict = {code: country.upper() for country, code in sorted(country_dial.items()) if 80 < code < 100}
print(a_dict)
