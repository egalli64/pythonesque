"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
lone_sum: https://codingbat.com/prob/p143951
"""
import unittest
from lone_sum import lone_sum


class TestLoneSum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(lone_sum(1, 2, 3), 6)

    def test_given_2(self):
        self.assertEqual(lone_sum(3, 2, 3), 2)

    def test_given_3(self):
        self.assertEqual(lone_sum(3, 3, 3), 0)


if __name__ == "__main__":
    unittest.main()
