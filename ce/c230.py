"""
Football
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/01/codeeval-football.html
      https://www.codeeval.com/open_challenges/230/
"""
import sys


def solution(line):
    teams = {}
    for country, clubs in enumerate(line.split(' | '), start=1):
        for team in map(int, clubs.split()):
            teams.setdefault(team, []).append(str(country))
    result = ["{}:{};".format(key, ",".join(teams[key])) for key in sorted(teams.keys())]
    return ' '.join(result)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        test_cases = open(sys.argv[1], 'r')
        for test in test_cases:
            print(solution(test.rstrip('\n')))
        test_cases.close()
    else:
        print('Data filename expected as argument!')