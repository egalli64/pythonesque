"""
Linear interpolation

From: Beginning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque folder pygame/beginning
"""


def lerp(a: int, b: int, factor: float):
    """Linear interpolation between a and b, the factor is in [0, 1]"""
    return a + (b - a) * factor


print(lerp(100, 200, 0.0))
print(lerp(100, 200, 0.25))
print(lerp(100, 200, 0.5))
print(lerp(100, 200, 0.75))
print(lerp(100, 200, 1.0))
