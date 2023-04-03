"""
Exercism Python track

Source: https://exercism.org/tracks/python
My solutions: https://github.com/egalli64/pythonesque/exercism

Black Jack https://exercism.org/tracks/python/exercises/black-jack

Functions to help play and score a game of blackjack.
"""
import unittest
from black_jack import *


class TestBlackJack(unittest.TestCase):
    def test_given_value_of_card(self):
        card = ['K', '4', 'A']
        expected = [10, 4, 1]
        for i, (card, expected) in enumerate(zip(card, expected)):
            with self.subTest(i, input_data=card, output_data=expected):
                self.assertEqual(value_of_card(card), expected)

    def test_given_higher_card(self):
        cards = [('K', '10'), ('4', '6'), ('K', 'A')]
        expected = [('K', '10'), '6', 'K']
        for i, (cards, expected) in enumerate(zip(cards, expected)):
            with self.subTest(i, input_data=cards, output_data=expected):
                self.assertEqual(higher_card(cards[0], cards[1]), expected)

    def test_given_value_of_ace(self):
        cards = [('6', 'K'), ('7', '3')]
        expected = [1, 11]
        for i, (cards, expected) in enumerate(zip(cards, expected)):
            with self.subTest(i, input_data=cards, output_data=expected):
                self.assertEqual(value_of_ace(cards[0], cards[1]), expected)

    def test_given_is_blackjack(self):
        cards = [('A', 'K'), ('10', '9')]
        expected = [True, False]
        for i, (cards, expected) in enumerate(zip(cards, expected)):
            with self.subTest(i, input_data=cards, output_data=expected):
                self.assertEqual(is_blackjack(cards[0], cards[1]), expected)

    def test_given_can_split_pairs(self):
        cards = [('Q', 'K'), ('10', 'A')]
        expected = [True, False]
        for i, (cards, expected) in enumerate(zip(cards, expected)):
            with self.subTest(i, input_data=cards, output_data=expected):
                self.assertEqual(can_split_pairs(cards[0], cards[1]), expected)

    def test_given_can_double_down(self):
        cards = [('A', '9'), ('10', '2')]
        expected = [True, False]
        for i, (cards, expected) in enumerate(zip(cards, expected)):
            with self.subTest(i, input_data=cards, output_data=expected):
                self.assertEqual(can_double_down(cards[0], cards[1]), expected)


if __name__ == '__main__':
    unittest.main()
