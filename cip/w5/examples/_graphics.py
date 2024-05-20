"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 4: Random Circles
- Mock for the graphic module internally used by Stanford
"""


class Canvas(object):
    def __init__(self, x, y):
        print(f"Mocking a {x, y} canvas")

    def create_oval(self, x0, y0, x1, y1, color):
        print(f"Mocking a {color} oval in {x0, y0}, {x1, y1}")

    def create_rectangle(self, x0, y0, x1, y1, color):
        print(f"Mocking a {color} rectangle in {x0, y0}, {x1, y1}")

    def create_line(self, x0, y0, x1, y1):
        print(f"Mocking a line from {x0, y0} to {x1, y1}")

    def create_text(self, x, y, text, color, font, font_size):
        print(f"Mocking a line from {x, y} for '{text}', in color {color}, font {font} {font_size}")
