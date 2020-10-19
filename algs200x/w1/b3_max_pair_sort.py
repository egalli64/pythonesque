def max_pair(values):
    assert(len(values) > 1)
    values.sort(reverse=True)

    return values[0] * values[1]
