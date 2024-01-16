"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Warmup 2 https://codingbat.com/python/Warmup-2
last2 https://codingbat.com/prob/p145834
"""
import unittest
from last2 import last2, last2_walrus


class TestLast2(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(last2("hixxhi"), 1)

    def test_given_2(self):
        self.assertEqual(last2("xaxxaxaxx"), 1)

    def test_given_3(self):
        self.assertEqual(last2("axxxaaxx"), 2)

    def test_given_walrus_1(self):
        self.assertEqual(last2_walrus("hixxhi"), 1)

    def test_given_walrus_2(self):
        self.assertEqual(last2_walrus("xaxxaxaxx"), 1)

    def test_given_walrus_3(self):
        self.assertEqual(last2_walrus("axxxaaxx"), 2)


if __name__ == "__main__":
    unittest.main()
