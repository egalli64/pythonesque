"""
Template for HackerRank problems
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/
"""

import unittest
from hr.template import solution


class TestSolution(unittest.TestCase):

    def test_provided_1(self):
        self.assertEqual('something', solution('something'))


if __name__ == '__main__':
    unittest.main()
