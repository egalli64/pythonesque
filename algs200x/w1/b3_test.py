"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w1

Week 1 - Maximum Pairwise Product
Find the maximum product of two distinct numbers in a sequence of non-negative integers.
"""
import pytest

from b3_max_pair_sort import max_pair


class TestMaxPairSort:
    def test_given_1(self):
        assert max_pair([1, 2, 3]) == 6

    def test_given_2(self):
        values = [int(x) for x in "7 5 14 2 8 8 10 1 2 3".split()]
        assert max_pair(values) == 140

    def test_bad(self):
        with pytest.raises(AssertionError):
            max_pair([1])
