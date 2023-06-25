"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque/cisco/pe1/

PE1: Module 2 Section 4 Variables – data-shaped boxes
"""
# an integer variable
var = 1
# a float variable
account_balance = 1000.0
# a string variable
client_name = 'John Doe'
# print them all
print(var, account_balance, client_name)

try:
    print(Var)
except NameError:
    print("If a variable is not defined can't be accessed!")

# changing the value in a variable by assignment
var = var + 1
print(var)

# apply the Pythagorean theorem
a = 3.0
b = 4.0
print(f"a is {a}, b is {b}")
c = (a ** 2 + b ** 2) ** 0.5
print("square root of (a square plus b square) is", c)

# Shortcut operators
x = 3
print('x is', x)
x = x * 2
print('after doubling x is', x)

sheep = 42
print('sheep is', sheep)
sheep = sheep + 1
print('after increasing by 1 sheep is', sheep)

x *= 2
sheep += 1
print('after doubling x and increasing sheep by 1, using shortcut operators:', x, sheep)

# Mile to kilometer converter
MILE_TO_KILOMETER = 1.61

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * MILE_TO_KILOMETER
kilometers_to_miles = kilometers / MILE_TO_KILOMETER

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
