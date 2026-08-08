"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Merging Mappings with |
"""
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}

# generate a merged mapping, same keys are overwritten
d3 = d1 | d2
print(d3)

# update a mapping in-place
d1 |= d2
print(d1)
