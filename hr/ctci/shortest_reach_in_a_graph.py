"""
HackerRank Cracking the Coding Interview BFS: Shortest Reach in a Graph
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

Implement a BFS to get the shortest distance from a node to every other node in a graph
"""
from collections import defaultdict, deque
DISTANCE = 6


class Graph:
    def __init__(self, size):
        self.size = size
        self.neighbors = defaultdict(lambda: [])

    def connect(self, x, y):
        self.neighbors[x].append(y)
        self.neighbors[y].append(x)

    def find_all_distances(self, root):
        result = [-1] * self.size
        buffer = deque()

        result[root] = 0
        buffer.append(root)

        while buffer:
            current = buffer.popleft()
            for neighbor in self.neighbors[current]:
                if result[neighbor] < 0:
                    result[neighbor] = result[current] + DISTANCE
                    buffer.append(neighbor)

        result.pop(root)
        return result


def solution(nodes, edges, start):
    g = Graph(nodes)
    for edge in edges:
        g.connect(edge[0] - 1, edge[1] - 1)
    return g.find_all_distances(start - 1)


if __name__ == '__main__':
    nr_queries = int(input())
    for _ in range(nr_queries):
        nr_nodes, nr_edges = [int(x) for x in input().split()]
        tuples = []
        for _ in range(nr_edges):
            tuples.append(tuple(int(x) for x in input().split()))
        head = int(input())

        print(' '.join(map(str, solution(nr_nodes, tuples, head))))
