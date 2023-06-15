"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 5 - If Statement - Using if Statements with Lists
"""
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# loop on all toppings
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("Finished making your pizza!\n")

# loop on toppings but green peppers
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("Finished making your pizza!\n")

# avoid looping on an empty list
requested_toppings.clear()
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?\n")

available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!\n")
