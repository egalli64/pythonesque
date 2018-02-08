"""
HackerRank Cracking the Coding Interview DFS: Connected Cell in a Grid
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/hackerrank-dfs-connected-cell-in-grid.html
      https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid

Given an n x m matrix, find and print the number of cells in the largest region in the matrix.
"""


def connected(matrix, i, j):
    """
        If there is life in matrix[i][j], count the connected living cells
        Warning! For efficiency reason this is a disruptive algorithm!
    """
    if not (0 <= i < len(matrix)) or not (0 <= j < len(matrix[0])):
        return 0

    if matrix[i][j] != 1:
        return 0

    result = 1
    matrix[i][j] = 0

    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            if i != ii or j != jj:
                result += connected(matrix, ii, jj)

    return result


def solution(matrix):
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result = max(result, connected(matrix, i, j))
    return result


if __name__ == '__main__':
    n = int(input().strip())
    m = int(input().strip())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    print(solution(grid))
