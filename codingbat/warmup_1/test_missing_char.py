"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 1 https://codingbat.com/python/Warmup-1
missing_char https://codingbat.com/prob/p149524
"""
from missing_char import missing_char


class TestMissingChar:
    def test_given_1(self):
        assert missing_char("kitten", 1) == "ktten"

    def test_given_2(self):
        assert missing_char("kitten", 0) == "itten"

    def test_given_3(self):
        assert missing_char("kitten", 4) == "kittn"
