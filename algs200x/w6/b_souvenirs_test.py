"""
Partitioning Souvenirs

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/06/partitioning-souvenirs-patched.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 6 - Dynamic Programming 2 - 3-Partition problem
"""
import unittest

from b_souvenirs import solution


class TestSolution(unittest.TestCase):
    def test_provided_2(self):
        self.assertFalse(solution([40]))

    def test_provided_3(self):
        self.assertTrue(solution([17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]))

    def test_provided_4(self):
        self.assertTrue(solution([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]))

    def test_extra(self):
        self.assertTrue(solution([1, 2, 1, 2]))

    def test_extra_2(self):
        self.assertFalse(solution([6, 6, 3]))

    def test_extra_3(self):
        self.assertTrue(solution([3, 1, 1, 2, 2]))

    def test_test_1(self):
        self.assertTrue(solution([1, 1, 1]))

    def test_test_2(self):
        self.assertFalse(solution([3, 3, 3, 3]))

    def test_test_3(self):
        self.assertFalse(solution([4, 1, 3, 2]))

    def test_test_4(self):
        self.assertFalse(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    def test_test_5(self):
        self.assertTrue(solution([12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]))

    def test_test_6(self):
        self.assertTrue(solution([20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]))

    def test_test_7(self):
        self.assertTrue(solution([19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]))

    def test_test_8(self):
        self.assertFalse(solution([1, 1, 1, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1]))

    def test_test_9(self):
        self.assertTrue(solution([1, 2, 2, 2, 1, 3, 3, 3, 2, 2, 3, 2, 1, 2, 3, 3, 2, 2]))

    def test_test_10(self):
        self.assertFalse(solution([6, 7, 8, 5, 11, 3, 1, 19, 16, 19, 5, 7, 13, 10, 16, 4, 15, 16]))

    def test_test_11(self):
        self.assertTrue(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))

    def test_shuai(self):
        self.assertFalse(solution([7, 2, 2, 2, 2, 2, 2, 2, 3]))

    def test_confounding_choice(self):
        self.assertFalse(solution([3, 2, 2, 2, 3]))

    def test_duplicates(self):
        self.assertTrue(solution([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))


if __name__ == '__main__':
    unittest.main()
