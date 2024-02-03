"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
xyz_there: https://codingbat.com/prob/p149391
"""


def xyz_there(str: str):
    """
    Parameters:
        str
    Return True if str contains "xyz" _not_ preceded by "."
    """
    start = 0
    while True:
        pos = str.find("xyz", start)

        if pos == -1:
            return False
        elif pos == 0 or str[pos - 1] != ".":
            return True

        start = pos + 1


def xyz_there_walrus(str: str):
    """
    Parameters:
        str
    Return True if str contains "xyz" _not_ preceded by "."
    """
    start = 0
    while (pos := str.find("xyz", start)) != -1:
        if pos == 0 or str[pos - 1] != ".":
            return True

        start = pos + 1

    return False
