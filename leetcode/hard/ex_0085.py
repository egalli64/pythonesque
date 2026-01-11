"""
LeetCode Problems: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

85. Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle/description/
Find the largest rectangle containing only 1's and return its area.
"""

from typing import List

def _area_largest_rectangle(heights: List[int]) -> int:
    stack = []
    result = 0
    for i, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > height:
            h_idx = stack.pop()
            h_val = heights[h_idx]
            left = stack[-1] if stack else -1
            width = i - left - 1
            result = max(result, h_val * width)
        stack.append(i)
    return result


def maximalRectangle(matrix: List[List[str]]) -> int:
    n_cols = len(matrix[0])
    heights = [0] * n_cols
    result = 0

    for row in matrix:
        for i, val in enumerate(row):
            heights[i] = heights[i] + 1 if val == '1' else 0

        result = max(result, _area_largest_rectangle(heights))

    return result

if __name__ == "__main__":
    print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 6)
    print(maximalRectangle([["0"]]) == 0)
    print(maximalRectangle([["1"]]) == 1)
