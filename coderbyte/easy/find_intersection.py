"""
Coder-byte Challenges

Source: https://coderbyte.com/challenges
My solutions: https://github.com/egalli64/pythonesque coderbyte folder

Find Intersection
"""


def find_intersection(str_arr: list[str]):
    """
    Given an array of two strings, find the intersection of all the elements in it.
    Each element in the array represents a list of comma-separated numbers sorted in ascending order.
    Return a string representing the intersection, keeping the original order. Or "false", for empty intersection.
    """
    left = set(str_arr[0].split(", "))
    right = set(str_arr[1].split(", "))

    xs = left & right
    if xs:
        buffer = sorted([int(x) for x in xs])
        result = [str(x) for x in buffer]

        return ",".join(result)
    else:
        return "false"
