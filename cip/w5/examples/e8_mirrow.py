"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Mirror, mirror on the ... canvas
"""

from _graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Create mirror line
    canvas.create_line(CANVAS_WIDTH // 2, 0, CANVAS_WIDTH // 2, CANVAS_HEIGHT)

    # Create red rectangle
    rect_left_x = 20
    rect_top_y = 50
    rect_width = 100
    rect_height = 200
    canvas.create_rectangle(
        rect_left_x,
        rect_top_y,
        rect_left_x + rect_width,
        rect_top_y + rect_height,
        "red",
    )

    # mirror
    m_x_1 = CANVAS_WIDTH - rect_left_x - rect_width
    m_x_2 = CANVAS_WIDTH - rect_left_x
    canvas.create_rectangle(m_x_1, rect_top_y, m_x_2, rect_top_y + rect_height, "blue")


if __name__ == "__main__":
    main()
