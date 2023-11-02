"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 4 – OOP: Methods
 2. The inner life of classes and objects
"""


class Classy:
    varia = 1

    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass


obj = Classy()

print("The object dictionary:", obj.__dict__)
print("The class dictionary:", Classy.__dict__)

print("The class name:", Classy.__name__)
print("The type of obj:", type(obj))

print("The class module:", Classy.__module__)
print("The object module:", obj.__module__)


class Sub(Classy):
    pass


print("Classy bases:", Classy.__bases__)
print("Sub bases:", Sub.__bases__)
