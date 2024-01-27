"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
count_hi: https://codingbat.com/prob/p167246
"""
import unittest
from count_hi import count_hi


class TestDoubleChar(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(count_hi("abc hi ho"), 1)

    def test_given_2(self):
        self.assertEqual(count_hi("ABChi hi"), 2)

    def test_given_3(self):
        self.assertEqual(count_hi("hihi"), 2)


if __name__ == "__main__":
    unittest.main()
