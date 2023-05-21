"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 5: Scribble
- Mock for the graphic module internally used by Stanford
"""
import random


class Canvas(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'Mocking a {x, y} canvas')

    def create_oval(self, x0, y0, x1, y1, color):
        print(f'Mocking a {color} oval in {x0, y0}, {x1, y1}')

    def mainloop(self):
        print("Mocking main loop")

    def get_mouse_x(self):
        return random.randint(0, self.x)

    def get_mouse_y(self):
        return random.randint(0, self.y)
