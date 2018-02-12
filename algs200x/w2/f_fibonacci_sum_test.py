"""
Last Digit of the Partial Sum of Fibonacci Numbers

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/last-digit-of-sum-of-fibonacci-numbers.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
"""
import unittest

from algs200x.w2.f_fibonacci_sum_1 import solution as naive
from algs200x.w2.f_fibonacci_sum_2 import solution as smarter


class TestSolution(unittest.TestCase):
    def test_naive_1(self):
        self.assertEqual(1, naive(3, 7))

    def test_naive_2(self):
        self.assertEqual(5, naive(10, 10))

    def test_naive_3(self):
        self.assertEqual(2, naive(10, 200))

    # too slow
    # def test_naive_big(self):
    #     self.assertEqual(2, naive(1, 100000000))

    def test_smarter_1(self):
        self.assertEqual(1, smarter(3, 7))

    def test_smarter_3(self):
        self.assertEqual(2, smarter(10, 200))

    def test_smarter_big(self):
        self.assertEqual(5, smarter(1, 100000000))


if __name__ == '__main__':
    unittest.main()
