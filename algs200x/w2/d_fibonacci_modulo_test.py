"""
Calculate Fibonacci modulo m

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/fibonacci-modulo-with-pisano-period.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x

"""
import unittest

from algs200x.w2.d_fibonacci_modulo_1 import solution as naive
from algs200x.w2.d_fibonacci_modulo_2 import solution as pisano


class TestSolution(unittest.TestCase):
    def test_naive_1(self):
        self.assertEqual(161, naive(239, 1000))

    # too slow to bear it
    # def test_naive_2(self):
    #     self.assertEqual(10249, solution_1(2816213588, 30524))

    # too slow
    def test_naive_3(self):
        self.assertEqual(125, naive(5 * 10 ** 5, 1000))

    def test_pisano_0(self):
        self.assertEqual(1, pisano(15, 3))

    def test_pisano_1(self):
        self.assertEqual(161, pisano(239, 1000))

    def test_pisano_20M(self):
        self.assertEqual(125, pisano(2 * 10 ** 7, 1000))


if __name__ == '__main__':
    unittest.main()
