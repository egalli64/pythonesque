"""
HackerRank Tutorials  Cracking the Coding Interview  Tries: Contacts - plain version
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-tries-contacts.html
      https://www.hackerrank.com/challenges/ctci-contacts
"""


class Node:
    def __init__(self):
        self.count = 1
        self.children = {}


trie = Node()


def add(node, name):
    for letter in name:
        sub = node.children.get(letter)
        if sub:
            sub.count += 1
        else:
            sub = node.children[letter] = Node()
        node = sub


def find(node, data):
    for letter in data:
        sub = node.children.get(letter)
        if not sub:
            return 0
        node = sub
    return node.count


if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        op, param = input().split()
        if op == 'add':
            add(trie, param)
        else:
            print(find(trie, param))
