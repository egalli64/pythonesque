"""
LeetCode Easy Problems: https://leetcode.com/problemset/?difficulty=EASY
My solutions: https://github.com/egalli64/pythonesque/leetcode

1957. Delete Characters to Make Fancy String
https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
"""


def makeFancyString(s: str) -> str:
    """
    No more that two consecutive chars are allowed in the passed string

    Assume the input string is not empty
    """
    result = [s[0]]
    prev = s[0]
    counter = 1

    for cur in s[1:]:
        if cur == prev:
            counter += 1
        else:
            counter = 1

        if counter < 3:
            result.append(cur)

        prev = cur

    return "".join(result)
