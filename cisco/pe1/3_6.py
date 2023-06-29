"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 3 Section 6 – Operations on lists
"""
list_1 = [1]
# shallow copy
list_2 = list_1
list_1[0] = 2
print("Two aliases to the same data:", list_1, list_2)

# deep copy
list_2 = list_1[:]
list_1[0] = 3
print("Data have been copied in a different place:", list_1, list_2)

my_list = [10, 8, 6, 4, 2]
print("A list:", my_list)
new_list = my_list[1:3]
print("Slice 1:3 of the previous list:", new_list)

# 3.6.3 Slices – negative indices
new_list = my_list[1:-1]
print("Slice 1:-1 (no extremes):", new_list)

print("Slice :3 (first three elements):", my_list[:3])
print("Slice :3 (from element[3] on):", my_list[3:])

del my_list[1:3]
print("After removing the slice [1:3]:", my_list)

del my_list[:]
print("After removing the slice [:]:", my_list)

try:
    del my_list
    print(my_list)
except NameError:
    print("The name my_list is not associated to a variable anymore!")

# 3.6.4 The in and not in operators
my_list = [0, 3, 12, 8, 2]
print("The list:", my_list)

print("Is 5 in list?", 5 in my_list)
print("Is 5 not in list?", 5 not in my_list)
print("Is 12 in list?", 12 in my_list)

# 3.6.5 Lists – some simple programs
# max
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print("The largest element in list is", largest)

largest = my_list[0]
for cur in my_list:
    if cur > largest:
        largest = cur
print("The largest element in list is", largest)

largest = my_list[0]
for cur in my_list[1:]:
    if cur > largest:
        largest = cur
print("The largest element in list is", largest)

# find
to_find = 5
print(f"Look for {to_find} in {my_list}")

found = False
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Found at index", i)
else:
    print("Not found")

# list intersection
drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]

print(f"Count how many element in {drawn} are in {bets}")

hits = 0
for number in bets:
    if number in drawn:
        hits += 1

print(hits)

# 3.6.6 LAB - remove duplicates (using only lists!)
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
singles = []

for cur in my_list:
    if cur not in singles:
        singles.append(cur)

print(f"From {my_list} to {singles}")
