"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Centered Square
"""

from _graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
SQUARE_SIZE = 100


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    middle = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
    top = middle[0] - SQUARE_SIZE // 2, middle[1] - SQUARE_SIZE // 2
    bottom = top[0] + SQUARE_SIZE, top[1] + SQUARE_SIZE

    canvas.create_rectangle(top[0], top[1], bottom[0], bottom[1], "blue")


if __name__ == "__main__":
    main()
