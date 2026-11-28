"""
Fluent Python (Second Edition) by Luciano Ramalho
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/

Original code: https://github.com/fluentpython/example-code-2e/
My playground: https://github.com/egalli64/pythonesque/ fluent folder

ArithmeticProgression, a generalized range.
"""


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        """generate a progression from begin to end (None means no end), for the given step"""
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        # the actual return type is determined dynamically
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)

        # local variable for condition readability
        forever = self.end is None
        # helper to reduce floating point error accumulation
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            # precalculate the next required value
            result = self.begin + self.step * index
