"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
caught_speeding: https://codingbat.com/prob/p137202
"""
import unittest
from caught_speeding import caught_speeding


class TestCaughtSpeeding(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(caught_speeding(60, False), 0)

    def test_given_2(self):
        self.assertEqual(caught_speeding(65, False), 1)

    def test_given_3(self):
        self.assertEqual(caught_speeding(65, True), 0)


if __name__ == "__main__":
    unittest.main()
