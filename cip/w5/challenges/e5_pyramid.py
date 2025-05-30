"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Week 5: Pyramid
--------------------
draw a pyramid of bricks arranged in horizontal rows
the number of bricks in each row decreases by one as you move up the pyramid
"""

from _graphics import Canvas

CANVAS_WIDTH = 600  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300  # Height of drawing canvas in pixels

BRICK_WIDTH = 30  # The width of each brick in pixels
BRICK_HEIGHT = 12  # The height of each brick in pixels
BRICKS_IN_BASE = 14  # The number of bricks in the base


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for i in range(BRICKS_IN_BASE):
        nr_bricks = BRICKS_IN_BASE - i
        delta = (CANVAS_WIDTH - nr_bricks * BRICK_WIDTH) // 2

        y_1 = CANVAS_HEIGHT - BRICK_HEIGHT * i
        y_0 = y_1 - BRICK_HEIGHT
        for j in range(nr_bricks):
            x_0 = delta + BRICK_WIDTH * j
            x_1 = x_0 + BRICK_WIDTH
            canvas.create_rectangle(x_0, y_0, x_1, y_1, "yellow", "black")


if __name__ == "__main__":
    main()
