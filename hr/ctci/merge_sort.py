"""
HackerRank Cracking the Coding Interview  Merge Sort: Counting Inversions
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2017/03/hackerrank-merge-sort-counting.html
      https://www.hackerrank.com/challenges/ctci-merge-sort
"""


def merge(data, left, center, right):
    merged = []
    result = 0

    i = left
    j = center + 1
    while i <= center and j <= right:
        if data[i] > data[j]:
            result += (center - i + 1)
            merged.append(data[j])
            j += 1
        else:
            merged.append(data[i])
            i += 1

    for i in range(i, center+1):
        merged.append(data[i])
    for j in range(j, right+1):
        merged.append(data[j])

    data[left:right+1] = merged
    return result


def merge_sort(a, left, right):
    result = 0
    if left < right:
        center = left + (right - left) // 2
        result += merge_sort(a, left, center)
        result += merge_sort(a, center + 1, right)
        result += merge(a, left, center, right)
    return result


def count_inversions(a):
    return merge_sort(a, 0, len(a) - 1)


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        print(count_inversions(arr))
