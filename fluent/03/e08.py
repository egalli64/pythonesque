"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

defaultdict
"""
import collections

# the callable passed to the constructor is used to create a new value for a new key
a_default_dict = collections.defaultdict(list)
a_default_dict["a"].append(42)
a_default_dict["a"].append(12)
a_default_dict["b"].append(5)
a_default_dict["b"].append(4)
a_default_dict["c"].append(3)
print(a_default_dict)

for key in "cd":
    a_default_dict[key].append(99)
print(a_default_dict)
