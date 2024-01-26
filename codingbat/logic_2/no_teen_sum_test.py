"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
no_teen_sum: https://codingbat.com/prob/p100347
"""
import unittest
from no_teen_sum import no_teen_sum


class TestNoTeenSum(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(no_teen_sum(1, 2, 3), 6)

    def test_given_2(self):
        self.assertEqual(no_teen_sum(2, 13, 1), 3)

    def test_given_3(self):
        self.assertEqual(no_teen_sum(2, 1, 14), 3)


if __name__ == "__main__":
    unittest.main()
