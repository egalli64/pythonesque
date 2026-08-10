"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Immutable Mappings
"""
from types import MappingProxyType

a_dict = {1: 'A'}

a_mapping_proxy = MappingProxyType(a_dict)
print(f"A mapping proxy: {a_mapping_proxy!r}")

print(a_mapping_proxy[1])
try:
    a_mapping_proxy[2] = 'x'
except TypeError as e:
    print(f"can't assign new value to a_mapping_proxy, {e!r}")

a_dict[2] = 'B'
print(f"Now mapping proxy is {a_mapping_proxy!r}")
