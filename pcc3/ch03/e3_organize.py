"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 3 - Introducing Lists - Organizing a List
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Before sorting:', cars)
cars.sort()
print('After sorting:', cars)
cars.sort(reverse=True)
print('Reverse sort:', cars)

sorted_cars = sorted(cars)
print('Sorted copied list:', sorted_cars)
print('Original list:', cars)

sorted_cars.reverse()
print('The sorted list reversed:', sorted_cars)

print('Number of cars:', len(cars))