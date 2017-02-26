"""
HackerRank Tutorials  Cracking the Coding Interview  Sorting: Bubble Sort
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.hackerrank.com/challenges/ctci-bubble-sort
"""
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

tot_swaps = 0
for i in range(n):
    swaps = 0
    for j in range(n-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j+1], a[j]
            swaps += 1
    if not swaps:
        break
    else:
        tot_swaps += swaps

print('Array is sorted in {} swaps.'.format(tot_swaps))
print('First Element:', a[0])
print('Last Element:', a[-1])
