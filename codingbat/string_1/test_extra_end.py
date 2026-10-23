"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
extra_end: https://codingbat.com/prob/p148853
"""
from extra_end import extra_end


class TestExtraEnd:
    def test_given_1(self):
        assert extra_end("Hello") == "lololo"

    def test_given_2(self):
        assert extra_end("ab") == "ababab"

    def test_given_3(self):
        assert extra_end("Hi") == "HiHiHi"
