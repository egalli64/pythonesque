"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

collections.ChainMap
"""
from collections import ChainMap

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
chain = ChainMap(d1, d2)

print("two plain dicts:", d1, d2)
print("chained:", chain)

# lookup in chain is performed in association order
print("looking in the chain for 'a' and 'c' give:", chain["a"], chain["c"])

# upsert work on the first dict only
chain["c"] = -1
print("Changing 'c' on chain gives:", chain)
