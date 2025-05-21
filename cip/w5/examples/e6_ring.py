"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Ring ring!
---
Create a red ring on the white canvas
"""

from _graphics import Canvas

CANVAS_WIDTH = 150
CANVAS_HEIGHT = 150

# the diameter of the outer red circle
OUTER_DIAMETER = 50
# the left and top coordinates of the outer red circle
OUTER_LEFT_X = (CANVAS_WIDTH - OUTER_DIAMETER) / 2
OUTER_TOP_Y = (CANVAS_HEIGHT - OUTER_DIAMETER) / 2
# the size of the red band of the ring
# inner_left_x = outer_left_x + RING_WIDTH
RING_WIDTH = 10


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    x_0 = OUTER_LEFT_X
    y_0 = OUTER_TOP_Y
    x_1 = OUTER_LEFT_X + OUTER_DIAMETER
    y_1 = OUTER_TOP_Y + OUTER_DIAMETER
    canvas.create_oval(x_0, y_0, x_1, y_1, "red")

    x_0 = OUTER_LEFT_X + RING_WIDTH
    y_0 = OUTER_TOP_Y + RING_WIDTH
    x_1 = OUTER_LEFT_X + OUTER_DIAMETER - RING_WIDTH
    y_1 = OUTER_TOP_Y + OUTER_DIAMETER - RING_WIDTH
    canvas.create_oval(x_0, y_0, x_1, y_1, "white")


if __name__ == "__main__":
    main()
