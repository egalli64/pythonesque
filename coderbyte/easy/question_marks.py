"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Questions Marks
"""


def question_marks(s: str) -> str:
    """
    Ensure that each pair of digits that addup to 10 are interleaved by exactly three question marks.
    Return false if a negative case is found, or no pair with 10-sum is found
    """
    count = 0

    i = 0
    while i < len(s):
        if s[i].isdigit():
            left = int(s[i])
            j = s.find(str(10 - left), i + 1)
            if j == -1:
                i += 1
            elif s.count("?", i, j) != 3:
                return "false"
            else:
                count += 1
                i = j
        else:
            i += 1

    return "true" if count else "false"
