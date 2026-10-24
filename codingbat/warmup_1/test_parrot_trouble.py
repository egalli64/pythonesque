"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
parrot_trouble https://codingbat.com/prob/p166884
"""
from parrot_trouble import parrot_trouble


class TestParrotTrouble:
    def test_given_1(self):
        assert parrot_trouble(True, 6) is True

    def test_given_2(self):
        assert parrot_trouble(True, 7) is False

    def test_given_3(self):
        assert parrot_trouble(False, 6) is False
