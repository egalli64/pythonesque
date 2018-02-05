"""
HackerRank Tutorials  Cracking the Coding Interview  Heaps: Find the Running Median
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-heaps-find-running-median.html
      https://www.hackerrank.com/challenges/ctci-find-the-running-median
"""
from heapq import heappop, heappush


class MedianHeap:
    def __init__(self):
        self.left = []   # max heap
        self.right = []  # min heap

    def push(self, value):
        if not self.left or value < -self.left[0]:
            heappush(self.left, -value)
        else:
            heappush(self.right, value)

        # balance the heaps
        bigger = self.left if len(self.left) > len(self.right) else self.right
        smaller = self.left if len(self.left) < len(self.right) else self.right
        if len(bigger) - len(smaller) > 1:
            moved = -1 * heappop(bigger)
            heappush(smaller, moved)

    def median(self):
        bigger = self.left if len(self.left) > len(self.right) else self.right
        smaller = self.left if len(self.left) < len(self.right) else self.right

        if bigger is smaller:
            return (self.right[0] - self.left[0]) / 2
        else:
            maxi = -1.0 if bigger is self.left else 1.0
            return maxi * bigger[0]


def solution(values):
    heap = MedianHeap()

    result = []
    for value in values:
        heap.push(value)
        result.append(str(heap.median()))

    return '\n'.join(result)


if __name__ == '__main__':
    n = int(input())
    data = []
    for i in range(n):
        data.append(int(input()))

    print(solution(data))
