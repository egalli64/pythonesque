"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Section Week 2: Spread Beepers
- Custom world. Karel is on (1,1), facing east
- There is a pile of beepers on (2,1), Karel has to spread them out along the row
- Jeanine version
"""
from stanfordkarel import *


def main():
    take_and_place()
    turn_around()
    check_stack()
    turn_around()
    go_forward()
    turn_around()
    take_and_place()
    go_forward()
    final_stage()
    go_forward()
    check_again()


def take_and_place():
    move()
    if beepers_present():
        pick_beeper()
        move()

    # for i in range(1):
    if no_beepers_present():
        put_beeper()
    else:
        move()
        move()
        if no_beepers_present():
            put_beeper()


def check_stack():
    move()
    if beepers_present():
        pick_beeper()
        turn_around()
        move()
    if beepers_present():
        move()
        put_beeper()


def check_again():
    if facing_west():
        while front_is_blocked():
            turn_around()
            move()
            if beepers_present():
                pick_beeper()
                if no_beepers_present():
                    put_beeper()
                    turn_around()
                    move()
                    turn_around()
                else:
                    move()
                    while beepers_present():
                        move()
                    if no_beepers_present():
                        put_beeper()
                        turn_around()
                    while beepers_present():
                        move()


def final_stage():
    if facing_east():
        while front_is_blocked():
            turn_around()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def pick_up():
    move()
    if beepers_present():
        pick_beeper()
    while front_is_clear():
        move()
        put_beeper()


def go_forward():
    while front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program("exercise")
