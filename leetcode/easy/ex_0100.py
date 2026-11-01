"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

100. Same Tree: https://leetcode.com/problems/same-tree/description/
"""
from tree_node import TreeNode


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Check if two trees are equal."""
    if p is None and q is None:
        return True
    elif p is None or q is None or p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
