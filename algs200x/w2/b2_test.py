"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Fibonacci last digit
"""
from b2_fibonacci_last_digit import get_fibonacci_last_digit


class TestSolution:
    def test_given_1(self):
        assert get_fibonacci_last_digit(200) == 5

    def test_given_2(self):
        assert get_fibonacci_last_digit(331) == 9

    def test_given_3(self):
        assert get_fibonacci_last_digit(327305) == 5