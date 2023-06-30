"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 3 Section 8 – Test
"""
print("-2- dynamic type")
x = 1
x = x == x
print(x)

print("-3- while loop")
i = 0
while i <= 3:
    i += 2
    print("*")

print("-4- break")
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")

print("-5- for else")
for i in range(1):
    print("#")
else:
    print("#")

print("-6- continue")
var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

print("-7- left shift")
var = 1
while var < 10:
    print("#")
    var = var << 1

print("-8- boolean operators")
z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

print("-9- bitwise operators")
a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)

print("-10- list")
my_list = [3, 1, -2]
print(my_list[my_list[-1]])

print("-11- slice")
my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

print("-12- swap")
vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]
print(vals)

print("-13- list ops")
vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]
print(vals)

print("-14- shallow copy")
nums = [1, 2, 3]
vals = nums
del vals[1:2]
print(nums, vals)

print("-15- deep copy (tricky)")
nums = [1, 2, 3]
vals = nums[-1:-2]
print(nums, vals)

print("-16- for each / insert")
my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

print("-17- insert on list while loopin on it (don't do such things in production code!)")
my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

print("-18- list comprehension")
my_list = [i for i in range(-1, 2)]
print(my_list)

print("-19- matrix")
t = [[3-i for i in range(3)] for j in range(3)]
print(t)
s = 0
for i in range(3):
    s += t[i][i]
print(s)

print("-20- matrix")
my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list)
try:
    print(my_list[2][0])
except IndexError:
    print("Out of range!")
