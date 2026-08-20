"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Anonymous Functions
"""
fruits = ["strawberry", "fig", "apple", "cherry", "raspberry", "banana"]
print("original fruits: ", fruits)
print("weirdly sorted fruits:", sorted(fruits, key=lambda word: word[::-1]))
