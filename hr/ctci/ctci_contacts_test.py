"""
HackerRank Tutorials  Cracking the Coding Interview  Tries: Contacts - plain version
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-tries-contacts.html
      https://www.hackerrank.com/challenges/ctci-contacts
"""

import unittest

from hr.ctci.ctci_contacts import trie, add, find


class TestCodeEval(unittest.TestCase):

    def test_provided_1(self):
        add(trie, 'hack')
        add(trie, 'hackerrank')
        self.assertEqual(2, find(trie, 'hac'))

    def test_provided_2(self):
        add(trie, 'hack')
        add(trie, 'hackerrank')
        self.assertEqual(0, find(trie, 'hak'))


if __name__ == '__main__':
    unittest.main()
