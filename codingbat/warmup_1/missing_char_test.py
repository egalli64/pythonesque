"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 1 https://codingbat.com/python/Warmup-1
missing_char https://codingbat.com/prob/p149524
"""
import unittest
from missing_char import missing_char


class TestMissingChar(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(missing_char("kitten", 1), "ktten")

    def test_given_2(self):
        self.assertEqual(missing_char("kitten", 0), "itten")

    def test_given_3(self):
        self.assertEqual(missing_char("kitten", 4), "kittn")


if __name__ == "__main__":
    unittest.main()
