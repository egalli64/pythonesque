"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 8 - Functions - Storing Your Functions in Modules

The pizza module
"""


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f'Making a {size}-inch pizza with')
    for topping in toppings:
        print('-', topping)
