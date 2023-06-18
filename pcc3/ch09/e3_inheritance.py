"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 9 - Classes - Inheritance
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

    def fill_gas_tank(self):
        """A method that is going to be overridden"""
        print("Filling the tank for", self.get_descriptive_name())


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """
    ElectricCar is_a Car and has_a Battery

    Hierarchy: Car is the superclass of ElectricCar
    Composition: Car owns a Battery as a part of it
    """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class

        Call the constructor of the base class
        Then define the data member for the current class
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """
        Print a statement describing the battery size.

        Extends the base interface adding a new method specific for this class

        Delegation: the request is passed "as is" to its aggregate
        """
        self.battery.describe_battery()

    def fill_gas_tank(self):
        """
        Implicit method override

        Electric cars don't have gas tanks
        """
        print("This car doesn't have a gas tank!")


giulia = Car('alfa romeo', 'giulia', 2023)
print(giulia.get_descriptive_name())
giulia.fill_gas_tank()
# expect an AttributeError if running the next statement
# giulia.describe_battery()

leaf = ElectricCar('nissan', 'leaf', 2024)
print(leaf.get_descriptive_name())
leaf.fill_gas_tank()
leaf.describe_battery()
# not using delegation (yuck!)
leaf.battery.get_range()
