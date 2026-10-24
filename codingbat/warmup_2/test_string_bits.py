"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Warmup 2 https://codingbat.com/python/Warmup-2
string_bits https://codingbat.com/prob/p113152
"""
from string_bits import string_bits


class TestStringBits:
    def test_given_1(self):
        assert string_bits("Hello") == "Hlo"

    def test_given_2(self):
        assert string_bits("Hi") == "H"

    def test_given_3(self):
        assert string_bits("Heeololeo") == "Hello"
