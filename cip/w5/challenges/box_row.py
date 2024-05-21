"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Program: Box Row
---
Create a row of boxes on the canvas bottom
"""

from _graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH // N_BOXES


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    y0 = CANVAS_HEIGHT - BOX_SIZE
    for i in range(N_BOXES):
        x0 = BOX_SIZE * i
        x1 = BOX_SIZE * (i + 1)
        canvas.create_rectangle(x0, y0, x1, CANVAS_HEIGHT, "white", "black")


if __name__ == "__main__":
    main()
