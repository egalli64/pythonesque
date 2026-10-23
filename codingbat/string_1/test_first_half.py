"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
first_half: https://codingbat.com/prob/p107010
"""
from first_half import first_half


class TestFirstHalf:
    def test_given_1(self):
        assert first_half("WooHoo") == "Woo"

    def test_given_2(self):
        assert first_half("HelloThere") == "Hello"

    def test_given_3(self):
        assert first_half("abcdef") == "abc"
