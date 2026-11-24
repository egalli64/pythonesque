"""
edX UCSanDiegoX - Algorithmic Design and Techniques
https://www.edx.org/learn/algorithms/the-university-of-california-san-diego-algorithmic-design-and-techniques
My notes: https://github.com/egalli64/pythonesque folder algs200x/w6

Week 6 - Dynamic Programming /2: Partitioning Souvenirs
"""
from b1_souvenirs import solution


class TestSolution:
    def test_given_1(self):
        assert solution([3, 3, 3, 3]) is False

    def test_given_2(self):
        assert solution([40]) is False

    def test_given_3(self):
        assert solution([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]) is True

    def test_given_4(self):
        assert solution([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]) is True

    def test_extra_1(self):
        assert solution([1, 2, 1, 2]) is True

    def test_extra_2(self):
        assert solution([6, 6, 3]) is False

    def test_extra_3(self):
        assert solution([3, 1, 1, 2, 2]) is True

    def test_more_1(self):
        assert solution([1, 1, 1]) is True

    def test_more_2(self):
        assert solution([3, 3, 3, 3]) is False

    def test_more_3(self):
        assert solution([4, 1, 3, 2]) is False

    def test_more_4(self):
        assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) is False

    def test_more_5(self):
        assert solution([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]) is True

    def test_more_6(self):
        assert solution([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]) is True

    def test_more_7(self):
        assert solution([19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]) is True

    def test_more_8(self):
        assert solution([1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1]) is False

    def test_more_9(self):
        assert solution([1, 2, 2, 2, 1, 3, 3, 3, 2, 2, 3, 2, 1, 2, 3, 3, 2, 2]) is True

    def test_more_10(self):
        assert solution([6, 7, 8, 5, 11, 3, 1, 19, 16, 19, 5, 7, 13, 10, 16, 4, 15, 16]) is False

    def test_more_11(self):
        assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]) is True

    def test_shuai(self):
        assert solution([7, 2, 2, 2, 2, 2, 2, 2, 3]) is False

    def test_confounding_choice(self):
        assert solution([3, 2, 2, 2, 3]) is False

    def test_duplicates(self):
        assert solution([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) is True
