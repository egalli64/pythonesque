"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w5

Week 5 - Dynamic Programming /1: Primitive Calculator
"""
from b1_calculator_greedy import solution


class TestSolution:
    def test_given_1(self):
        assert solution(1) == [1]

    def test_given_2(self):
        assert solution(5) in ([1, 3, 4, 5], [1, 2, 4, 5])

    def test_given_3(self):
        """This test is expected to fail, since a greedy approach won't work here"""
        # actual solution is [1, 2, 4, 5, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]
        assert solution(96234) in ([1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038, 16039, 48117, 96234],
                                   [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234])
