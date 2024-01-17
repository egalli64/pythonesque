"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
first_two: https://codingbat.com/prob/p184816
"""
import unittest
from first_two import first_two


class TestFirstTwo(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(first_two('Hello'), 'He')

    def test_given_2(self):
        self.assertEqual(first_two('abcdefg'), 'ab')

    def test_given_3(self):
        self.assertEqual(first_two('ab'), 'ab')


if __name__ == "__main__":
    unittest.main()
