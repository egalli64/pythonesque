"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

Deep and Shallow Copies of Arbitrary Objects
"""
import copy
from typing import override


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    @override
    def __repr__(self) -> str:
        return f"Bus({self.passengers})"


bus1 = Bus(["Alice", "Bill", "Claire", "David"])
print("the original bus:", bus1, id(bus1))
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(f"the copy has id {id(bus2)}, and the deep copy {id(bus3)}")

bus1.drop("Bill")
print("Bill is dropped from bus 1 (and 2)", bus1.passengers, id(bus1.passengers), id(bus2.passengers))
print("Bus 3 has its own passenger list:", bus3.passengers, id(bus3.passengers))
