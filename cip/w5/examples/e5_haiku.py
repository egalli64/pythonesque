"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Haiku
"""

from _graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
FIRST_LINE_LEFT_X = 50
FIRST_LINE_TOP_Y = 50
FONT_SIZE = 24
FONT = "Courier"
TEXT = [
    "An old silent pond...",
    "A frog jumps into the pond,",
    "splash! Silence again.",
]


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for i in range(3):
        y = FIRST_LINE_TOP_Y + FONT_SIZE * i
        canvas.create_text(FIRST_LINE_LEFT_X, y, TEXT[i], FONT, FONT_SIZE, "blue")


if __name__ == "__main__":
    main()
