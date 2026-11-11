"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w1

Week 1 - Sum of Two Digits
"""

from a2_add import add


class TestAdd:
    def test_plain(self):
        assert add(4, 3) == 7

    def test_zero(self):
        assert add(0, 0) == 0

    def test_signed(self):
        assert add(4, -3) == 1

    def test_negative(self):
        assert add(-4, -3) == -7
