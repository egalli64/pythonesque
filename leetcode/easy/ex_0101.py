"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

101. Symmetric Tree
"""
from tree_node import TreeNode


def is_mirror(left: TreeNode | None, right: TreeNode | None) -> bool:
    if left is None and right is None:
        return True
    elif left is None or right is None:
        return False
    else:
        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)


def is_symmetric(root: TreeNode | None) -> bool:
    """Check if the tree is symmetric."""
    return True if root is None else is_mirror(root.left, root.right)
