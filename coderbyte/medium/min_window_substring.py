"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Min Window Substring
"""
from collections import Counter


def min_window_substring(str_arr: list[str]):
    source, target = str_arr
    target_counts = Counter(target)
    window_counts = Counter()

    required_matching = len(target_counts)
    matching = 0

    left = 0
    min_window_len = len(source) + 1
    min_window = ""

    for right, current in enumerate(source):
        window_counts[current] += 1

        if current in target_counts and window_counts[current] == target_counts[current]:
            matching += 1

        while left <= right and matching == required_matching:
            if (right - left + 1) < min_window_len:
                min_window_len = right - left + 1
                min_window = source[left:right + 1]

            left_char = source[left]
            window_counts[left_char] -= 1
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                matching -= 1
            left += 1

    return min_window
