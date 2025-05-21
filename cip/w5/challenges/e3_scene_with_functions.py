"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Scene with Functions
---
Build a nature scene shown in an image (ungraded assignment)
"""

from _graphics import Canvas
import math

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 140, 10, "salmon")
    # M1: two more clouds
    draw_cloud(canvas, 30, 50, "pink")
    draw_cloud(canvas, 260, 30, "purple")
    # M2: three trees
    draw_tree(canvas, 30, 180, "green")
    draw_tree(canvas, 100, 180, "red")
    draw_tree(canvas, 300, 180, "orange")


def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in
    different values of x and y (the location of the cloud) and
    color (the color of the cloud).
    """
    cloud_bottom_start_y = y + (1 / 3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1 / 4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3 / 4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, cloud_bottom_start_y, x + (3 / 4) * CLOUD_WIDTH, cloud_bottom_end_y, color
    )
    canvas.create_oval(
        x + (1 / 4) * CLOUD_WIDTH,
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color,
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x, y, cloud_top_end_x, y + (2 / 3) * CLOUD_HEIGHT, color
    )


def draw_tree(canvas, x, y, color):
    """
    M2
    """
    x_b = x
    y_b = y
    sz_b = 50

    w_t = 20
    h_t = 50
    x_t = x + (sz_b // 2) - (w_t // 2)
    y_t = y + sz_b - 5

    canvas.create_rectangle(x_t, y_t, x_t + w_t, y_t + h_t, "brown")
    canvas.create_oval(x_b, y_b, x + sz_b, y + sz_b, color)


if __name__ == "__main__":
    main()
