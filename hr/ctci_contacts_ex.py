"""
HackerRank Tutorials  Cracking the Coding Interview  Tries: Contacts - no trie
author: Unknown - Anonymous contribution to the blog
info: http://thisthread.blogspot.com/2017/02/hackerrank-tries-contacts.html
      https://www.hackerrank.com/challenges/ctci-contacts
"""

match = set()
count = dict()

for i in range(int(input())):
    op = input().split(' ')
    if op[0] == 'add':
        contact = list(op[1])
        for j in range(len(op[1])):
            word = ''.join(contact[:j + 1])
            if word in match:
                count[word] += 1
            else:
                match.add(word)
                count[word] = 1
    else:  # 'find' assumed
        print(count[op[1]] if op[1] in count else 0)
