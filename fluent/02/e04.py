"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Generator Expressions
"""
import array

symbols = "$¢£¥€¤"

# genexp to create a tuple
codes = tuple(ord(symbol) for symbol in symbols)
print(codes)

# genexp to create an array
codes = array.array('I', (ord(symbol) for symbol in symbols))
print(codes)

# genexp generates elements but does not store them in a sequence
colors = ('black', 'white')
sizes = ('S', 'M', 'L')
# each t-shirt is deleted as soon as it is not referenced anymore
for t_shirt in (f'{color} {size}' for color in colors for size in sizes):
    print(t_shirt)
