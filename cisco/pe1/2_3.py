"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 2 Section 3 Operators - data manipulation tools
"""
# Basic operators
print('4 + 2 =', 4 + 2)
print('4 - 2 =', 4 - 2)
print('4 * 2 =', 4 * 2)
print('4 / 2 =', 4 / 2)
print('(floor division) 4 // 2 =', 4 // 2)
print('6 // 4 =', 6 // 4)
print('(tricky!) -6 // 4 =', -6 // 4)
print('4 % 2 =', 4 % 2)
print('4 ** 2 =', 4 ** 2)
print('4 ** 2.0 =', 4 ** 2.0)

try:
    print(2 // 0)
except ZeroDivisionError:
    print("Can't divide an integer by zero!")

try:
    print(2.0 / 0.0)
except ZeroDivisionError:
    print("Can't divide any number by zero!")

try:
    print(2 % 0)
except ZeroDivisionError:
    print("Can't get a modulo zero!")

print('Multiplication has an higher priority than sum: 2 + 3 * 5 =', 2 + 3 * 5)
print('Binding is (usually) from left to right: 9 % 6 % 2 =', 9 % 6 % 2)
print('Binding for exponents is from right to left: 2 ** 1 ** 3 =', 2 ** 1 ** 3)
print('Right binding beats unary minus, exponents has top priority: -3 ** 2 =', -3 ** 2)
print('Use parenthesis to force evaluation order: (2 ** 1) ** 3 =', (2 ** 1) ** 3)
