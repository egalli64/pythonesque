"""
HackerRank Tutorials  30 Days of Code  Day 23: BST Level-Order Traversal
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/tree-traversal.html
      https://www.hackerrank.com/challenges/30-binary-trees
"""
import unittest
from hr.tree_traversal import *


class TestSolution(unittest.TestCase):

    def setUp(self):
        node1 = Node(1)
        node2 = Node(2, node1)
        node4 = Node(4)
        node7 = Node(7)
        node5 = Node(5, node4, node7)

        self.root = Node(3, node2, node5)

    def test_in_order_r(self):
        self.assertEqual([1, 2, 3, 4, 5, 7], in_order_r(self.root))

    def test_in_order_i(self):
        self.assertEqual([1, 2, 3, 4, 5, 7], in_order_i(self.root))

    def test_pre_order_r(self):
        self.assertEqual([3, 2, 1, 5, 4, 7], pre_order_r(self.root))

    def test_pre_order_i(self):
        self.assertEqual([3, 2, 1, 5, 4, 7], pre_order_i(self.root))

    def test_post_order_r(self):
        self.assertEqual([1, 2, 4, 7, 5, 3], post_order_r(self.root))

    def test_post_order_i(self):
        expected_values = [1, 2, 4, 7, 5, 3]
        result = post_order_i(self.root)
        self.assertEqual(len(expected_values), len(result))
        for expected, actual in zip(expected_values, result):
            self.assertEqual(expected, actual)

    def test_level_order_r(self):
        self.assertEqual([3, 2, 5, 1, 4, 7], level_order_r(self.root))

    def test_level_order_i(self):
        self.assertEqual([3, 2, 5, 1, 4, 7], level_order_i(self.root))

if __name__ == '__main__':
    unittest.main()
