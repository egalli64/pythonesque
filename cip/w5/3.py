"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Diagnostic 3

Write a program that has Karel draw four small "waves". Each wave is a triangle made up of three beepers. There is a gap between each wave.
"""
from stanfordkarel import *


def main():
    while front_is_clear():
        make_wave()
        if front_is_clear():
            move()
            move()


def make_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    turn_left()


# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
