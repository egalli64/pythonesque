"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1518. Water Bottles
https://leetcode.com/problems/water-bottles/description/
"""

import unittest
from ex_0066 import plusOne


class TestPlusOne(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual(plusOne([1,2,3]), [1,2,4])

    def test_given_2(self):
        self.assertEqual(plusOne([4,3,2,1]), [4,3,2,2])

    def test_given_3(self):
        self.assertEqual(plusOne([9]), [1,0])

if __name__ == "__main__":
    unittest.main()
