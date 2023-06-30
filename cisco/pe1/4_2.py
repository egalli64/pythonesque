"""
Cisco Network Academy
Python Essentials 1: https://skillsforall.com/course/python-essentials-1
My notes: https://github.com/egalli64/pythonesque - cisco/pe1 folder

PE1: Module 4 Section 2 – How functions communicate with their environment
"""


def message(number):
    """
    Shadowing: the _parameter_ number hides the external variable number
    """
    print("Enter a number:", number)


# an unrelated variable with just the same name of the message() parameter
number = 1234
message(1)
print(number)

# 4.2.2 Positional parameter passing


def my_function(a, b, c):
    print(a, b, c)


# invoking a function passing the arguments by position
my_function(1, 2, 3)


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)


introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

# 4.2.3 Keyword argument passing
introduction(first_name="James", last_name="Bond")
introduction(last_name="Kurosawa", first_name="Akira")

try:
    introduction(surname="Skywalker", first_name="Luke")
except TypeError:
    print("Be careful in using the right parameter name!")

# 4.2.4 Mixing positional and keyword arguments


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)


# positional call
adding(1, 2, 3)

# keyword call
adding(c=1, a=2, b=3)

# mix
adding(3, c=1, b=2)
# works fine, it is just a bit strange
adding(4, 3, c=2)

try:
    adding(3, a=1, b=2)
except TypeError:
    print("Mixing calling styles is dangerous!")

# 4.2.5 Parametrized functions – more details


def introduction2(first_name, last_name="Smith"):
    """last_name has a _default value_"""
    print("Hi, my name is", first_name, last_name)


introduction2("James", "Doe")
introduction2("Henry")
introduction2(first_name="William")


def introduction3(first_name="John", last_name="Smith"):
    print("Hey, my name is", first_name, last_name)


introduction3()
introduction3("Tom")
introduction3(last_name="Hopkins")
