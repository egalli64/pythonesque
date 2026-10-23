"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
non_start: https://codingbat.com/prob/p127703
"""
from non_start import non_start


class TestNonStart:
    def test_given_1(self):
        assert non_start("Hello", "There") == "ellohere"

    def test_given_2(self):
        assert non_start("java", "code") == "avaode"

    def test_given_3(self):
        assert non_start("shotl", "java") == "hotlava"
