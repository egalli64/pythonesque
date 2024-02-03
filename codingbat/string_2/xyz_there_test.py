"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
xyz_there: https://codingbat.com/prob/p149391
"""

import unittest
from xyz_there import xyz_there, xyz_there_walrus


class TestXyzThere(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(xyz_there("abcxyz"), True)

    def test_given_2(self):
        self.assertEqual(xyz_there("abc.xyz"), False)

    def test_given_3(self):
        self.assertEqual(xyz_there("xyz.abc"), True)

    def test_empty(self):
        self.assertEqual(xyz_there(""), False)

    def test_good_the_second(self):
        self.assertEqual(xyz_there(".xyzxyz"), True)

    def test_walrus_given_1(self):
        self.assertEqual(xyz_there_walrus("abcxyz"), True)

    def test_walrus_given_2(self):
        self.assertEqual(xyz_there_walrus("abc.xyz"), False)

    def test_walrus_given_3(self):
        self.assertEqual(xyz_there_walrus("xyz.abc"), True)

    def test_walrus_empty(self):
        self.assertEqual(xyz_there_walrus(""), False)

    def test_walrus_good_the_second(self):
        self.assertEqual(xyz_there_walrus(".xyzxyz"), True)


if __name__ == "__main__":
    unittest.main()
