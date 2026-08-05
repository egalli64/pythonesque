"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Nested Unpacking
"""
# Example 2-8. Unpacking nested tuples - notice the last element of each record, a nested tuple
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    # the middle elements are ignored, the last one is unpacked
    for name, _, _, (lat, lon) in metro_areas:
        # filter, only the western elements are used
        if lon <= 0:
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == '__main__':
    main()
