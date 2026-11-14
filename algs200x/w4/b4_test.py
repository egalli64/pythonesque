"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w4

Week 4 - Divide-and-Conquer: Majority Element
Boyer–Moore
"""
from b4_majority_bm import solution

TEST_DATA = list(range(8000000)) + [8000000] * 8000001


class TestSolution:
    def test_given_1(self):
        assert solution([2, 3, 9, 2, 2]) is True

    def test_given_2(self):
        assert solution([1, 2, 3, 4]) is False

    def test_given_3(self):
        assert solution([1, 2, 3, 1]) is False

    def test_extra_1(self):
        assert solution(TEST_DATA) is True

    def test_extra_2(self):
        with open("algs200x/w4/b_majority.in") as file:
            next(file)  # skip header
            data = [int(x) for x in next(file).split()]

        assert solution(data) is True
