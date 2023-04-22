"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 9: Painting corners
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter9.html
"""
from stanfordkarel import *


def main():
    # The available colors for a corner
    colors = [BLACK, BLUE, CYAN, DARK_GRAY, GRAY, GREEN, LIGHT_GRAY,
              MAGENTA, ORANGE, PINK, RED, WHITE, YELLOW]

    # Move around on the first row an paint the current corner
    for color in colors:
        paint_corner(color)
        if front_is_blocked():
            turn_left()
            turn_left()
        if front_is_clear():
            move()

    if corner_color_is(BLUE):
        print("Karel is on a blue corner")

    while front_is_clear():
        move()
    turn_left()
    turn_left()
    paint_corner(WHITE)


if __name__ == '__main__':
    run_karel_program()
