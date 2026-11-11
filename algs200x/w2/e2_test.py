"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Fibonacci modulo m
Smarter solution by Pisano
"""
from e2_fibonacci_modulo import solution


class TestSolution:
    def test_given_1(self):
        assert solution(239, 1000) == 161

    def test_given_2(self):
        assert solution(2816213588, 30524) == 10249

    def test_extra(self):
        assert solution(400000, 1000) == 875
