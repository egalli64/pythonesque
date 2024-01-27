"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
make_chocolate: https://codingbat.com/prob/p190859
"""
import unittest
from make_chocolate import make_chocolate


class TestMakeChocolate(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(make_chocolate(4, 1, 9), 4)

    def test_given_2(self):
        self.assertEqual(make_chocolate(4, 1, 10), -1)

    def test_given_3(self):
        self.assertEqual(make_chocolate(4, 1, 7), 2)


if __name__ == "__main__":
    unittest.main()
