"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 2 https://codingbat.com/python/Warmup-2
string_splosion https://codingbat.com/prob/p118366
"""
from string_splosion import string_splosion


class TestStringSplosion:
    def test_given_1(self):
        assert string_splosion("Code") == "CCoCodCode"

    def test_given_2(self):
        assert string_splosion("abc") == "aababc"

    def test_given_3(self):
        assert string_splosion("ab") == "aab"
