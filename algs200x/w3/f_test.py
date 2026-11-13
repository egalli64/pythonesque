"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Maximizing Your Salary
"""
from f_salary import solution


class TestSolution:
    def test_given_1(self):
        assert solution(['21', '2']) == '221'

    def test_given_2(self):
        assert solution(['9', '4', '6', '1', '9']) == '99641'

    def test_given_3(self):
        assert solution(['23', '39', '92']) == '923923'

    def test_extra(self):
        with open("algs200x/w3/f_salary.in") as file:
            next(file)  # skip header
            data = next(file).split()

        xs = solution(data)
        assert len(xs) == 290
        assert xs.startswith('9983975967')
        assert xs.endswith('8140123101')
