"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Pattern Matching with Mappings - extracts names of creators from media records
"""
from collections import OrderedDict


def get_creators(record: dict) -> list:
    match record:
        # when matching this pattern, extract the author names in a list and return it
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        # in api version 1 a single author name was expected, return it in a list
        case {"type": "book", "api": 1, "author": name}:
            return [name]
        # no other type:book is expected
        case {"type": "book"}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        # like book api version 1
        case {"type": "movie", "director": name}:
            return [name]
        # no more valid records
        case _:
            raise ValueError(f"Invalid record: {record!r}")


# partial mapping matching is accepted
b1 = dict(api=1, author="Douglas Hofstadter", type="book", title="Gödel, Escher, Bach")
print(get_creators(b1))

b2_authors = "Martelli Ravenscroft Holden".split()
b2 = OrderedDict(api=2, type="book", title="Python in a Nutshell", authors=b2_authors)
print(get_creators(b2))

try:
    get_creators({'type': 'book', 'pages': 770})
except ValueError as e:
    print(f"Expected failure: {e!r}")

try:
    get_creators({42: 'Spam, spam, spam'})
except ValueError as e:
    print(f"Expected failure: {e!r}")
