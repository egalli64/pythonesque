"""
UnionFind

Based on Union-find (weighted quick-union)
From Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne
https://algs4.cs.princeton.edu/home/

author: Manny egalli64@gmail.com
info:   http://thisthread.blogspot.com/
"""

import unittest
from union_find import UnionFind


class TestUnionFind(unittest.TestCase):

    def test_tiny(self):
        uf = UnionFind(10)
        uf.union(4, 3)
        uf.union(3, 8)
        uf.union(6, 5)
        uf.union(9, 4)
        uf.union(2, 1)
        uf.union(5, 0)
        uf.union(7, 2)
        uf.union(6, 1)

        self.assertEqual(2, uf.count)
        self.assertTrue(uf.connected(2, 6))
        self.assertFalse(uf.connected(4, 5))


if __name__ == '__main__':
    unittest.main()

