"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
combo_string: https://codingbat.com/prob/p194053
"""
from combo_string import combo_string


class TestComboString:
    def test_given_1(self):
        assert combo_string("Hello", "hi") == "hiHellohi"

    def test_given_2(self):
        assert combo_string("hi", "Hello") == "hiHellohi"

    def test_given_3(self):
        assert combo_string("aaa", "b") == "baaab"
