"""
Algebraic vector with Vector2 - Calculate direction from point A to point B

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

# two points
point_a = pygame.Vector2(10, 20)
point_b = pygame.Vector2(30, 35)
print("Two points:", point_a, point_b)

# algebraic vector
vector_ab = point_b - point_a
print("Vector AB:", vector_ab)  # (20, 15)

vector_ba = point_a - point_b
print("Vector BA:", vector_ba)  # (-20, -15)
