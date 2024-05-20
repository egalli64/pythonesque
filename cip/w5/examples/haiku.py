"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Program: Haiku
"""

from _graphics import Canvas

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
X = 50
Y = 50
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
        y = Y + FONT_SIZE * i
        canvas.create_text(X, y, TEXT[i], FONT, FONT_SIZE, "blue")


if __name__ == "__main__":
    main()
