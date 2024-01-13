"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
monkey_trouble https://codingbat.com/prob/p120546
"""
import unittest
from monkey_trouble import monkey_trouble


class TestMonkeyTrouble(unittest.TestCase):
    def test_given_1(self):
        self.assertTrue(monkey_trouble(True, True))

    def test_given_2(self):
        self.assertTrue(monkey_trouble(False, False))

    def test_given_3(self):
        self.assertFalse(monkey_trouble(True, False))


if __name__ == "__main__":
    unittest.main()
