"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
parrot_trouble https://codingbat.com/prob/p166884
"""
import unittest
from parrot_trouble import parrot_trouble


class TestSleepIn(unittest.TestCase):
    def test_given_1(self):
        self.assertTrue(parrot_trouble(True, 6))

    def test_given_2(self):
        self.assertFalse(parrot_trouble(True, 7))

    def test_given_3(self):
        self.assertFalse(parrot_trouble(False, 6))


if __name__ == "__main__":
    unittest.main()
