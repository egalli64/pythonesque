"""
Maximizing the Number of Prize Places in a Competition

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 3 - greedy algorithms
"""
import unittest

from algs200x.w3.e_prizes import solution


class TestSolution(unittest.TestCase):
    def test_provided_1(self):
        size, elements = solution(6)
        self.assertEqual(size, 3)
        self.assertEqual(elements[0], 1)
        self.assertEqual(elements[1], 2)
        self.assertEqual(elements[2], 3)

    def test_provided_2(self):
        size, elements = solution(8)
        self.assertEqual(size, 3)
        self.assertEqual(elements[0], 1)
        self.assertEqual(elements[1], 2)
        self.assertEqual(elements[2], 5)

    def test_provided_3(self):
        size, elements = solution(2)
        self.assertEqual(size, 1)
        self.assertEqual(elements[0], 2)

    def test_provided_ex(self):
        size, elements = solution(182414564)
        self.assertEqual(size, 19100)
        self.assertEqual(elements[-1], 19114)


if __name__ == '__main__':
    unittest.main()
