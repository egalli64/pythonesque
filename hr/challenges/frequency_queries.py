from collections import defaultdict


def freqQuery(queries):
    frequencies = {}
    inverse = defaultdict(int)

    result = []
    for query in queries:
        command, value = query

        if command != 3: # edit
            current = frequencies.get(value, 0)
            if current:
                inverse[current] -= 1
            if command == 1: # insert
                frequencies[value] = current + 1
            elif current: # delete
                frequencies[value] -= 1

            if value in frequencies:
                inverse[frequencies[value]] += 1
        else:
            result.append(1 if inverse.get(value) else 0)

    return result
