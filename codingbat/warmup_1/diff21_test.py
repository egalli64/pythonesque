"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
diff21 https://codingbat.com/prob/p197466
"""
import unittest
from diff21 import diff21, diff21_more_readable


class TestDiff21(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(diff21(19), 2)

    def test_given_2(self):
        self.assertEqual(diff21(10), 11)

    def test_given_3(self):
        self.assertEqual(diff21(21), 0)

    def test_given_readable_1(self):
        self.assertEqual(diff21_more_readable(19), 2)

    def test_given_readable_2(self):
        self.assertEqual(diff21_more_readable(10), 11)

    def test_given_readable_3(self):
        self.assertEqual(diff21_more_readable(21), 0)


if __name__ == "__main__":
    unittest.main()
