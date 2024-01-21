"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
near_ten: https://codingbat.com/prob/p165321
"""
import unittest
from near_ten import near_ten


class TestNearTen(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(near_ten(12), True)

    def test_given_2(self):
        self.assertEqual(near_ten(17), False)

    def test_given_3(self):
        self.assertEqual(near_ten(19), True)


if __name__ == "__main__":
    unittest.main()
