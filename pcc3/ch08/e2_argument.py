"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 8 - Functions - Passing Arguments
"""


def describe_pet(type, name):
    """Display information about a pet"""
    print(f"I have a {type}.", f"My {type}'s name is {name.title()}.")


# invoke a function matching argument to parameter by position
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# matching argument to parameter by name
describe_pet(type='hamster', name='harry')


def describe_pet(name, type='dog'):
    """Display information about a pet with default type"""
    print(f"I have a {type}.", f"My {type}'s name is {name.title()}.")


describe_pet(name='willie')

try:
    describe_pet()
except:
    print("Python can't guess pet name!")
