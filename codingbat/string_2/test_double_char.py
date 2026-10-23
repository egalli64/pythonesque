"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 2: https://codingbat.com/python/String-2
double_char: https://codingbat.com/prob/p170842
"""
from double_char import double_char


class TestDoubleChar:
    def test_given_1(self):
        assert double_char("The") == "TThhee"

    def test_given_2(self):
        assert double_char("AAbb") == "AAAAbbbb"

    def test_given_3(self):
        assert double_char("Hi-There") == "HHii--TThheerree"
