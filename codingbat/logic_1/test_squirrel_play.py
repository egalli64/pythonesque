"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 1: https://codingbat.com/python/Logic-1
squirrel_play: https://codingbat.com/prob/p135815
"""
from squirrel_play import squirrel_play


class TestSquirrelPlay:
    def test_given_1(self):
        assert squirrel_play(70, False) is True

    def test_given_2(self):
        assert squirrel_play(95, False) is False

    def test_given_3(self):
        assert squirrel_play(95, True) is True
