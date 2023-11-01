"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 3 – OOP: Properties
 1. Instance variables
"""


class ExampleClass:
    def __init__(self, val=1):
        self.first = val

    def set_second(self, val):
        """Yuck! A non-ctor adding a property to the current object"""
        self.second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
# terrible! changing the object structure from outside!
example_object_3.third = 5

# print the objects seen as dictionaries
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

print("---")


class ExampleClass2:
    def __init__(self, val=1):
        # sort of hidden object property
        self.__first = val

    def set_second(self, val=2):
        self.__second = val


example_object_1 = ExampleClass2()
example_object_2 = ExampleClass2(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass2(4)

example_object_3.__third = 5
print("Double underscore is completely useless here:", example_object_3.__third)

# the double underscored properties, when defined in the class, have a mangled name, but are still visible
print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
