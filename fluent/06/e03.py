"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Choosing Between == and is (equality against identity)
"""
from random import choice

# identity is preferred for singleton
x = choice([None, 42, None])
if x is None:
    print("None has been chosen")
else:
    print("Lucky choice")

# sentinel objects are another typical use case for identity
END_OF_DATA = object()
data = [42, "hello!", END_OF_DATA]

for item in data:
    if item is END_OF_DATA:
        print("End of data")
    else:
        print("Doing something")
