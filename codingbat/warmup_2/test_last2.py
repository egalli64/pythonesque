"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 2 https://codingbat.com/python/Warmup-2
last2 https://codingbat.com/prob/p145834
"""
from last2 import last2, last2_walrus


class TestLast2:
    def test_given_1(self):
        assert last2("hixxhi") == 1

    def test_given_2(self):
        assert last2("xaxxaxaxx") == 1

    def test_given_3(self):
        assert last2("axxxaaxx") == 2

    def test_given_walrus_1(self):
        assert last2_walrus("hixxhi") == 1

    def test_given_walrus_2(self):
        assert last2_walrus("xaxxaxaxx") == 1

    def test_given_walrus_3(self):
        assert last2_walrus("axxxaaxx") == 2
