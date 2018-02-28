"""
Maximum Amount of Gold

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 6 - Dynamic Programming 2
"""
import unittest

from algs200x.w6.a_gold import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(9, solution(10, [1, 4, 8]))


if __name__ == '__main__':
    unittest.main()
