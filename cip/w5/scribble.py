"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 5: Scribble
- Draw a circle wherever the mouse is located on the screen
"""
from graphics import Canvas
import time

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 1


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    while True:
        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()

        if 0 <= x <= CANVAS_WIDTH and 0 <= y <= CANVAS_HEIGHT:
            canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, 'cyan')

        canvas.mainloop()
        time.sleep(DELAY)


if __name__ == "__main__":
    main()
