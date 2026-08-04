"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Cartesian Products
"""
colors = ('black', 'white')
sizes = ('S', 'M', 'L')

# listcomp to generate the cartesian product colors x sizes
# each color mapped against each size
t_shirts = [(color, size) for color in colors for size in sizes]
print(t_shirts)

# just print each element in the cartesian product, without generating a list
for color in colors:
    for size in sizes:
        print((color, size))

# each size mapped against each color
t_shirts = [(color, size) for size in sizes for color in colors]
print(t_shirts)
