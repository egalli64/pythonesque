"""
HackerRank Algorithms Implementation Beautiful Days at the Movies

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

Given three integers i, j, k
Return how many beautiful number are in [i .. j] where
 beautiful means that abs(x - reverse(x)) % k == 0
"""
def solution(first, last, divisor):
    result = 0
    for i in range(first, last + 1):
        if (i - int(str(i)[::-1])) % divisor == 0:
            result += 1
    return result

if __name__ == '__main__':
    i, j, k = map(int, input().split())
    print(solution(i, j, k))