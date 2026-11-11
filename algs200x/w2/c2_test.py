"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w2

Week 2 - Greater Common Divisor
"""
import math
from c2_gdc_euclid import gcd_iterative, gcd_recursive


class TestRecursiveSolution:
    def test_given_1(self):
        assert gcd_recursive(18, 35) == 1

    def test_given_2(self):
        assert gcd_recursive(28851538, 1183019) == 17657

    def test_given_3(self):
        assert gcd_recursive(1344, 217) == 7


class TestIterativeSolution:
    def test_given_1(self):
        assert gcd_iterative(18, 35) == 1

    def test_given_2(self):
        assert gcd_iterative(28851538, 1183019) == 17657

    def test_given_3(self):
        assert gcd_iterative(1344, 217) == 7


class TestBuiltinSolution:
    def test_given_1(self):
        assert math.gcd(18, 35) == 1

    def test_given_2(self):
        assert math.gcd(28851538, 1183019) == 17657

    def test_given_3(self):
        assert math.gcd(1344, 217) == 7
