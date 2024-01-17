"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
make_abba: https://codingbat.com/prob/p182144
"""
import unittest
from make_abba import make_abba


class TestMakeAbba(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(make_abba("Hi", "Bye"), "HiByeByeHi")

    def test_given_2(self):
        self.assertEqual(make_abba("Yo", "Alice"), "YoAliceAliceYo")

    def test_given_3(self):
        self.assertEqual(make_abba("What", "Up"), "WhatUpUpWhat")


if __name__ == "__main__":
    unittest.main()
