"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
extra_end: https://codingbat.com/prob/p148853
"""
import unittest
from extra_end import extra_end


class TestExtraEnd(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(extra_end("Hello"), "lololo")

    def test_given_2(self):
        self.assertEqual(extra_end("ab"), "ababab")

    def test_given_3(self):
        self.assertEqual(extra_end("Hi"), "HiHiHi")


if __name__ == "__main__":
    unittest.main()
