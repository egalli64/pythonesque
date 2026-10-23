"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
left2: https://codingbat.com/prob/p160545
"""
from left2 import left2


class TestLeft2:
    def test_given_1(self):
        assert left2("Hello") == "lloHe"

    def test_given_2(self):
        assert left2("java") == "vaja"

    def test_given_3(self):
        assert left2("Hi") == "Hi"
