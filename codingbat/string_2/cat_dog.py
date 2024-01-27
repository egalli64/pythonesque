"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 2: https://codingbat.com/python/String-2
cat_dog: https://codingbat.com/prob/p164876
"""


def cat_dog(str: str):
    """
    Parameters:
        str
    return True there is the same number of "cat" and "dog" in the input string
    """
    return str.count("cat") == str.count("dog")
