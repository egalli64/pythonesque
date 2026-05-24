"""
Vector2 addition - Assuming the object is actually an algebraic vector

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

# three points
a = pygame.Vector2(10.0, 20.0)
b = pygame.Vector2(30.0, 35.0)
c = pygame.Vector2(15.0, 45.0)
print(f"A is {a}, B is {b}, and C is {c}")

# three vectors
ab = b - a
bc = c - b
ac = c - a
print(f"Vector AB is {ab}, BC is {bc}, and AC is {ac}")

ac_as_sum = ab + bc
print(f"AB + BC is {ac_as_sum}, same as AC = {ac}")


print("Magnitude of AC is", ac.magnitude())
print("AC normalized is", ac.normalize())
