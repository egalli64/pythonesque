"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
middle_way: https://codingbat.com/prob/p171011
"""
import unittest
from middle_way import middle_way


class TestMiddleWay(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(middle_way([1, 2, 3], [4, 5, 6]), [2, 5])

    def test_given_2(self):
        self.assertEqual(middle_way([7, 7, 7], [3, 8, 0]), [7, 8])

    def test_given_3(self):
        self.assertEqual(middle_way([5, 2, 9], [1, 4, 5]), [2, 4])


if __name__ == "__main__":
    unittest.main()
