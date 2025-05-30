"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 5: Random Circles
- Draw 20 circles at random positions with random colors and sizes on the given canvas

implement the function draw_random_circle(canvas)
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

    # 1. do the actual job
    draw_random_circles(canvas)


def random_color():
    """Given function: pick a random color from a short selection"""
    colors = ["blue", "purple", "salmon", "lightblue", "cyan", "forestgreen"]
    return random.choice(colors)


def draw_random_circles(canvas):
    """
    2. draw circles on the canvas
    """
    for i in range(N_CIRCLES):
        draw_random_circle(canvas)


def draw_random_circle(canvas):
    """3. Draw a circle at random positions with random colors on the canvas"""
    x = random.randint(0, CANVAS_WIDTH)
    y = random.randint(0, CANVAS_HEIGHT)

    color = random_color()
    canvas.create_oval(x, y, x + CIRCLE_SIZE, y + CIRCLE_SIZE, color)
    print(f"A {color} circle in {x, y}, {x + CIRCLE_SIZE, y + CIRCLE_SIZE}")


if __name__ == "__main__":
    main()
