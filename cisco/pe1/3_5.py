"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 3 Section 5 Sorting simple lists: the bubble sort algorithm
"""
my_list = [8, 10, 6, 2, 4]
print("List:", my_list)

while True:
    ordered = True
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            ordered = False
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    if ordered:
        break

print("Sorted list:", my_list)

# lazy version
my_list = [8, 10, 6, 2, 4]
print("List:", my_list)

sz = len(my_list) - 1
for i in range(sz):
    for j in range(sz):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
print("Sorted list:", my_list)

# much easier and performing
my_list = [8, 10, 6, 2, 4]
print("List:", my_list)
my_list.sort()
print("Sorted list:", my_list)
