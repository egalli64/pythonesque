"""
Majority Element

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      http://thisthread.blogspot.com/2018/02/majority-element.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""
import unittest

from algs200x.w4.b_majority import solution_naive, solution_sort, solution_hash, solution_dac, solution_bm


class TestSolution(unittest.TestCase):
    slow_1 = [2] * 2000 + [1] * 2001
    slow_2 = [1] * 100000 + [2] * 100001
    slow_3 = [1] * 4000000 + [2] * 4000001

    def test_naive_1(self):
        self.assertEqual(1, solution_naive([2, 3, 9, 2, 2]))

    def test_naive_2(self):
        self.assertEqual(0, solution_naive([1, 2, 3, 4]))

    def test_naive_3(self):
        self.assertEqual(0, solution_naive([1, 2, 3, 1]))

    def test_naive_slow_1(self):
        self.assertEqual(1, solution_naive(self.slow_1))

    def test_dac_1(self):
        self.assertEqual(1, solution_dac([2, 3, 9, 2, 2]))

    def test_dac_2(self):
        self.assertEqual(0, solution_dac([1, 2, 3, 4]))

    def test_dac_3(self):
        self.assertEqual(0, solution_dac([1, 2, 3, 1]))

    def test_dac_x(self):
        self.assertEqual(0, solution_dac([1, 2] * 3))

    def test_dac_x2(self):
        self.assertEqual(1, solution_dac([1, 2] * 3 + [1]))

    def test_dac_x3(self):
        self.assertEqual(1, solution_dac([1, 2] * 3 + [2]))

    def test_dac_slow_1(self):
        self.assertEqual(1, solution_dac(self.slow_1))

    def test_dac_slow_2(self):
        self.assertEqual(1, solution_dac(self.slow_2))

    def test_sort_1(self):
        self.assertEqual(1, solution_sort([2, 3, 9, 2, 2]))

    def test_sort_1a(self):
        self.assertEqual(1, solution_sort([9, 3, 9, 9, 2]))

    def test_sort_2(self):
        self.assertEqual(0, solution_sort([1, 2, 3, 4]))

    def test_sort_3(self):
        self.assertEqual(0, solution_sort([1, 2, 3, 1]))

    def test_sort_slow_1(self):
        self.assertEqual(1, solution_sort(self.slow_1))

    def test_sort_slow_2(self):
        self.assertEqual(1, solution_sort(self.slow_2))

    def test_sort_slow_3(self):
        self.assertEqual(1, solution_sort(self.slow_3))

    def test_hash_1(self):
        self.assertEqual(1, solution_hash([2, 3, 9, 2, 2]))

    def test_hash_2(self):
        self.assertEqual(0, solution_hash([1, 2, 3, 4]))

    def test_hash_3(self):
        self.assertEqual(0, solution_hash([1, 2, 3, 1]))

    def test_hash_slow_2(self):
        self.assertEqual(1, solution_hash(self.slow_2))

    def test_hash_slow_3(self):
        self.assertEqual(1, solution_hash(self.slow_3))

    def test_bm_1(self):
        self.assertEqual(1, solution_bm([2, 3, 9, 2, 2]))

    def test_bm_2(self):
        self.assertEqual(0, solution_bm([1, 2, 3, 4]))

    def test_bm_3(self):
        self.assertEqual(0, solution_bm([1, 2, 3, 1]))

    def test_bm_slow_2(self):
        self.assertEqual(1, solution_bm(self.slow_2))


if __name__ == '__main__':
    unittest.main()
