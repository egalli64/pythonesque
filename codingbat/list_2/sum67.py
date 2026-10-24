"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque codingbat folder

List 2: https://codingbat.com/python/List-2
sum67: https://codingbat.com/prob/p108886
"""


def sum67(nums: list[int]) -> int:
    """
    Parameters:
        nums a possibly empty int list
    return sum of values in nums, skipping subsequences delimited by 6 and 7
    """
    result = 0
    sub_seq = False

    for num in nums:
        if num == 7 and sub_seq:
            sub_seq = False
        elif num == 6:
            sub_seq = True
        elif not sub_seq:
            result += num

    return result
