"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
in1to10: https://codingbat.com/prob/p158497
"""
import unittest
from in1to10 import in1to10


class TestIn1to10(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(in1to10(5, False), True)

    def test_given_2(self):
        self.assertEqual(in1to10(11, False), False)

    def test_given_3(self):
        self.assertEqual(in1to10(11, True), True)


if __name__ == "__main__":
    unittest.main()
