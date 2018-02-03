"""
HackerRank Tutorials  Cracking the Coding Interview  Tries: Contacts - chunk version
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/02/hackerrank-tries-contacts.html
      https://www.hackerrank.com/challenges/ctci-contacts
"""


class Node:
    def __init__(self, data=None):
        self.count = 1
        self.data = data
        self.children = {}


trie = Node()


def add(node, name):
    for i in range(len(name)):
        sub = node.children.get(name[i])
        if not sub:
            node.children[name[i]] = Node(name[i:])
            return

        sub.count += 1
        if sub.data == name[i:]:
            return
        elif len(sub.data) > 1:
            split = sub.data[1:]
            sub.data = sub.data[0]
            sub.children[split[0]] = Node(split)
        node = sub


def find(node, data):
    for i in range(len(data)):
        node = node.children.get(data[i])
        if not node:
            return 0
        if node.data.startswith(data[i:]):
            break
    return node.count


if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        op, param = input().split()
        if op == 'add':
            add(trie, param)
        else:
            print(find(trie, param))
