"""
Linear interpolation

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""


def lerp(a, b, factor):
    """Linear interpolation between a and b, the factor is in [0, 1]"""
    return a + (b - a) * factor


print(lerp(100, 200, 0.0))
print(lerp(100, 200, 0.25))
print(lerp(100, 200, 0.5))
print(lerp(100, 200, 0.75))
print(lerp(100, 200, 1.0))
