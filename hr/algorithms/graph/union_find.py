"""
UnionFind

Based on Union-find (weighted quick-union)
From Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne
https://algs4.cs.princeton.edu/home/

author: Manny egalli64@gmail.com
info:   http://thisthread.blogspot.com/2018/04/union-find.html
        http://thisthread.blogspot.com/2018/04/hackerrank-roads-and-libraries.html
"""

class UnionFind:
    def __init__(self, n):
        self.count = n
        self.id = [i for i in range(n)]
        self.sz = [1 for i in range(n)]

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return False

        self.count -= 1
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        return True
        

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p
    
    def connected(self, p, q):
        return self.find(p) == self.find(q)
