"""
Extra exercise: 2-partition problem
https://github.com/egalli64/pythonesque folder algs200x/w6
"""
from f_2_partition import solution


class TestSolution:
    def test_1(self):
        assert solution([1, 5, 11, 5]) is True

    def test_2(self):
        assert solution([1, 5, 3]) is False

    def test_3(self):
        assert solution([1, 3, 11, 5]) is False

    def test_4(self):
        assert solution([3, 1, 1, 2, 2, 1]) is True

    def test_5(self):
        assert solution([7, 5, 3, 5]) is True
