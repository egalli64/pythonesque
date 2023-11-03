"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 2 - Strings, List, Exceptions
 Section 7 – The anatomy of exceptions
 1. Exceptions
"""
import math

# The Python exception hierarchy
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Dividing by zero causes a ZeroDivisionError")

try:
    y = 1 / 0
except ArithmeticError:
    print("ZeroDivisionError is an ArithmeticError")

try:
    y = 1 / 0
except Exception:
    print("ArithmeticError is an Exception")

try:
    y = 1 / 0
except BaseException:
    print("Exception is a BaseException")


def bad_fun(n):
    """A function managing an exception internally"""
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")


if bad_fun(0) == None:
    print("Something bad happened in bad_fun")


def bad_fun_exc(n):
    """A function that causes an exception to be (implicitly) raised"""
    return 1 / n


try:
    bad_fun_exc(0)
except ArithmeticError:
    print("What happened? An exception was raised!")


def bad_fun_raising(n):
    """A function explicitly raising an exception"""
    raise ZeroDivisionError


try:
    bad_fun_raising(0)
except ArithmeticError:
    print("What happened? An error?")


def bad_fun_reraise(n):
    """A function that implicitly raises an exception, manages it, then re-raise it"""
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun_reraise(0)
except ArithmeticError:
    print("I see!")


values = [25, -1]

for value in values:
    try:
        assert value >= 0.0
        print(math.sqrt(value))
    except AssertionError:
        print("Discarding negative values")
