"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 8 - Functions - Defining a Function
"""


def greet_user():
    """define a function with no parameter"""
    print("Hello!")


# invoke a function
greet_user()


def greet_user(username):
    """define a function with a single parameter"""
    print(f"Hello, {username.title()}!")


# invoke a function passing an argument
greet_user('jesse')
