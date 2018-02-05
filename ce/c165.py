"""
Suggest Groups
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-suggest-groups.html
      https://www.codeeval.com/open_challenges/165/
"""

import sys


def solution(data):
    users = [row.split(':') for row in data.rstrip().split('\n')]
    u_groups = {}
    for user in users:
        for i in [1, 2]:
            user[i] = user[i].split(',') if user[i] else []
        u_groups[user[0]] = user.pop()

    suggestions = {}
    for user in users:
        candidates = {}
        for friend in user[1]:
            for group in u_groups[friend]:
                candidates[group] = candidates.setdefault(group, 0) + 1
        for group in candidates:
            if group not in u_groups[user[0]] and candidates[group] >= len(user[1]) / 2:
                suggestions.setdefault(user[0], []).append(group)

    result = ['%s:%s' % (u, ','.join(sorted(suggestions[u]))) for u in sorted(suggestions.keys())]
    return '\n'.join(result) + '\n'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = open(sys.argv[1], 'r')
        print(solution(file.read()))
        file.close()
    else:
        print('Data filename expected as argument!')
