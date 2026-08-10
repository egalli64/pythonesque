"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

collections.Counter
"""
from collections import Counter

counter = Counter("abracadabra")
print(counter)

counter.update("aaaaazzz")
print(counter)

print("The three most common elements:", counter.most_common(3))
