"""
Vector2 magnitude - Assuming the object is actually an algebraic vector

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

a = pygame.Vector2(10.0, 20.0)
b = pygame.Vector2(30.0, 35.0)

# vector from a to b: [20, 15]
ab = b - a
# its magnitude is 25
print(ab, ab.magnitude())
