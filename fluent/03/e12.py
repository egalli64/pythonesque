"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Subclassing UserDict Instead of dict - compare with StrKeyDict0 from e09
"""
from collections import UserDict


class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        else:
            return self[str(key)]

    def __contains__(self, key):
        # convert the input key to string - internally keys are all str now
        return str(key) in self.data

    def __setitem__(self, key, item):
        # convert to string on insertion
        self.data[str(key)] = item


d = StrKeyDict([("2", "two"), ("4", "four")])

# both string and integer are interpreted as expected
print(d["2"], d[4])

# no fallback provided, exception is generated
try:
    d[1]
except KeyError as e:
    print(f"{e!r}")

# use the fallback since the key (int or str) is not in there
print(d.get(1, 'N/A'))

# the in operator works fine too
print(2 in d, 1 in d, "4" in d)
