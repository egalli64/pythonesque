"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 4: Random Circles
- Draw up to 20 circles at random positions with random colors and sizes on a canvas

Extension 1: Random number of circles in [1 .. 20]
"""

from graphics import Canvas
import random

# canvas constants
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300

# circle constants
CIRCLE_SIZE = 20
N_CIRCLES = 20


def main():
    print("Random Circles")

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_random_circles(canvas)


def draw_random_circles(canvas):
    """
    EXTENSION 1: Draw a random number of circles in [1, N_CIRCLES] on the canvas
    """
    n_circles = random.randrange(N_CIRCLES) + 1
    print(f"{n_circles} circles")
    for i in range(n_circles):
        draw_random_circle(canvas)


def draw_random_circle(canvas):
    """3. Draw a circle at random positions with random colors on the canvas"""
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)

    color = random_color()
    canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, color)
    print(f"A {color} circle in {x, y}, {x + CIRCLE_SIZE, y + CIRCLE_SIZE}")


def random_color():
    """Pick a random color from a short selection"""
    colors = ["blue", "purple", "salmon", "lightblue", "cyan", "forestgreen"]
    return random.choice(colors)


if __name__ == "__main__":
    main()
