"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2 Module 4 - Miscellaneous
 Section 1 - Generators, iterators, and closures
 1 Generators - where to find them
"""
# A range is a generator, that is an iterator
for i in range(3):
    print(i, end="")
print()


class Fib:
    """Fibonacci generator"""

    def __init__(self, n):
        self._n = n
        self._i = 0
        self._p1 = self._p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("[__next__", end="] ")
        self._i += 1
        if self._i > self._n:
            print("Stopping iteration")
            raise StopIteration
        if self._i in [1, 2]:
            return 1
        result = self._p1 + self._p2
        self._p1, self._p2 = self._p2, result
        return result


for i in Fib(10):
    print(i)

# Other example


class Fib2:
    def __init__(self, n):
        self._n = n
        self._i = 0
        self._p1 = self._p2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._i += 1
        if self._i > self._n:
            raise StopIteration
        if self._i in [1, 2]:
            return 1
        result = self._p1 + self._p2
        self._p1, self._p2 = self._p2, result
        return result


class Class:
    def __init__(self, n):
        self._iterator = Fib2(n)

    def __iter__(self):
        print("Using the class iterator")
        return self._iterator


object = Class(8)

for i in object:
    print(i)
