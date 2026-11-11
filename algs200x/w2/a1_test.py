"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Fibonacci
A naive Fibonacci calculator - make some sort of sense only for very low input
Do not expect an input greater than 45
"""
from a1_fibonacci_naive import calc_fib

class TestSolution:
    def test_given(self):
        assert calc_fib(10) == 55
