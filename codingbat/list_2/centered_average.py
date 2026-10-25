"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
centered_average: https://codingbat.com/prob/p126968
"""


def centered_average(nums: list[int]) -> int:
    """
    Parameters:
        nums an int list sized 3+
    return the centered average (truncated to int) of nums, ignoring the smallest and largest elements
    """
    return (sum(nums) - max(nums) - min(nums)) // (len(nums) - 2)
