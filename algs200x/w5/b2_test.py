"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Primitive Calculator
"""
from b2_calculator_dp import solution


class TestSolution:
    def test_given_1(self):
        assert solution(1) == [1]

    def test_given_2(self):
        assert solution(5) in ([1, 3, 4, 5], [1, 2, 4, 5])

    def test_given_3(self):
        assert solution(96234) in ([1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038, 16039, 48117, 96234],
                                   [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234])

    def test_extra_1(self):
        assert solution(11) == [1, 3, 9, 10, 11]

    def test_extra_2(self):
        assert solution(98734) in (
            [1, 3, 9, 18, 19, 57, 114, 228, 456, 457, 1371, 2742, 5484, 5485, 16455, 32910, 32911, 98733, 98734],)
