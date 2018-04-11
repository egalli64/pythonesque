"""
HackerRank Algorithms Graph Theory Roads and Libraries

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/04/hackerrank-roads-and-libraries.html
      https://www.hackerrank.com/challenges/torque-and-development/problem

Given:
- the costs of building a library and a road, both as integer
- n nodes, m edges, leading to a forest of undirected graphs

Return the cheapest cost of having a library for each connected graph.
"""
from union_find import UnionFind

def solution(n, library, road, edges):
    if road >= library:
        return n * library

    uf = UnionFind(n)
    road_count = 0

    for edge in edges:
        if uf.union(edge[0] - 1, edge[1] - 1):
            road_count += 1
            if uf.count == 1:
                break

    return road_count * road + uf.count * library


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        nc, nr, cl, cr = map(int, input().split())

        items = []
        for _ in range(nr):
            items.append(list(map(int, input().split())))

        print(solution(nc, cl, cr, items))
