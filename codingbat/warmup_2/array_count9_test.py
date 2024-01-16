"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
array_count9 https://codingbat.com/prob/p166170
"""
import unittest
from array_count9 import array_count9, array_count9_loop


class TestStringBits(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(array_count9([1, 2, 9]), 1)

    def test_given_2(self):
        self.assertEqual(array_count9([1, 9, 9]), 2)

    def test_given_3(self):
        self.assertEqual(array_count9([1, 9, 9, 3, 9]), 3)

    def test_given_1_loop(self):
        self.assertEqual(array_count9_loop([1, 2, 9]), 1)

    def test_given_2_loop(self):
        self.assertEqual(array_count9_loop([1, 9, 9]), 2)

    def test_given_3_loop(self):
        self.assertEqual(array_count9_loop([1, 9, 9, 3, 9]), 3)


if __name__ == "__main__":
    unittest.main()
