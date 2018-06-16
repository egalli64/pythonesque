# Learn Python Challenge: Day 6 Exercises

def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    assert height % 2 == 0, 'diamond height must be an even integer'

    result = ''
    left, right = '/', '\\'
    middle = height // 2
    for i in range(height):
        if i == middle:
            # swap delimiters
            left, right = right, left

        sz = i+1 if i < middle else height - i
        result += (left * sz).rjust(middle) + (right * sz).ljust(middle) + '\n'

    return result[:-1]

if __name__ == '__main__':
    print(diamond(4))