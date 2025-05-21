"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Exploring Colors
"""

from _graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CENTER = CANVAS_WIDTH // 2


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # a red circle
    red = "#990000"
    canvas.create_oval(25, 25, 175, 175, color=red)

    # a plus sign
    canvas.create_line(190, 100, 210, 100)
    canvas.create_line(200, 90, 200, 110)

    # a blue circle
    blue = "#000099"
    canvas.create_oval(CENTER + 25, 25, CENTER + 175, 175, color=blue)

    # an arrow
    canvas.create_line(200, 170, 200, 210)
    canvas.create_line(200, 210, 190, 190)
    canvas.create_line(200, 210, 210, 190)

    # a purple circle
    purple = "#990099"
    canvas.create_oval(CENTER - 75, 225, CENTER + 75, 375, purple)


if __name__ == "__main__":
    main()
