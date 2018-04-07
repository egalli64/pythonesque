"""
HackerRank Algorithms Implementation Climbing the Leaderboard

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/04/hackerrank-climbing-leaderboard.html
      https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem
      

Given two list of integers:
- scores: monotonically decreasing
- alice: her scoring in time - monotonically increasing
Return her history following the dense ranking convention
"""
from bisect import bisect


def solution_bisect(scores, alice):
    ranking = [scores[-1]]
    for i in range(len(scores)-2, -1, -1):
        if scores[i] > ranking[-1]:
            ranking.append(scores[i])
    
    # or, more compact but expensive too
    # ranking = sorted(list(set(scores)))

    results = []
    last = len(ranking) + 1
    for score in alice:
        results.append(last - bisect(ranking, score))

    return results

def solution(scores, alice):
    ranking = [scores[0]]
    for score in scores[1:]:
        if score < ranking[-1]:
            ranking.append(score)
    
    results = []
    for score in alice:
        while ranking and score >= ranking[-1]:
            ranking.pop()
        results.append(len(ranking) + 1)
    
    return results
    

if __name__ == '__main__':
    input()  # discard header
    a = list(map(int, input().split()))

    input()  # discard header
    b = list(map(int, input().split()))

    print('\n'.join(map(str, solution(a, b))))
