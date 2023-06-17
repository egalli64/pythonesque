"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 8 - Functions - Passing a List
"""


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        print(f"Hello, {name.title()}!")


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        design = unprinted_designs.pop()
        print(f"Printing model: {design}")
        completed_models.append(design)


def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("The following models have been printed:")
    for model in completed_models:
        print(model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List
designs = ['phone case', 'robot pendant', 'dodecahedron']
models = []

print('The design list:', designs)
# force a list deep copy, so that the original list stay untouched
print_models(designs[:], models)
show_completed_models(models)
print('The design list:', designs)
