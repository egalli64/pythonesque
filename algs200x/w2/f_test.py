"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Last Digit of the Sum of the first n Fibonacci Numbers
"""
from f_fibonacci_sum import solution


class TestSolution:
    def test_given_1(self):
        assert solution(3) == 4

    def test_given_2(self):
        assert solution(100) == 5

    def test_extra_1(self):
        assert solution(832564823476) == 3

    def test_extra_2(self):
        assert solution(614162383528) == 9
