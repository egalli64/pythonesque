"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques

Week 2 - Least Common Multiple
"""
import math
from d2_lcm_euclid import lcm


class TestSolution:
    def test_given_1(self):
        assert lcm(6, 8) == 24

    def test_extra_1(self):
        assert lcm(4999, 5007) == 4999 * 5007

    def test_given_2(self):
        assert lcm(28851538, 1183019) == 1933053046


class TestBuiltinSolution:
    def test_given_1(self):
        assert math.lcm(6, 8) == 24

    def test_extra_1(self):
        assert math.lcm(4999, 5007) == 4999 * 5007

    def test_given_2(self):
        assert math.lcm(28851538, 1183019) == 1933053046
