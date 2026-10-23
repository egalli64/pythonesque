"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 2: https://codingbat.com/python/String-2
count_hi: https://codingbat.com/prob/p167246
"""
from count_hi import count_hi


class TestDoubleChar:
    def test_given_1(self):
        assert count_hi("abc hi ho") == 1

    def test_given_2(self):
        assert count_hi("ABChi hi") == 2

    def test_given_3(self):
        assert count_hi("hihi") == 2
