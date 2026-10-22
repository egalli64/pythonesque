"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
sum2: https://codingbat.com/prob/p192589
"""
from sum2 import sum2


class TestSum2:
    """assuming pytest"""

    def test_given_1(self):
        assert sum2([1, 2, 3]) == 3

    def test_given_2(self):
        assert sum2([1, 1]) == 2

    def test_given_3(self):
        assert sum2([1, 1, 1, 1]) == 2
