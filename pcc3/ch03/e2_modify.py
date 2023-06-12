"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 3 - Introducing Lists - Modifying, Adding, and Removing Elements
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# lists are mutable
motorcycles[0] = 'ducati'
print(motorcycles)

# push back
motorcycles.append('honda')
print(motorcycles)

# insert into
motorcycles.insert(0, 'mv agusta')
print(motorcycles)

# drop an element
del motorcycles[0]
print(motorcycles)

# pop the last element (see the list as a stack)
last = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {last.title()}.")

# pop anywhere
first = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first.title()}.")

# find and drop
motorcycles.remove('yamaha')

try:
    motorcycles.remove('ducati')
except ValueError:
    print("Can't remove a missing element")
