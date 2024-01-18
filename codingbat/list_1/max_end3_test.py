"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
max_end3: https://codingbat.com/prob/p135290
"""
import unittest
from max_end3 import max_end3, max_end3_new


class TestMaxEnd3(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(max_end3([1, 2, 3]), [3, 3, 3])

    def test_given_2(self):
        self.assertEqual(max_end3([11, 5, 9]), [11, 11, 11])

    def test_given_3(self):
        self.assertEqual(max_end3([2, 11, 3]), [3, 3, 3])

    def test_given_new_1(self):
        self.assertEqual(max_end3_new([1, 2, 3]), [3, 3, 3])

    def test_given_new_2(self):
        self.assertEqual(max_end3_new([11, 5, 9]), [11, 11, 11])

    def test_given_new_3(self):
        self.assertEqual(max_end3_new([2, 11, 3]), [3, 3, 3])


if __name__ == "__main__":
    unittest.main()
