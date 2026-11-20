"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Number of Inversions
"""
from d1_inversions_naive import solution

INPUT_TEST_4000 = [x for x in range(4000)] + [1]


class TestSolution:
    def test_given(self):
        assert solution([2, 3, 9, 2, 9]) == 2

    def test_4000(self):
        assert solution(INPUT_TEST_4000) == 3998
