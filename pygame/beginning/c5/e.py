"""
Calculating positions - Stepping through the path from A to B

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

a = pygame.Vector2(10, 20)
b = pygame.Vector2(30, 35)
print("Points:", a, b)

ab = b - a
print("Vector AB:", ab)

step = ab / 10
print(f"Stepping by {step} from A to B", end=": ")

pos = a
for n in range(10):
    pos += step
    print(pos, end=" ")
print()
