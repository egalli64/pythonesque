"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 2 - Numbers
"""
# Integers
print("2 + 3 =", 2 + 3)
print("8 - 3 =", 8 - 3)
print("2 * 3 =", 2 * 3)
# "plain" division leads to float, even with integer operands
print("2 / 3 =", 2 / 3)
# integer division
print("2 // 3 =", 2 // 3)

# power
print("2 ** 3 =", 2 ** 3)

# evaluation order, multiplicative operations first
print("2 + 3 * 4 =", 2 + 3 * 4)

# forcing evaluation order with parentheses
print("(2 + 3) * 4 =", (2 + 3) * 4)

# Floats
# like integer, but beware of rounding issues
print("0.2 + 0.1 =", 0.2 + 0.1)
# mixing integer and float leads to float
print("1.0 + 2 =", 1.0 + 2)

# use underscore to improve readability of large numbers
universe_age = 14_000_000_000
print(universe_age)

# just as hint, constant names are all in uppercase
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)
