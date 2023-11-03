"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 4 – OOP: Methods
 1. Methods in detail
"""


class Classy:
    a_class_variable = 2

    def __init__(self, value=None):
        self.value = value

    def method(self):
        print("'method' has been called on a Classy object")

    def method2(self, par):
        """No overload in Python"""
        print("method2:", par)

    def method3(self):
        """A method using self"""
        print("method3:", Classy.a_class_variable, self.a_property)
        self.other()

    def other(self):
        print("other")


obj = Classy()
obj.method()

obj.method2(1)
obj.method2(2)
obj.method2(3)

# Yuck!
obj.a_property = 3
obj.method3()

obj2 = Classy(42)
print("Accessing a property defined by the ctor:", obj2.value)
