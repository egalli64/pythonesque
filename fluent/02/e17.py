"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/02-array-seq/array-seq.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Using + and * with Sequences
"""
a_list = [1, 2, 3]

# multiply the seq with an integer (both left/right works)
print(a_list * 3)
print(2 * a_list)

# both + and * create a new object
b_list = [4, 5, 6]
print(a_list + b_list)
