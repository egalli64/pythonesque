"""
Extra exercise: 0/1 knapsack
https://github.com/egalli64/pythonesque folder algs200x/w6
"""
from e_01_knapsack import solution


class TestSolution:
    def test_1(self):
        assert solution(7, [1, 3, 4, 5], [1, 4, 5, 7]) == 9

    def test_2(self):
        assert solution(50, [10, 20, 30], [60, 100, 120]) == 220

    def test_3(self):
        assert solution(10, [8, 1, 3], [8, 1, 3]) == 9
