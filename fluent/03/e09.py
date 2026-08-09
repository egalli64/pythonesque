"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

The __missing__ Method
"""
from typing import override


class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            # see get implementation here below - without this check expect an infinite recursion
            raise KeyError(key)
        else:
            return self[str(key)]

    @override
    def get(self, key, default=None):
        try:
            # could trigger __missing__
            return self[key]
        except KeyError:
            return default

    @override
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([("2", "two"), ("4", "four")])

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
