"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
front3 https://codingbat.com/prob/p147920
"""
from front3 import front3


class TestFront3:
    def test_given_1(self):
        assert front3("Java") == "JavJavJav"

    def test_given_2(self):
        assert front3("Chocolate") == "ChoChoCho"

    def test_given_3(self):
        assert front3("abc") == "abcabcabc"

    def test_short(self):
        assert front3("a") == "aaa"
