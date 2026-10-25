"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
centered_average: https://codingbat.com/prob/p126968
"""
from centered_average import centered_average


class TestCenteredAverage:
    def test_given_1(self):
        assert centered_average([1, 2, 3, 4, 100]) == 3

    def test_given_2(self):
        assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5

    def test_given_3(self):
        assert centered_average([-10, -4, -2, -4, -2, 0]) == -3
