"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

Logic 1: https://codingbat.com/python/Logic-1
alarm_clock: https://codingbat.com/prob/p119867
"""
import unittest
from alarm_clock import alarm_clock


class TestAlarmClock(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(alarm_clock(1, False), "7:00")

    def test_given_2(self):
        self.assertEqual(alarm_clock(5, False), "7:00")

    def test_given_3(self):
        self.assertEqual(alarm_clock(0, False), "10:00")


if __name__ == "__main__":
    unittest.main()
