"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
sum2: https://codingbat.com/prob/p192589
"""
import unittest
from sum2 import sum2


class TestSum2(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(sum2([1, 2, 3]), 3)

    def test_given_2(self):
        self.assertEqual(sum2([1, 1]), 2)

    def test_given_3(self):
        self.assertEqual(sum2([1, 1, 1, 1]), 2)


if __name__ == "__main__":
    unittest.main()
