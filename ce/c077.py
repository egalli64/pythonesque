"""
CodeEval Da Vyncy
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/77/
"""
import sys


def overlapping(lhs, rhs):
    """
    Calculate the size of the overlapping section between the two fragments
    :param lhs: left fragment 
    :param rhs: right fragment
    :return: overlapping size
    """
    result = 0
    for i in range(1, len(rhs)):
        if lhs.endswith(rhs[0:i]):
            result = i
    return result


def merge_largest(fragments):
    """
    Merge the two largest fragments in a new one
    :param fragments: list of fragments
    :return: False when no more merging is possible
    """
    indices = None
    overlap = 0

    for i in range(len(fragments)):
        for j in range(i+1, len(fragments)):
            for pos in [(i, j), (j, i)]:
                candidate_overlap = overlapping(fragments[pos[0]], fragments[pos[1]])
                if candidate_overlap > overlap:
                    overlap = candidate_overlap
                    indices = (pos[0], pos[1])

    if overlap == 0:
        return False

    merged = fragments[indices[0]] + fragments[indices[1]][overlap:]
    fragments.append(merged)

    fragments.pop(indices[1] if indices[1] > indices[0] else indices[0])
    fragments.pop(indices[0] if indices[0] < indices[1] else indices[1])
    return True


def solution(line):
    """
    Solve the problem for a single test case
    :param line: the fragments, as a CSV string w/ semicolon as separator
    :return: the longest fragment after merging
    """
    fragments = line.split(';')
    while merge_largest(fragments):
        pass
    return max(fragments, key=len)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as file:
            for test in file:
                print(solution(test.rstrip('\n')))
    else:
        print('Data filename expected as argument!')
