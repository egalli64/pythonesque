"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Diagnostic 5
"""
from graphics import Canvas


def main():
    # draws two cars
    canvas = Canvas(400, 400)
    x = 10
    y = 10
    draw_car()

    x = 100
    y = 100
    draw_car()


def draw_car(canvas, x, y):
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)


if __name__ == '__main__':
    main()
