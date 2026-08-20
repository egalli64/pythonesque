"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

User-Defined Callable Types
"""
import random


class BingoCage:
    def __init__(self, items):
        # defensive copy of the passed sequence
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
print("using bingo as a plain object:", bingo.pick())
print("using bingo as a callable:", bingo())
print("bingo is actually a callable: ", callable(bingo))
