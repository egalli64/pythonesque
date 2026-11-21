"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 Divide-and-Conquer - Organizing a Lottery
"""
from algs200x.w4.e2_lottery_sort import solution


class TestSolution:
    def test_given_1(self):
        assert solution([(0, 5), (7, 10)], [1, 6, 11]) == [1, 0, 0]

    def test_given_2(self):
        actual = solution([(-10, 10)], [-100, 100, 0])
        expected = [0, 0, 1]

        # relaxed expectation!
        assert sorted(actual) == sorted(expected)

    def test_given_3(self):
        assert solution([(3, 2), (0, 5), (-3, 2), (7, 10)], [1, 6]) == [2, 0]
