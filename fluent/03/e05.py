"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Standard API of Mapping Types: abc (Abstract Base Class)
"""
import collections
from collections import abc

a_dict = {}
print("A dict is an abc.Mapping:", isinstance(a_dict, abc.Mapping))
print("A dict is an abc.MutableMapping:", isinstance(a_dict, abc.MutableMapping))
print("A dict is a collections.UserDict:", isinstance(a_dict, collections.UserDict))
