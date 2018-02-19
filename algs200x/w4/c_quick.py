"""
Improving Quick Sort

author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/2018/02/a-few-divide-and-conquer-problems.html
      https://www.edx.org/course/algorithmic-design-techniques-uc-san-diegox-algs200x
      week 4 - Divide and Conquer
"""


def partition(data, left, right):
    pivot = data[left]

    i = left
    j = right + 1

    while True:
        i += 1
        while data[i] < pivot:
            if i == right:
                break
            i += 1

        j -= 1
        while data[j] > pivot:
            if j == left:
                break
            j -= 1

        if i >= j:
            break
        data[i], data[j] = data[j], data[i]

    data[left], data[j] = data[j], data[left]
    return j


def quick(data, left, right):
    if right <= left:
        return

    pivot = partition(data, left, right)
    quick(data, left, pivot - 1)
    quick(data, pivot + 1, right)


def solution_quick(data):
    quick(data, 0, len(data) - 1)


def quick3(data, left, right):
    if right <= left:
        return

    p_left = left
    p_right = right
    pivot = data[left]
    i = left + 1
    while i <= p_right:
        if data[i] < pivot:
            data[p_left], data[i] = data[i], data[p_left]
            p_left += 1
            i += 1
        elif data[i] > pivot:
            data[p_right], data[i] = data[i], data[p_right]
            p_right -= 1
        else:
            i += 1

    quick3(data, left, p_left - 1)
    quick3(data, p_right + 1, right)


def solution_quick3(data):
    quick3(data, 0, len(data) - 1)


if __name__ == '__main__':
    input()  # discard header

    line = input().split()

    items = [int(x) for x in line]
    solution_quick(items)
    print(' '.join(str(x) for x in items))
