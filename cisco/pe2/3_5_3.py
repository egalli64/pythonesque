"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 3 - Object-Oriented Programming
 Section 5 – OOP Fundamentals: Inheritance
 3. isinstance()
"""


class Vehicle:
    def __str__(self):
        return "vehicle"


class LandVehicle(Vehicle):
    def __str__(self):
        return "land vehicle"


class TrackedVehicle(LandVehicle):
    def __str__(self):
        return "tracked vehicle"


my_vehicle = Vehicle()
my_land_vehicle = LandVehicle()
my_tracked_vehicle = TrackedVehicle()

for obj in [my_vehicle, my_land_vehicle, my_tracked_vehicle]:
    print(f"{obj} is-a ...", end=' ')
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(f"{cls.__name__}?", isinstance(obj, cls), end='! ')
    print()
