"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Final Test
"""
print("-1- list insert")
my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)

print("-5- None")


def function_1(a):
    return None


def function_2(a):
    return function_1(a) * function_1(a)


try:
    print(function_2(2))
except TypeError:
    print("None is a bad beast")

print("-6- integer division")
print(1 // 2)

print("-7- positional and keyword argument")


def func(a, b):
    return b ** a

# print(func(b=2, 2))


print("-8- boolean operators")
z = 0
y = 10
x = y < z and z > y or y < z and z < y
print(x)

print("-9- variables and functions")
# Naming a variable as an existing function is legal (but not a good idea)
original_print = print
print = 42

original_print(print)
print = original_print

print("Back to normality")

print("-10- list, index, del")
my_list = [x * x for x in range(5)]
print("my_list", my_list)


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))

print("-11- assignment / swap")
x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

print("-12- XOR to swap")
a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

print("-13- function")


def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))

print("-14- list, del")

nums = [1, 2, 3]
vals = nums
del vals[:]
print(nums, vals)

print("-15- modulo operator")

x = 3
y = 2

x = x % y
x = x % y
y = y % x

print(y)

print("-16- string concatenation")
y = "3"
x = "6"
print(x + y)

print("-17- print separator")
print("a", "b", "c", sep="sep")

print("-18- joy of divisions")
x = 1 // 5 + 1 / 5
print(x)

print("-19- tuple")
my_tuple = (1, 2, 3)
try:
    my_tuple[1] = my_tuple[1] + my_tuple[0]
except TypeError:
    print("Tuple is immutable")

print("-20- float")
x = float("2")
y = float("4")
print(y ** (1 / x))


print("-21- dictionary")
dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]
print(v)

print("-22- list comprehension, range")
lst = [i for i in range(-1, -2)]
print(lst)

print("-23- function invoking")


def fun(a, b, c=0):
    print("ok")


fun(0, 1, 2)
try:
    fun()
except TypeError:
    print("Missing a and b")
fun(b=0, a=0)
try:
    fun(b=1)
except TypeError:
    print("Missing b")

print("-24- recursive function")


def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))

print("-25- beware of infinite loop")
i = 0
while i < i + 2:
    i += 1
    print("*")
    if i > 10:
        print("Got it, thank you")
        break
else:
    print("*")

print("-26- tuple")
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

print("-27- dictionary values()")
dd = {"1": "0", "0": "1"}
try:
    for x in dd.vals():
        print(x, end="")
except AttributeError:
    print("Python runtime check of attributes is a pain!")

print("-28- Dictionary and tuple")
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

print("-29- Function default argument")


def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

print("-30- list comprehension")
lst = [[x for x in range(3)] for y in range(3)]
print(lst)

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

print("-31-")
try:
    value = "0"
    print(int(value)/len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")

print("-32- SyntaxError")
try:
    print(5/0)
    # break
# except:
#    print("Sorry, something went wrong...")
except (ValueError, ZeroDivisionError):
    print("Too bad...")

print("-33- index()")
foo = (1, 2, 3)
try:
    foo.index(0)
except ValueError:
    print("Not found")

print("-34- exception")

try:
    1 // 0
except (TypeError, ValueError, ZeroDivisionError):
    print("A")

# try:
#     1 // 0
# except TypeError, ValueError, ZeroDivisionError:
#     print("B")

try:
    1 // 0
except:
    (TypeError, ValueError, ZeroDivisionError)
    print("C")

try:
    1 // 0
except:
    TypeError, ValueError, ZeroDivisionError
    print("D")

# try:
#     1 // 0
# except (TypeError, ValueError, ZeroDivisionError)
#     print("E")


# try:
#     1 // 0
# except TypeError, ValueError, ZeroDivisionError
#     print("F")

print("-35- SyntaxError")
# print(Hello, World!)
