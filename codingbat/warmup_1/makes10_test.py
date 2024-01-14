"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
makes10 https://codingbat.com/prob/p124984
"""
import unittest
from makes10 import makes10


class TestMakes10(unittest.TestCase):
    def test_given_1(self):
        self.assertTrue(makes10(9, 10))

    def test_given_2(self):
        self.assertFalse(makes10(9, 9))

    def test_given_3(self):
        self.assertTrue(makes10(1, 9))


if __name__ == "__main__":
    unittest.main()
