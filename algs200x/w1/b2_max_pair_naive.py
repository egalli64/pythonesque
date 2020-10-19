
def max_pair(values):
    assert(len(values) > 1)

    result = 0

    n = len(values)
    for i in range(n):
        for j in range(i+1, n):
            result = max(result, values[i] * values[j])

    return result
