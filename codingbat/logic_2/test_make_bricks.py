"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

Logic 2: https://codingbat.com/python/Logic-2
make_bricks: https://codingbat.com/prob/p118406
"""
from make_bricks import make_bricks


class TestMakeBricks:
    def test_given_1(self):
        assert make_bricks(3, 1, 8) == True

    def test_given_2(self):
        assert make_bricks(3, 1, 9) == False

    def test_given_3(self):
        assert make_bricks(3, 2, 10) == True
