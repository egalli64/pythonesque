"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
make_out_word: https://codingbat.com/prob/p129981
"""
from make_out_word import make_out_word


class TestMakeOutWord:
    def test_given_1(self):
        assert make_out_word("<<>>", "Yay") == "<<Yay>>"

    def test_given_2(self):
        assert make_out_word("<<>>", "WooHoo") == "<<WooHoo>>"

    def test_given_3(self):
        assert make_out_word("[[]]", "word") == "[[word]]"
