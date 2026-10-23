"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
without_end: https://codingbat.com/prob/p138533
"""
from without_end import without_end


class TestWithoutEnd:
    def test_given_1(self):
        assert without_end("Hello") == "ell"

    def test_given_2(self):
        assert without_end("java") == "av"

    def test_given_3(self):
        assert without_end("coding") == "odin"
