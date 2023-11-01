"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 3 – OOP: Properties
 2. Class variables
"""


class ExampleClass:
    """A class with a class variable"""
    counter = 0

    def __init__(self, val=1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
print("Accessing a class variable in a clean way:", ExampleClass.counter)

print("The class dictionary:", ExampleClass.__dict__)
example_object = ExampleClass(2)

print("The class dictionary:", ExampleClass.__dict__)
print("The object dictionary:", example_object.__dict__)
