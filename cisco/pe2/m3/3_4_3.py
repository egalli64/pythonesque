"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 4 – OOP: Methods
 3. Reflection and introspection
"""


class MyClass:
    """An empty class"""
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
