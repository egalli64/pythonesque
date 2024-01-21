"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
love6: https://codingbat.com/prob/p100958
"""
import unittest
from love6 import love6


class TestLove6(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(love6(6, 4), True)

    def test_given_2(self):
        self.assertEqual(love6(4, 5), False)

    def test_given_3(self):
        self.assertEqual(love6(1, 5), True)


if __name__ == "__main__":
    unittest.main()
