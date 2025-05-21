"""
Code in Place 2025 https://codeinplace.stanford.edu/cip5
My notes: https://github.com/egalli64/pythonesque/cip

Program: Rect Line Replay - for debugging practice
"""

import _graphics as graphics


def main():
    canvas = graphics.create_canvas(300, 300)

    for i in range(20):
        value = i * 10
        left_x = value
        top_y = value
        right_x = value + 10
        bottom_y = value + 10

        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, "blue")

        print(i)


if __name__ == "__main__":
    main()
