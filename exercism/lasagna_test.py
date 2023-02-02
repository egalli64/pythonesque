"""
Exercism Python track

Source: https://exercism.org/tracks/scala
My solutions: https://github.com/egalli64/pythonesque/exercism

Guido's Gorgeous Lasagna
https://exercism.org/tracks/python/exercises/guidos-gorgeous-lasagna/edit
"""
import unittest
from lasagna import *


class TestLasagna(unittest.TestCase):

    def test_expected_bake_time(self):
        self.assertEqual(EXPECTED_BAKE_TIME, 40)

    def test_bake_time_remaining(self):
        values = [1, 2, 5, 10, 15, 23, 33, 39]
        results = [40 - item for item in values]

        for i, (time, expected) in enumerate(zip(values, results), start=1):
            with self.subTest(f'variation #{i}: input {time}, expected {expected}'):
                actual = bake_time_remaining(time)
                self.assertEqual(actual, expected)

    def test_preparation_time_in_minutes(self):
        values = [1, 2, 5, 8, 11, 15]
        results = [item * 2 for item in values]

        for i, (layers, expected) in enumerate(zip(values, results), start=1):
            with self.subTest(f'variation #{i}: input {layers}, expected {expected}'):
                actual = preparation_time_in_minutes(layers)
                self.assertEqual(actual, expected)

    def test_elapsed_time_in_minutes(self):
        layers = (1, 2, 5, 8, 11, 15)
        elapseds = (3, 7, 8, 4, 15, 20)
        results = [layer * 2 + elapsed for layer,
                   elapsed in zip(layers, elapseds)]

        for i, (layers, time, expected) in enumerate(zip(layers, elapseds, results), start=1):
            with self.subTest(f'variation #{i}: {layers}, {time} -> {expected}'):
                actual = elapsed_time_in_minutes(layers, time)
                self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
