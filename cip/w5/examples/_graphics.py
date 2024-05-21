"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 4: Random Circles
- Mock for the graphic module internally used by Stanford
"""

def create_canvas(x, y):
    return Canvas(x, y)

class Canvas(object):
    def __init__(self, x, y):
        print(f"Mock {x, y} canvas")

    def create_oval(self, x0, y0, x1, y1, color):
        print(f"Mock {color} oval in {x0, y0}, {x1, y1}")

    def create_rectangle(self, x0, y0, x1, y1, color="black"):
        print(f"Mock {color} rectangle in {x0, y0}, {x1, y1}")

    def create_line(self, x0, y0, x1, y1):
        print(f"Mock line from {x0, y0} to {x1, y1}")

    def create_text(self, x, y, text, font, font_size, color):
        print(f"Mock text from {x, y} for '{text}', font {font} {font_size} {color}")

    def create_image(self, x, y, filename):
        print(f"Mock image from {x, y} for {filename}")

    def get_mouse_x(self):
        print("Mock x mouse position")
        return 42

    def get_mouse_y(self):
        print("Mock y mouse position")
        return 24
