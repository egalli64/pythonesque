"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - Greater Common Divisor
Naive
"""
from c1_gdc_naive import gcd_naive


class TestSolution:
    def test_given_1(self):
        assert gcd_naive(18, 35) == 1

    def test_given_2(self):
        assert gcd_naive(28851538, 1183019) == 17657

    def test_given_3(self):
        assert gcd_naive(1344, 217) == 7
