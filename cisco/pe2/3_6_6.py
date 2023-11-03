"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 6 - Exceptions once again
 4. How to create your own exception
"""


# A first example
class MyZeroDivisionError(ZeroDivisionError):
    pass


def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")


for mode in [False, True]:
    try:
        do_the_division(mode)
    except ZeroDivisionError:
        print("Division by zero")

for mode in [False, True]:
    try:
        do_the_division(mode)
    except MyZeroDivisionError:
        print("My division by zero")
    except ZeroDivisionError:
        print("Original division by zero")


# A second example
class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


def make_pizza(pizza, cheese):
    if pizza not in ["margherita", "capricciosa", "calzone"]:
        raise PizzaError(pizza, "no such pizza on the menu")
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "too much cheese")
    print("Pizza ready!")


for pizza, cheese in [("calzone", 0), ("margherita", 110), ("silliness", 20)]:
    try:
        make_pizza(pizza, cheese)
    except TooMuchCheeseError as ex:
        print(ex, ":", ex.cheese)
    except PizzaError as ex:
        print(ex, ":", ex.pizza)
