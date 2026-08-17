"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Mutable Types as Parameter Defaults: Bad Idea
"""


class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):
        """the mutable default argument value is looking for troubles - use None instead"""
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


bus1 = HauntedBus(["Alice", "Bill"])
print("bus 1 passengers:", bus1.passengers)

bus1.pick("Charlie")
bus1.drop("Alice")
print("passengers on bus 1 now:", bus1.passengers)

bus2 = HauntedBus()
bus2.pick("Carrie")
print("bus 2 passengers:", bus2.passengers)

bus3 = HauntedBus()
bus3.pick("Dave")
print("bus 2 and 3 share the passengers:", bus2.passengers is bus3.passengers, bus3.passengers)
print("no problem on bus 1:", bus1.passengers)
