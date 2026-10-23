"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 2: https://codingbat.com/python/String-2
cat_dog: https://codingbat.com/prob/p164876
"""
from cat_dog import cat_dog


class TestDoubleChar:
    def test_given_1(self):
        assert cat_dog("catdog") is True

    def test_given_2(self):
        assert cat_dog("catcat") is False

    def test_given_3(self):
        assert cat_dog("1cat1cadodog") is True
