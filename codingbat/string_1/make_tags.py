"""
CodingBat Python track

Source: https://codingbat.com/python
My solutions: https://github.com/egalli64/pythonesque/codingbat

String 1: https://codingbat.com/python/String-1
make_tags: https://codingbat.com/prob/p132290
"""


def make_tags(tag, word):
    """
    Parameters:
        tag str
        word str
    return the generate HTML element for the passed tag having word as content
    """
    return "<" + tag + ">" + word + "</" + tag + ">"


def make_tags_f_str(tag, word):
    """
    Parameters:
        tag str
        word str
    return the generate HTML element for the passed tag having word as content
    """
    return f"<{tag}>{word}</{tag}>"
