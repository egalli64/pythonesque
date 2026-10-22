"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 1: https://codingbat.com/python/List-1
make_pi: https://codingbat.com/prob/p113659
"""
from make_pi import make_pi


class TestMakePi:
    """assuming pytest"""

    def test_given(self):
        assert make_pi() == [3, 1, 4]
