"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque/exercism

Card Games https://exercism.org/tracks/python/exercises/card-games

Functions for tracking poker hands and assorted card tasks.
"""
import unittest
from lists import *


class TestCardGames(unittest.TestCase):
    def test_given_get_rounds(self):
        self.assertEqual(get_rounds(27), [27, 28, 29])

    def test_given_concatenate_rounds(self):
        self.assertEqual(concatenate_rounds(
            [27, 28, 29], [35, 36]), [27, 28, 29, 35, 36])

    def test_given_list_contains_round(self):
        round = [27, 28, 29, 35, 36]
        targets = [29, 30]
        expected_results = [True, False]

        for (target, expected) in zip(targets, expected_results):
            with self.subTest(input_data=target, output_data=expected):
                actual = list_contains_round(round, target)
                self.assertEqual(actual, expected)

    def test_given_card_average(self):
        self.assertEqual(card_average([5, 6, 7]), 6.0)

    def test_given_approx_average_is_average(self):
        rounds = [[1, 2, 3], [2, 3, 4, 8, 8], [1, 2, 3, 5, 9]]
        expected_results = [True, True, False]

        for (round, expected) in zip(rounds, expected_results):
            with self.subTest(input_data=round, output_data=expected):
                actual = approx_average_is_average(round)
                self.assertEqual(actual, expected)

    def test_given_average_even_is_average_odd(self):
        rounds = [[1, 2, 3], [1, 2, 3, 4]]
        expected_results = [True, False]

        for (round, expected) in zip(rounds, expected_results):
            with self.subTest(input_data=round, output_data=expected):
                actual = average_even_is_average_odd(round)
                self.assertEqual(actual, expected)

    def test_given_maybe_double_last(self):
        rounds = [[5, 9, 11], [5, 9, 10]]
        expected_results = [[5, 9, 22], [5, 9, 10]]

        for (round, expected) in zip(rounds, expected_results):
            with self.subTest(input_data=round, output_data=expected):
                actual = maybe_double_last(round)
                self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
