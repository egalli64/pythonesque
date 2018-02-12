"""
Last Digit of the Sum of Fibonacci Numbers

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x

"""
import unittest

from algs200x.w2.e_fibonacci_sum_1 import solution as naive
from algs200x.w2.e_fibonacci_sum_2 import solution as smarter


class TestSolution(unittest.TestCase):
    def test_naive_1(self):
        self.assertEqual(4, naive(3))

    def test_naive_2(self):
        self.assertEqual(5, naive(100))

    def test_smarter_1(self):
        self.assertEqual(4, smarter(3))

    def test_smarter_2(self):
        self.assertEqual(5, smarter(100))

    def test_smarter_big(self):
        self.assertEqual(3, smarter(832564823476))

    def test_smarter_limit(self):
        self.assertEqual(9, smarter(614162383528))


if __name__ == '__main__':
    unittest.main()
