"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 4 Section 4 – Scopes in Python
"""


def scope_test():
    x = 123
    print("A variable local to a function", x)


scope_test()
try:
    print(x)
except NameError:
    print("It is not possible to access a local variable outside its scope")


def my_function():
    print("Accessing a variable in the global scope from a function:", var)


var = 1
my_function()
print("Accessing a variable in the global scope:", var)


def my_function2():
    # the local "var" is shadowing the global "var"
    var = 2
    print("Accessing the local var:", var)


my_function2()
print("Accessing the global var in its scope:", var)

# 4.4.2 Functions and scopes: the global keyword


def my_function3():
    # accessing the global "var", not creating a local one
    global var
    var = 2
    print("Changing the global var (yuk!):", var)


my_function3()
print("Accessing the global var in its scope:", var)

# 4.4.3 How the function interacts with its arguments
# Scalar arguments are passed by value


def my_function4(n):
    print("I got", n)
    n += 1
    print("I have", n)


my_function4(var)
print("The global var has not changed:", var)

# Passing a list


def my_function(list_p):
    print("#1 (p):", list_p)
    print("#2 (g):", list_g)
    list_p = [0, 1]
    print("#3 (a new list is created and its pointer is assigned to p):", list_p)
    print("#4 (g unaffected):", list_g)


list_g = [2, 3]
my_function(list_g)
print("#5 (g unaffected):", list_g)


def my_function(list_p):
    print("#1 (p):", list_p)
    print("#2 (g):", list_g)
    del list_p[0]
    print("#3 (an element in p as been removed):", list_p)
    print("#4 (g see the changes too):", list_g)


my_function(list_g)
print("#5 (g changed):", list_g)
