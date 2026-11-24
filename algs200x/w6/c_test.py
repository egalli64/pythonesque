"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w6

Week 6 - Dynamic Programming /2: Maximizing the Value of an Arithmetic Expression
"""
import pytest

from c_max_expr import solution


class TestSolution:
    def test_given_1(self):
        assert solution([1, 5], ['+']) == 6

    def test_given_2(self):
        assert solution([5, 8, 7, 4, 8, 9], ['-', '+', '*', '-', '+']) == 200

    def test_quiz(self):
        assert solution([7, 6, 3, 2, 7, 4, 2, 4, 2, 9, 6, 8],
                        ['+', '+', '-', '-', '-', '*', '+', '+', '-', '*', '*']) == 9168

    def test_wrong_operation(self):
        with pytest.raises(KeyError):
            solution([1, 5], ['^'])
