"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 4: Random Circles
- Draw up to 20 circles at random positions with random colors and sizes on a canvas

implement the function draw_random_circle(canvas)
"""

from graphics import Canvas
import random

# canvas constants
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300

# circle constants
SIZE = 20
N_CIRCLES = 20


def main():
    print("Random Circles")

    # 1. create a canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # 2. do the actual job on it
    draw_random_circles(canvas)


def draw_random_circles(canvas):
    # EXTENSION 1: Draw a random number of circles in [1, N_CIRCLES] on the canvas
    # n_circles = random.randrange(N_CIRCLES) + 1
    # print(f"{n_circles} circles")
    # for i in range(n_circles):

    for i in range(N_CIRCLES):
        draw_random_circle(canvas)


def draw_random_circle(canvas):
    """Draw a circle at random positions with random colors on the canvas"""
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)

    # EXTENSION 2: random size (at least 2 point, max is SIZE)
    # size = random.randrange(1, SIZE) + 1
    # x = random.randint(0, CANVAS_WIDTH - size)
    # y = random.randint(0, CANVAS_HEIGHT - size)

    color = random_color()
    canvas.create_oval(x, y, x + SIZE, y + SIZE, color)
    print(f"A {color} circle in {x, y}, {x + SIZE, y + SIZE}")

    # EXTENSION 2: put the circle on the canvas
    # canvas.create_oval(x, y, x + size, y + size, color)
    # print(f"A {color} circle in {x, y}, {x + size, y + size}")


def random_color():
    """Pick a random color from a short selection"""
    colors = ["blue", "purple", "salmon", "lightblue", "cyan", "forestgreen"]
    return random.choice(colors)


if __name__ == "__main__":
    main()
