"""
HackerRank Algorithms Implementation Designer PDF Viewer

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
      

Given a list of int, heights of [a..z] characters, and a string of them
Return the area taken by the string, assuming each char having width 1.
"""

def solution(heights, word):
    height = 0

    for c in word:
        height = max(height, heights[ord(c) - ord('a')])

    return height * len(word)

if __name__ == '__main__':
    data = list(map(int, input().split()))
    w = input().strip()

    print(solution(data, w))
