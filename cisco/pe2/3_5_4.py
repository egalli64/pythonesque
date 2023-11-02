"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 5 – OOP Fundamentals: Inheritance
 4 The is operator
"""


class SampleClass:
    def __init__(self, val):
        self.val = val


objects = [SampleClass(0), SampleClass(1)]
objects.append(objects[1])
objects[2].val += 1
print([x.val for x in objects])

for i in range(len(objects)-1):
    for j in range(i+1, len(objects)):
        print(f"object[{i}] is object[{j}]?", objects[i] is objects[j])

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print("Comparing objects vs comparing references:", string_1 == string_2, string_1 is string_2)
