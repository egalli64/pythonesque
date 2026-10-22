"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 1: https://codingbat.com/python/Logic-1
alarm_clock: https://codingbat.com/prob/p119867
"""
from alarm_clock import alarm_clock


class TestAlarmClock:
    """assuming pytest"""

    def test_given_1(self):
        assert alarm_clock(1, False) == "7:00"

    def test_given_2(self):
        assert alarm_clock(5, False) == "7:00"

    def test_given_3(self):
        assert alarm_clock(0, False) == "10:00"
