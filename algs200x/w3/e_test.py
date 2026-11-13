"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w3

Week 3 - greedy algorithms: Maximizing the Number of Prize Places in a Competition
"""
from e_prizes import solution


class TestSolution:
    def test_given_1(self):
        elements = solution(6)
        assert len(elements) == 3
        assert elements[0] == 1
        assert elements[1] == 2
        assert elements[2] == 3

    def test_given_2(self):
        elements = solution(8)
        assert len(elements) == 3
        assert elements[0] == 1
        assert elements[1] == 2
        assert elements[2] == 5

    def test_given_3(self):
        elements = solution(2)
        assert len(elements) == 1
        assert elements[0] == 2

    def test_extra(self):
        elements = solution(182414564)
        assert len(elements) == 19100
        assert elements[-1] == 19114
