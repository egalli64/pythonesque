"""
Number of Inversions

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""


def solution_naive(data):
    result = 0

    for i in range(len(data) - 1):
        for j in range(i+1, len(data)):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]
                result += 1

    return result


def merge(data, left, pivot, right):
    merged = []
    inversions = 0

    i = left
    j = pivot + 1
    while i <= pivot and j <= right:
        if data[i] > data[j]:
            inversions += (pivot - i + 1)
            merged.append(data[j])
            j += 1
        else:
            merged.append(data[i])
            i += 1

    for i in range(i, pivot + 1):
        merged.append(data[i])
    for j in range(j, right+1):
        merged.append(data[j])

    data[left:right + 1] = merged
    return inversions


def merge_sort(data, left, right):
    result = 0
    if left < right:
        pivot = left + (right - left) // 2
        result += merge_sort(data, left, pivot)
        result += merge_sort(data, pivot + 1, right)
        result += merge(data, left, pivot, right)
    return result


def solution_merge(data):
    return merge_sort(data, 0, len(data) - 1)


if __name__ == '__main__':
    input()  # header discarded

    items = [int(x) for x in input().split()]
    print(solution_merge(items))
