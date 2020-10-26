def max_pair(values):
    assert(len(values) > 1)

    first = values[0]
    second = values[1]
    if second > first:
        first, second = second, first

    for i in range(2, len(values)):
        if values[i] > first:
            first, second = values[i], first
        elif values[i] > second:
            second = values[i]

    return first * second
