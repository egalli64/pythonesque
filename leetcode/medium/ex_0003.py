"""
LeetCode Problems: https://leetcode.com/problemset/
My solutions: https://github.com/egalli64/pythonesque/leetcode

3. Longest Substring Without Repeating Characters https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without duplicate characters.
    """
    buffer: dict[str, int] = {}

    result = 0
    first = 0

    for i, ch in enumerate(s):
        if ch in buffer and buffer[ch] >= first:
            result = max(result, i - first)
            first = buffer[ch] + 1
        buffer[ch] = i

    return max(result, len(s) - first)


def length_of_longest_substring_alt(s: str) -> int:
    buffer: dict[str, int] = {}

    result = 0
    first = 0

    for i, ch in enumerate(s):
        if ch in buffer:
            for j in range(first, buffer[ch] + 1):
                buffer.pop(s[j])
                first += 1

        buffer[ch] = i
        result = max(result, len(buffer))

    return result
