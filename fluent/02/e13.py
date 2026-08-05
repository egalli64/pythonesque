"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Destructuring nested tuples - Example 2-10
"""
from e11 import metro_areas


# compare this with the e11 code
def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    # each element in metro_areas is processed as record
    for record in metro_areas:
        match record:
            # use match-case to destructure the record
            # notice the filter by the optional if-clause
            case name, _, _, (lat, lon) if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


if __name__ == '__main__':
    main()
