"""
CodingBat Python track: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
sleep_in https://codingbat.com/prob/p173401
"""
from sleep_in import sleep_in


class TestSleepIn:
    def test_given_1(self):
        assert sleep_in(False, False) is True

    def test_given_2(self):
        assert sleep_in(True, False) is False

    def test_given_3(self):
        assert sleep_in(False, True) is True
