"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Tuples as Records
"""
# Example 2-7. Tuples used as records
lax_coordinates = (33.9425, -118.408056)
print("Lat/lon for Los Angeles Airport:", lax_coordinates)

city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
print(f"Data about a city: {city}, year {year}, population {pop} (x 1000), change {chg}%, area {area} km2")

print("Travelers info")
traveler_ids = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA205856")]
for passport in sorted(traveler_ids):
    # old-style
    print("\t(1) %s: %s" % passport, end="\t")
    # format + unpacking
    print("(2) {}: {}".format(*passport), end="\t")
    # usually preferred
    print(f"(3) {passport[0]}: {passport[1]}")

# using underscore to explicitly mark elements as not used in the for loop
for country, _ in sorted(traveler_ids):
    print(country)
