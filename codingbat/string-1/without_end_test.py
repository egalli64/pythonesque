"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
without_end: https://codingbat.com/prob/p138533
"""
import unittest
from without_end import without_end


class TestWithoutEnd(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(without_end("Hello"), "ell")

    def test_given_2(self):
        self.assertEqual(without_end("java"), "av")

    def test_given_3(self):
        self.assertEqual(without_end("coding"), "odin")


if __name__ == "__main__":
    unittest.main()
