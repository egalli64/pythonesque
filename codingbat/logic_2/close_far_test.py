"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 2: https://codingbat.com/python/Logic-2
close_far: https://codingbat.com/prob/p160533
"""
import unittest
from close_far import close_far


class TestCloseFar(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(close_far(1, 2, 10), True)

    def test_given_2(self):
        self.assertEqual(close_far(1, 2, 3), False)

    def test_given_3(self):
        self.assertEqual(close_far(4, 1, 3), True)


if __name__ == "__main__":
    unittest.main()
