"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: THIS big!
"""

from _graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
THIS_BIG = 144
CENTER_X = 160
CENTER_Y = 160


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    canvas.create_rectangle(
        CENTER_X - THIS_BIG // 2,
        CENTER_Y - THIS_BIG // 2,
        CENTER_X + THIS_BIG // 2,
        CENTER_Y + THIS_BIG // 2,
    )


if __name__ == "__main__":
    main()
