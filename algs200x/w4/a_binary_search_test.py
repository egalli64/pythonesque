"""
Binary Search

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""
import unittest

from algs200x.w4.a_binary_search import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        results = solution([1, 5, 8, 12, 13], [8, 1, 23, 1, 11])
        self.assertEqual(5, len(results))
        self.assertEqual(2, results[0])
        self.assertEqual(0, results[1])
        self.assertEqual(-1, results[2])
        self.assertEqual(0, results[3])
        self.assertEqual(-1, results[4])


if __name__ == '__main__':
    unittest.main()
