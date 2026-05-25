"""
Normalized Vector2 - Assuming the object is actually an algebraic vector

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

a = pygame.Vector2(10.0, 20.0)
b = pygame.Vector2(30.0, 35.0)
print(f"A is {a} and B is {b}")

ab = b - a
print("Vector AB is", ab)

print("Magnitude of AB is", ab.magnitude())
print("AB normalized is", ab.normalize())
print("AB is still", ab)

ab.normalize_ip()
print("AB normalized (in place) is", ab)
