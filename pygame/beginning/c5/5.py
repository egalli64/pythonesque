"""
Vector2 - represent a couple of values used for position, displacement, direction, velocity, ...

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame
import math

# by default a [0, 0] Vector2 is generated
print(pygame.Vector2())

# if a single value is passed, both components are initialized with it
print(pygame.Vector2(math.pi))

# a vector2 from a couple of values
print(pygame.Vector2(3, 5))

# a vector2 from a tuple
a_tuple = (6, 2)
v2 = pygame.Vector2(a_tuple)
print(a_tuple, v2)
