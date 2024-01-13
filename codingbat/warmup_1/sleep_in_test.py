"""
CodingBat Python track: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
sleep_in https://codingbat.com/prob/p173401
"""
import unittest
from sleep_in import sleep_in


class TestSleepIn(unittest.TestCase):
    def test_given_1(self):
        self.assertTrue(sleep_in(False, False))

    def test_given_2(self):
        self.assertFalse(sleep_in(True, False))

    def test_given_3(self):
        self.assertTrue(sleep_in(False, True))

if __name__ == "__main__":
    unittest.main()
