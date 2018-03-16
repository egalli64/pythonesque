"""
HackerRank Python Numpy Shape and Reshape

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-shape-reshape/problem
"""

import unittest
import numpy as np
from hr.numpy.shape_reshape import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertTrue(isinstance(result, np.ndarray))
        self.assertEqual(3, result.shape[0])
        self.assertEqual(3, result.shape[1])
        self.assertEqual(1, result[0][0])
        self.assertEqual(5, result[1][1])
        self.assertEqual(9, result[2][2])


if __name__ == '__main__':
    unittest.main()

