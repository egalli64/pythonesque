"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original file: https://github.com/fluentpython/example-code-2e/blob/master/03-dict-set/03-dict-set.ipynb
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Basic ways to create a dictionary
"""
# literal dictionary
dict_a = {'one': 1, 'two': 2, 'three': 3}

# keyword arguments
dict_b = dict(three=3, one=1, two=2)

# from an iterable of pairs
dict_c = dict([('two', 2), ('one', 1), ('three', 3)])

# from parallel iterables via zip()
dict_d = dict(zip(['one', 'three', 'two'], [1, 3, 2]))

# when a dict is passed to the ctor, a shallow copy of the original one is generated
dict_e = dict({'three': 3, 'two': 2, 'one': 1})

print("They are all equals:", dict_a == dict_b == dict_c == dict_d == dict_e)
