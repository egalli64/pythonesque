"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
front_times https://codingbat.com/prob/p165097
"""
import unittest
from front_times import front_times


class TestFrontTimes(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(front_times("Chocolate", 2), "ChoCho")

    def test_given_2(self):
        self.assertEqual(front_times("Chocolate", 3), "ChoChoCho")

    def test_given_3(self):
        self.assertEqual(front_times("Abc", 3), "AbcAbcAbc")


if __name__ == "__main__":
    unittest.main()
