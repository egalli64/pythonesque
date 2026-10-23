"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 2: https://codingbat.com/python/String-2
end_other: https://codingbat.com/prob/p174314
"""
from end_other import end_other


class TestEndOther:
    def test_given_1(self):
        assert end_other("Hiabc", "abc") is True

    def test_given_2(self):
        assert end_other("AbC", "HiaBc") is True

    def test_given_3(self):
        assert end_other("abc", "abXabc") is True
