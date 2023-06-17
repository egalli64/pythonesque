"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 9 - Classes - Creating and Using a Class
"""


class Dog:
    """
    A simple attempt to model a dog

    Each instance method must have a self parameter, the reference to the current object
    """

    def __init__(self, name, age):
        """
        Constructor must have this name
        Data members are defined in it
        """
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")


# an instance
willie = Dog('Willie', 6)
print('Name:', willie.name)
print('Age:', willie.age)
willie.sit()
willie.roll_over()

# another instance
lucy = Dog('Lucy', 3)
print('Name:', lucy.name)
print('Age:', lucy.age)
lucy.sit()
lucy.roll_over()
