"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

String 1: https://codingbat.com/python/String-1
first_two: https://codingbat.com/prob/p184816
"""
from first_two import first_two


class TestFirstTwo:
    def test_given_1(self):
        assert first_two('Hello') == 'He'

    def test_given_2(self):
        assert first_two('abcdefg') == 'ab'

    def test_given_3(self):
        assert first_two('ab') == 'ab'
