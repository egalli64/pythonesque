"""
Organizing a Lottery

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""
import unittest

from algs200x.w4.e_lottery import solution_naive, solution_sort


class TestSolution(unittest.TestCase):
    def test_naive_1(self):
        results = solution_naive([(0, 5), (7, 10)], [1, 6, 11])
        self.assertEqual(3, len(results))
        self.assertEqual(1, sum(results))

    def test_naive_2(self):
        results = solution_naive([(-10, 10)], [-100, 100, 0])
        self.assertEqual(3, len(results))
        self.assertEqual(1, sum(results))

    def test_naive_3(self):
        results = solution_naive([(3, 2), (0, 5), (-3, 2), (7, 10)], [1, 6])
        self.assertEqual(2, len(results))
        self.assertEqual(2, sum(results))

    def test_sort_1(self):
        results = solution_sort([(0, 5), (7, 10)], [1, 6, 11])
        self.assertEqual(3, len(results))
        self.assertEqual(1, sum(results))

    def test_sort_2(self):
        results = solution_sort([(-10, 10)], [-100, 100, 0])
        self.assertEqual(3, len(results))
        self.assertEqual(1, sum(results))

    def test_sort_3(self):
        results = solution_sort([(3, 2), (0, 5), (-3, 2), (7, 10)], [1, 6])
        self.assertEqual(2, len(results))
        self.assertEqual(2, sum(results))


if __name__ == '__main__':
    unittest.main()
