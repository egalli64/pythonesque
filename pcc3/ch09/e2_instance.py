"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 9 - Classes - Working with Classes and Instances
"""


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        # default value for a data attribute not matched by a parameter
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        return f"{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


a_car = Car('audi', 'a4', 2024)
print(a_car.get_descriptive_name())

# everything in a Python class is public
a_car.odometer_reading = 42
a_car.read_odometer()

# setter is not required but could make code more robust
a_car.update_odometer(23)
a_car.read_odometer()

# a bit more logic makes a method more useful
a_car.increment_odometer(48)
a_car.read_odometer()
