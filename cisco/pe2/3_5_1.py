"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 5 – OOP Fundamentals: Inheritance
 1. Inheritance – why and how? 
 2. issubclass()
"""


class Star:
    def __init__(self, name, galaxy):
        self._name = name
        self._galaxy = galaxy

    def __str__(self):
        """Override the standard way an object converts itself to a string"""
        return self._name + ' in ' + self._galaxy


sun = Star("Sun", "Milky Way")
print("An object as string:", sun)


class Vehicle:
    """Base class"""
    pass


class LandVehicle(Vehicle):
    """is-a Vehicle"""
    pass


class TrackedVehicle(LandVehicle):
    """is-a LandVehicle"""
    pass


for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
    print(f"{cls1.__name__} is-a ...", end=' ')

    for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
        print(f"{cls2.__name__}?", issubclass(cls1, cls2), end='! ')
    print()