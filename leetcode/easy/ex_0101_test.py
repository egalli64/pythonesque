"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

101. Symmetric Tree
"""
from tree_node import TreeNode
from ex_0101 import is_symmetric


class TestSolution:
    def test_given_1(self):
        tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        assert is_symmetric(tree) == True

    def test_given_2(self):
        tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
        assert is_symmetric(tree) == False
