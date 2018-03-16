"""
HackerRank Python Numpy Arrays

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/np-arrays/problem
"""

import unittest
import numpy as np
from hr.numpy.arrays import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        result = solution([1, 2, 3, 4, -8, -10])
        self.assertTrue(isinstance(result, np.ndarray))
        self.assertEqual(np.float64, result.dtype)
        self.assertEqual(-10, result[0])
        self.assertEqual(1, result[-1])


if __name__ == '__main__':
    unittest.main()

