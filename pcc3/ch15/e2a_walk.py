"""
Python Crash Course, Third Edition https://ehmatthes.github.io/pcc_3e/
My notes: https://github.com/egalli64/pythonesque/pcc3

Chapter 15 - Generating Data - Random Walks
"""
from random import randint


class RandomWalk:
    """Random walk generator"""

    def __init__(self, num_points=5_000):
        self.num_points = num_points

        # set origin to (0, 0)
        self.xs = [0]
        self.ys = [0]

        while len(self.xs) < self.num_points:
            # left or right?
            x_step = randint(-4, 4)
            # up or down?
            y_step = randint(-4, 4)

            # reject moves that go nowhere
            if not (x_step == 0 and y_step == 0):
                self.xs.append(self.xs[-1] + x_step)
                self.ys.append(self.ys[-1] + y_step)
