"""
Vector2 multiplication and division - Assuming the objects are actually an algebraic vectors

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame

a = pygame.Vector2(10, 20)
b = pygame.Vector2(2, 4)
print(f"A is {a} and B is {b}")

# scalar multiplication
print("A * 5 is", a * 5)

# vector dot product
print("A * B is", a * b)

# component-wise multiplication
print("Element-wise A * B is", a.elementwise() * b)

# scalar division
print("A / 5 is", a / 5)

# component-wise division
print("Element-wise A / B is", a.elementwise() / b)
