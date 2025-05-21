"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Draw Flag (Indonesia)
"""

from _graphics import Canvas

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT // 2, "red")


if __name__ == "__main__":
    main()
