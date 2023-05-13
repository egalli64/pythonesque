"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 4: Random Circles
- Draw up to 20 circles at random positions with random colors and sizes on a canvas
"""
from graphics import Canvas
import random

# canvas constants
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300

# circle constants
SIZE = 40
N_CIRCLES = 20


def main():
    # 1. create a canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # 2. do the actual job on it
    draw_random_circles(canvas)


def draw_random_circles(canvas):
    """Draw a random number of circles in [1, N_CIRCLES] on the canvas"""
    n_circles = random.randrange(1, N_CIRCLES + 1)
    print(f'{n_circles} circles')
    for i in range(n_circles):
        draw_random_circle(canvas)


def draw_random_circle(canvas):
    """Draw a circle with size in [2, SIZE], in a random position on the canvas (fully visible), with a random color"""
    size = random.randrange(2, SIZE + 1)
    x = random.randint(0, CANVAS_WIDTH - size)
    y = random.randint(0, CANVAS_HEIGHT - size)
    color = random_color()
    canvas.create_oval(x, y, x + size, y + size, color)
    print(f'A {color} circle in {x, y}, {x + size, y + size}')


def random_color():
    """Pick a random color from a short selection"""
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)


if __name__ == '__main__':
    main()
