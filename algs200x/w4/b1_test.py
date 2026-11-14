"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Divide-and-Conquer: Majority Element
Naive Algorithm
"""
from b1_majority_naive import solution

TEST_DATA = list(range(4000)) + [4000] * 20001


class TestSolution:

    def test_given_1(self):
        assert solution([2, 3, 9, 2, 2]) is True

    def test_given_2(self):
        assert solution([1, 2, 3, 4]) is False

    def test_given_3(self):
        assert solution([1, 2, 3, 1]) is False

    def test_extra(self):
        assert solution(TEST_DATA) is True
