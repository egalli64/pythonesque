"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 5 – OOP Fundamentals: Inheritance
 5. How Python finds properties and methods
"""


class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name}."


class Sub(Super):
    """super __str__ is inherited"""

    def __init__(self, name):
        Super.__init__(self, name)


obj = Sub("Andy")
print(obj)


class Sub2(Super):
    def __init__(self, name):
        """Using super() to access super class"""
        super().__init__(name)


obj2 = Sub2("Bob")
print(obj2)


class SuperA:
    """MI /A"""

    var_a = 10

    def fun_a(self):
        return 11


class SuperB:
    """MI /B"""

    var_b = 20

    def fun_b(self):
        return 21


class SubAB(SuperA, SuperB):
    """MI /AB"""

    pass


obj_ab = SubAB()

print(obj_ab.var_a, obj_ab.fun_a())
print(obj_ab.var_b, obj_ab.fun_b())

# Python MI - Left is evaluated before right
class Left:
    var = "L"
    var_left = "LL"

    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"

    def fun(self):
        return "Right"


class Sub_LR(Left, Right):
    pass


obj_lr = Sub_LR()

print(obj_lr.var, obj_lr.var_left, obj_lr.var_right, obj_lr.fun())
