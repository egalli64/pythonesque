"""
A 3D target - Creating a target Vector3

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

PLASMA_SPEED = 100  # meters per second

# two 3D points
a = pygame.Vector3(-6, 2, 2)
b = pygame.Vector3(7, 5, 10)
print(f"Point A{a}, point B{b}")

# a 3D vector
ab = b - a
print(f"Vector AB{ab}")

distance = ab.magnitude();
print("Distance from A to B is", distance)

direction = ab.normalize()
print("Direction to target is", direction)
