"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - Least Common Multiple
Naive
"""
from d1_lcm_naive import lcm_naive


class TestSolution:
    def test_given_1(self):
        assert lcm_naive(6, 8) == 24

    def test_extra_1(self):
        assert lcm_naive(4999, 5007) == 4999 * 5007
