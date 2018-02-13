"""
Maximizing the Value of a Loot

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""
import unittest

from algs200x.w3.b_max_loot import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        self.assertEqual(180.0, solution(50, [(60, 20), (100, 50), (120, 30)]))

    def test_provided_2(self):
        self.assertAlmostEqual(166.6667, solution(10, [(500, 30)]), 4)


if __name__ == '__main__':
    unittest.main()
