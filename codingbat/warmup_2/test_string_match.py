"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 2 https://codingbat.com/python/Warmup-2
string_match https://codingbat.com/prob/p182414
"""
from string_match import string_match


class TestStringMatch:
    def test_given_1(self):
        assert string_match("xxcaazz", "xxbaaz") == 3

    def test_given_2(self):
        assert string_match("abc", "abc") == 2

    def test_given_3(self):
        assert string_match("abc", "axc") == 0
