"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 4: Random Circles
- Mock for the graphic module internally used by Stanford
"""


class Canvas(object):
    def __init__(self, x, y):
        print(f'Mocking a {x, y} canvas')

    def create_oval(self, x0, y0, x1, y1, color):
        print(f'Mocking a {color} oval in {x0, y0}, {x1, y1}')
