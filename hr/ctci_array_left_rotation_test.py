"""
HackerRank Tutorials  Cracking the Coding Interview  Arrays: Left Rotation
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-arrays-left-rotation.html
      https://www.hackerrank.com/challenges/ctci-array-left-rotation
"""

import unittest
from hr.ctci_array_left_rotation import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual([5, 1, 2, 3, 4], solution([1, 2, 3, 4, 5], 5, 4))

if __name__ == '__main__':
    unittest.main()
