"""
2 way partition

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/2-partition-problem.html
"""
import unittest

from algs200x.w6.f_2_partition import solution


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertTrue(solution([1, 5, 11, 5]))

    def test_2(self):
        self.assertFalse(solution([1, 5, 3]))

    def test_3(self):
        self.assertFalse(solution([1, 3, 11, 5]))

    def test_4(self):
        self.assertTrue(solution([3, 1, 1, 2, 2, 1]))

    def test_5(self):
        self.assertTrue(solution([7, 5, 3, 5]))


if __name__ == '__main__':
    unittest.main()
