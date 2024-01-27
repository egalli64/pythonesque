"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
count_code: https://codingbat.com/prob/p186048
"""


def count_code(str: str):
    """
    Parameters:
        str
    return the number of times the pattern "co.e" is in the input string
    """
    count = 0
    pos = 0

    while True:
        head = str.find("co", pos)
        if head == -1 or head > len(str) - 4:
            break

        if str[head + 3] == "e":
            count += 1

        pos = head + 2

    return count


def count_code_walrus(str: str):
    """
    Parameters:
        str
    return the number of times the pattern "co.e" is in the input string
    """
    count = 0

    pos = -1
    while (pos := str.find("co", pos + 1)) != -1 and pos < len(str) - 3:
        if str[pos + 3] == "e":
            count += 1
            pos += 3
        else:
            pos += 1
    return count
