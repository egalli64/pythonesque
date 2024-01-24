"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
make_bricks: https://codingbat.com/prob/p118406
"""
import unittest
from make_bricks import make_bricks


class TestNearTen(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(make_bricks(3, 1, 8), True)

    def test_given_2(self):
        self.assertEqual(make_bricks(3, 1, 9), False)

    def test_given_3(self):
        self.assertEqual(make_bricks(3, 2, 10), True)


if __name__ == "__main__":
    unittest.main()
