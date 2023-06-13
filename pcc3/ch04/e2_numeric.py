"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 4 - Working With Lists - Making Numerical Lists
"""
print("Numbers in a range left-close, right-open interval [0..5)")
for value in range(0, 5):
    print(value)

print("Range from 0 (implicit) to 5 (right-open)")
for value in range(0, 5):
    print(value)

numbers = list(range(1, 6))
print('A range generated list:', numbers)

even_numbers = list(range(2, 11, 2))
print('A range generated list of even numbers:', even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print('First ten squares:', squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Given", digits)
print("Min:", min(digits))
print("Max:", max(digits))
print("Sum:", sum(digits))

# List Comprehensions
print('First ten squares (List Comprehensions):', [value**2 for value in range(1, 11)])
