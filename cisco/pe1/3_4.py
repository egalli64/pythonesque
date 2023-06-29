"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 3 Section 4 Lists
"""
numbers = [10, 5, 7, 2, 1]
print(numbers)

numbers[0] = 111
print(numbers)

numbers[1] = numbers[4]
print(numbers)

print("First element:", numbers[0])
print("List length:", len(numbers))

del numbers[1]
print("After removing element 1, lenght is:", len(numbers))
print(numbers)

try:
    print(numbers[4])
except IndexError:
    print("Can't read an out of range element!")

try:
    numbers[4] = 1
except IndexError:
    print("Can't assign to an out of range element!")

# 3.4.5 Negative indices
print("Last element in list:", numbers[-1])

# 3.4.6 LAB
"""
Given a list of five numbers: 1, 2, 3, 4, and 5.
1. replace the middle number in the list with an integer entered by the user
2. remove the last element from the list
3. print the length of the existing list
"""
hat_list = [1, 2, 3, 4, 5]
print(hat_list)

hat_list[len(hat_list) // 2] = int(input("New element to put in the middle: "))
print("Central element changed:", hat_list)

del hat_list[-1]
print(f"Last element removed: {hat_list}, size:", len(hat_list))

# 3.4.8 Adding elements to a list: append() and insert()
print("Back to", numbers)

numbers.append(4)
print(f"After appending: {numbers}, size:", len(numbers))

numbers.insert(0, 222)
print(f"After inserting in position 0: {numbers}, size:", len(numbers))

# Creating an empty list
my_list = []
for i in range(5):
    my_list.append(i + 1)
print("Appending all items:", my_list)

my_list = []
for i in range(5):
    my_list.insert(0, i + 1)
print("Inserting in 0 all items", my_list)

# 3.4.9 Making use of lists
my_list = [10, 1, 8, 3, 5]
print("Working on", my_list)

total = 0
for i in range(len(my_list)):
    total += my_list[i]
print("Total (for-range):", total)

# for-each
total = 0
for cur in my_list:
    total += cur
print("Total (for-each):", total)

# swap
sz = len(my_list)
for i in range(sz // 2):
    j = sz - i - 1
    my_list[i], my_list[j] = my_list[j], my_list[i]

print("Swapping elements:", my_list)

# 3.4.11 LAB
"""
step 1: create an empty list named beatles
step 2: append() to the list: John Lennon, Paul McCartney, and George Harrison
step 3: use a for to append() members by input(): Stu Sutcliffe, and Pete Best
step 4: del Stu Sutcliffe and Pete Best from the list
step 5: insert() Ringo Starr to the beginning of the list
"""
beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Firstly:", beatles)

for i in range(2):
    beatles.append(input("Add a beatle: "))
print("Then:", beatles)

del beatles[-2]
print("A leave:", beatles)
del beatles[-1]
print("Another leave:", beatles)

beatles.insert(0, "Ringo Starr")
print("And finally:", beatles)
