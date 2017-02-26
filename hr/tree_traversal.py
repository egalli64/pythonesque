"""
HackerRank Tutorials  30 Days of Code  Day 23: BST Level-Order Traversal
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/tree-traversal.html
      https://www.hackerrank.com/challenges/30-binary-trees
"""

from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def in_order_r(node):
    if not node:
        return []
    return in_order_r(node.left) + [node.data] + in_order_r(node.right)


def in_order_i(node):
    if not node:
        return []

    cur = node
    result = []
    stack = []
    while True:
        if cur:
            stack.append(cur)
            cur = cur.left
        elif stack:
            cur = stack.pop()
            result.append(cur.data)
            cur = cur.right
        else:
            return result


def pre_order_r(node):
    if not node:
        return []
    return [node.data] + pre_order_r(node.left) + pre_order_r(node.right)


def pre_order_i(node):
    if not node:
        return []

    result = []
    stack = [node]
    while stack:
        cur = stack.pop()
        result.append(cur.data)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return result


def post_order_r(node):
    if not node:
        return []
    return post_order_r(node.left) + post_order_r(node.right) + [node.data]


def post_order_i(node):
    if not node:
        return []

    stack = [node]
    result = deque()
    while stack:
        cur = stack.pop()
        result.appendleft(cur.data)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return result


def level_order_i(node):
    result = []
    buffer = deque([node])
    while buffer:
        cur = buffer.popleft()
        result.append(cur.data)
        if cur.left:
            buffer.append(cur.left)
        if cur.right:
            buffer.append(cur.right)
    return result


def level_order_rs(nodes):
    result = []
    below = []
    for node in nodes:
        result.append(node.data)
        if node.left:
            below.append(node.left)
        if node.right:
            below.append(node.right)
    if below:
        result += level_order_rs(below)
    return result


def level_order_r(node):
    return level_order_rs([node])
