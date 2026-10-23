"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
make_abba: https://codingbat.com/prob/p182144
"""
from make_abba import make_abba


class TestMakeAbba:
    def test_given_1(self):
        assert make_abba("Hi", "Bye") == "HiByeByeHi"

    def test_given_2(self):
        assert make_abba("Yo", "Alice") == "YoAliceAliceYo"

    def test_given_3(self):
        assert make_abba("What", "Up") == "WhatUpUpWhat"
