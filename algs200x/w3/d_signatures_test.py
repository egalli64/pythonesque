"""
Collecting Signatures

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""
import unittest

from algs200x.w3.d_signatures import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        counter, elements = solution([(1, 3), (2, 5), (3, 6)])
        self.assertEqual(counter, 1)
        self.assertEqual(elements[0], 3)

    def test_provided_2(self):
        counter, elements = solution([(4, 7), (1, 3), (2, 5), (5, 6)])
        self.assertEqual(counter, 2)
        self.assertEqual(elements[0], 3)
        self.assertEqual(elements[1], 6)


if __name__ == '__main__':
    unittest.main()
