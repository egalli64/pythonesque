"""
Improving Quick Sort

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""
import unittest

from algs200x.w4.c_quick import solution_quick, solution_quick3


class TestSolution(unittest.TestCase):

    def test_quick_1(self):
        data = [2, 3, 9, 2, 2]
        solution_quick(data)
        self.assertEqual(2, data[0])
        self.assertEqual(2, data[1])
        self.assertEqual(2, data[2])
        self.assertEqual(3, data[3])
        self.assertEqual(9, data[4])

    def test_quick_2(self):
        data = [x for x in range(10, -1, -1)] * 10000
        solution_quick(data)

        self.assertEqual(0, data[0])
        self.assertEqual(1, data[10000])
        self.assertEqual(2, data[20000])
        self.assertEqual(3, data[30000])
        self.assertEqual(4, data[40000])

    def test_quick3_1(self):
        data = [2, 3, 9, 2, 2]
        solution_quick3(data)
        self.assertEqual(2, data[0])
        self.assertEqual(2, data[1])
        self.assertEqual(2, data[2])
        self.assertEqual(3, data[3])
        self.assertEqual(9, data[4])

    def test_quick3_2(self):
        data = [x for x in range(10, -1, -1)] * 10000
        solution_quick3(data)

        self.assertEqual(0, data[0])
        self.assertEqual(1, data[10000])
        self.assertEqual(2, data[20000])
        self.assertEqual(3, data[30000])
        self.assertEqual(4, data[40000])


if __name__ == '__main__':
    unittest.main()
