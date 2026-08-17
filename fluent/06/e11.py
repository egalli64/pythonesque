"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Defensive Programming with Mutable Parameters
"""


class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # DANGER! the bus passenger list is an alias of the input one
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ["Sue", "Tina", "Maya", "Diana", "Pat"]
print("the team:", basketball_team)
bus = TwilightBus(basketball_team)
bus.drop("Tina")
bus.drop("Pat")
print("now the team is:", basketball_team)


class FixBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # generate a new list from the input one
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


basketball_team = ["Sue", "Tina", "Maya", "Diana", "Pat"]
print("the team:", basketball_team)
bus = FixBus(basketball_team)
bus.drop("Tina")
bus.drop("Pat")
print("now the team is:", basketball_team)
print("bus passengers:", bus.passengers)
