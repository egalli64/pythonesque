"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 2 https://codingbat.com/python/Warmup-2
front_times https://codingbat.com/prob/p165097
"""
from front_times import front_times


class TestFrontTimes:
    def test_given_1(self):
        assert front_times("Chocolate", 2) == "ChoCho"

    def test_given_2(self):
        assert front_times("Chocolate", 3) == "ChoChoCho"

    def test_given_3(self):
        assert front_times("Abc", 3) == "AbcAbcAbc"
