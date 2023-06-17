"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 8 - Functions - Passing an Arbitrary Number of Arguments
"""


def make_pizza(*args):
    """
    A function expecting a variable number of arguments
    The parameter is a tuple whose size is determined at runtime
    """
    print('Making a pizza with')
    for arg in args:
        print('-', arg)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def print_info(**kwargs):
    """
    A function expecting a variable number of named (keyword) arguments
    The parameter is a dictionary
    """
    print('Info')
    for key in kwargs:
        print(key, '->', kwargs[key])


print_info(first='albert', last='einstein',
           location='princeton', field='physics')
