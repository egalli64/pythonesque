"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Fibonacci last digit
Naive last digit of a Fibonacci number calculator
"""
from b1_fibonacci_last_digit import get_fibonacci_last_digit_naive


class TestSolution:
    def test_given(self):
        assert get_fibonacci_last_digit_naive(200) == 5
