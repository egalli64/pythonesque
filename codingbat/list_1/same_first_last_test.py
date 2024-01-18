"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

List 1: https://codingbat.com/python/List-1
same_first_last: https://codingbat.com/prob/p179078
"""
import unittest
from same_first_last import same_first_last


class TestSameFirstLast(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(same_first_last([1, 2, 3]), False)

    def test_given_2(self):
        self.assertEqual(same_first_last([1, 2, 3, 1]), True)

    def test_given_3(self):
        self.assertEqual(same_first_last([1, 2, 1]), True)

    def test_empty(self):
        self.assertFalse(same_first_last([]))

    def test_empty_unusually_picky(self):
        """CodingBat extra requirement, falsy is not enough"""
        actual = same_first_last([])
        self.assertIsInstance(actual, bool)
        self.assertFalse(actual)


if __name__ == "__main__":
    unittest.main()
