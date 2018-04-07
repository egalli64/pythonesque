"""
HackerRank Algorithms Implementation The Hurdle Race

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/the-hurdle-race/problem
      

Given an integer, natural limit, and a list of integer, hurdles to be jumped
Return the extra-push required to jump the highest hurdle
"""

def solution(natural, heights):
    delta = max(heights) - natural
    return 0 if delta < 1 else delta
    

if __name__ == '__main__':
    _, k = map(int, input().split())
    data = list(map(int, input().split()))

    print(solution(k, data))
