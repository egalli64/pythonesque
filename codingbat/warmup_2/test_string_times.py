"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 2 https://codingbat.com/python/Warmup-2
string_times https://codingbat.com/prob/p193507
"""
from string_times import string_times


class TestStringTimes:
    def test_given_1(self):
        assert string_times("Hi", 2) == "HiHi"

    def test_given_2(self):
        assert string_times("Hi", 3) == "HiHiHi"

    def test_given_3(self):
        assert string_times("Hi", 1) == "Hi"
