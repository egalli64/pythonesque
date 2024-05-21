"""
Code in Place 2024 https://codeinplace.stanford.edu/cip4
My notes: https://github.com/egalli64/pythonesque/cip

Week 5: Quilt
--------------------
Draw circles and squares that fill the patches at the provided location
"""

from _graphics import Canvas

# each patch is a square with this width and height:
PATCH_SIZE = 100
CANVAS_WIDTH = PATCH_SIZE * 4
CANVAS_HEIGHT = PATCH_SIZE * 2


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # draw the first row of patches
    draw_square_patch(canvas, 0, 0)
    draw_circle_patch(canvas, PATCH_SIZE, 0)
    draw_square_patch(canvas, PATCH_SIZE * 2, 0)
    draw_circle_patch(canvas, PATCH_SIZE * 3, 0)

    # milestone 1: draw the second row of patches
    draw_circle_patch(canvas, 0, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE, PATCH_SIZE)
    draw_circle_patch(canvas, PATCH_SIZE * 2, PATCH_SIZE)
    draw_square_patch(canvas, PATCH_SIZE * 3, PATCH_SIZE)


def draw_circle_patch(canvas, start_x, start_y):
    # milestone 2
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    canvas.create_oval(start_x, start_y, end_x, end_y, "salmon")


def draw_square_patch(canvas, start_x, start_y):
    # draws a purple frame at (start_x, start_y)
    end_x = start_x + PATCH_SIZE
    end_y = start_y + PATCH_SIZE
    inset = 20
    # first draw a purple square over the entire patch
    canvas.create_rectangle(start_x, start_y, end_x, end_y, "purple")
    # then draw a smaller white square on top
    canvas.create_rectangle(
        start_x + inset, start_y + inset, end_x - inset, end_y - inset, "white"
    )


if __name__ == "__main__":
    main()
