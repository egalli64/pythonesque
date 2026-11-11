"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Last Digit of the Partial Sum of n Fibonacci Numbers
"""
from g_fibonacci_sum import solution


class TestSolution:
    def test_given_1(self):
        assert solution(3, 7) == 1

    def test_given_2(self):
        assert solution(10, 10) == 5

    def test_given_3(self):
        assert solution(10, 200) == 2

    def test_extra_1(self):
        assert solution(57, 123) == 6

    def test_extra_2(self):
        assert solution(1, 100000000) == 5
