"""
Tutorials  Cracking the Coding Interview  Heaps: Find the Running Median
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-heaps-find-running-median.html
      https://www.hackerrank.com/challenges/ctci-find-the-running-median
"""

import unittest

from hr.ctci.find_the_running_median import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('12.0\n8.0\n5.0\n4.5\n5.0\n6.0', solution([12, 4, 5, 3, 8, 7]))

    def test_provided_2(self):
        self.assertEqual('1.0\n1.5\n2.0\n2.5\n3.0\n3.5\n4.0\n4.5\n5.0\n5.5', solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


if __name__ == '__main__':
    unittest.main()
