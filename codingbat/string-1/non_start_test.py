"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
non_start: https://codingbat.com/prob/p127703
"""
import unittest
from non_start import non_start


class TestNonStart(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(non_start("Hello", "There"), "ellohere")

    def test_given_2(self):
        self.assertEqual(non_start("java", "code"), "avaode")

    def test_given_3(self):
        self.assertEqual(non_start("shotl", "java"), "hotlava")


if __name__ == "__main__":
    unittest.main()
