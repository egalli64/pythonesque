"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 4 Section 8 - Test
"""
print("-1- function signature")


def fun():
    pass


print("-2- default parameter")


def function(x=0):
    return x


print(function())
print(function(42))

print("-4- tuple as sequence")
t1 = (1, 2, 3)
for x in t1:
    print(x)
print(t1[0], t1[1:-1], t1[-1])

print("-5- Recursive calls")


def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)


print(f(3))

print("-6- Recursive calls")


def fun(x):
    x += 1
    return x


x = 2
x = fun(x + 1)
print(x)

print("-7- Dictionary, list, tuple")


dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )

for i in sorted(dictionary.keys()):
    k = dictionary[i]
    # Insert your code here to get a b c on three lines
    print(k[0])

print("-8- function parameters")


def func(a, b):
    return a ** a


try:
    print(func(2))
except TypeError:
    print("Missing argument!")

print("-9- function")


def func_1(a):
    return a ** a


def func_2(a):
    return func_1(a) * func_1(a)


print(func_2(2))

print("-10- function with default arguments")


def fun(a=0, b=0):
    pass


print("-11- None")

a = 42
if a is not None:
    print("Not None:", a)

a = None
if a is None:
    print("None:", a)

print("-12- None")


def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return


x = fun(fun(2))
try:
    print(x + 1)
except TypeError:
    print("Can't add to None")

print("-13- global")


def fun(x):
    global y
    y = x * x
    return y


fun(2)
print(y)

print("-14- global")


def any():
    print(var + 1, end='')


var = 1
any()
print(var)

print("-15- tuple")

my_tuple = (1, 2, 3)

try:
    my_tuple[1] = my_tuple[1] + my_tuple[0]
except TypeError:
    print("Tuple is immutable!")

print("-16- list / function space name")

# my_list = ['Mary', 'had', 'a', 'little', 'lamb']


# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'


# print(my_list(my_list))

print("-17- positional / by name")


def fun(x, y, z):
    return x + 2 * y + 3 * z


print(fun(0, z=1, y=3))

print("-18- by name / default")


def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

print("-19- dictionary (pure silliness)")

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']

for k in range(len(dictionary)):
    v = dictionary[v]

print(v)

print("-20- tuple")

tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)

print("-22- exception")


try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
