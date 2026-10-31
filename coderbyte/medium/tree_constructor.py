"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Tree Constructor
"""
import re
from collections import Counter


def tree_constructor(ls: list[str]) -> str:
    """Check if the passed list contains a valid binary tree"""
    nodes = [node_builder(item) for item in ls]
    return "true" if check_parents(nodes) and check_children(nodes) else "false"


def node_builder(s: str) -> tuple[int, int]:
    item = re.findall(r"\d+", s)
    return int(item[0]), int(item[1])


def check_parents(nodes: list[tuple[int, int]]) -> bool:
    max_freq = max(Counter([right for _, right in nodes]).values())
    return False if max_freq > 2 else True


def check_children(nodes: list[tuple[int, int]]) -> bool:
    max_freq = max(Counter([left for left, _ in nodes]).values())
    return False if max_freq > 1 else True
