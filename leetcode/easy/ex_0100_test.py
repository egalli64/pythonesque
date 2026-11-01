"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

100. Same Tree: https://leetcode.com/problems/same-tree/description/
"""
from tree_node import TreeNode
from ex_0100 import is_same_tree


class TestSolution:
    def test_given_1(self):
        left = TreeNode(1, TreeNode(2), TreeNode(3))
        right = TreeNode(1, TreeNode(2), TreeNode(3))
        assert is_same_tree(left, right) == True

    def test_given_2(self):
        left = TreeNode(1, TreeNode(2))
        right = TreeNode(1, None, TreeNode(2))
        assert is_same_tree(left, right) == False

    def test_given_3(self):
        left = TreeNode(1, TreeNode(2), TreeNode(1))
        right = TreeNode(1, TreeNode(1), TreeNode(2))
        assert is_same_tree(left, right) == False
