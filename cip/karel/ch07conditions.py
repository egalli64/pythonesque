"""
Karel the Robot - Learns Python

Source: https://compedu.stanford.edu/karel-reader/docs/python/en/intro.html
My notes: https://github.com/egalli64/pythonesque/cip/karel

Chapter 7: Karel Conditions
https://compedu.stanford.edu/karel-reader/docs/python/en/chapter7.html
"""
from stanfordkarel import *


def main():
    """Show Karel conditional functions in action"""

    # 1 - Is there a wall in front of Karel?
    print('1a - front_is_clear(): ', end='')
    if front_is_clear():
        print('OK')
    else:
        print('Unexpected')

    print('1b - front_is_blocked(): ', end='')
    turn_back()
    if front_is_blocked():
        print('OK')
    else:
        print('Unexpected')

    # 2 - Are there beepers on this corner?
    print('2a - beepers_present(): ', end='')
    turn_back()
    move()
    if beepers_present():
        print('OK')
    else:
        print('Unexpected')

    print('2b - no_beepers_present(): ', end='')
    move()
    if no_beepers_present():
        print('OK')
    else:
        print('Unexpected')

    # 3 - Is there a wall to Karel’s left?
    print('3a - left_is_clear(): ', end='')
    if left_is_clear():
        print('OK')
    else:
        print('Unexpected')

    print('3b - left_is_blocked(): ', end='')
    turn_back()
    if left_is_blocked():
        print('OK')
    else:
        print('Unexpected')

    # 4 - Is there a wall to Karel’s right?
    print('4a - right_is_clear(): ', end='')
    if right_is_clear():
        print('OK')
    else:
        print('Unexpected')

    print('4b - right_is_blocked(): ', end='')
    turn_back()
    if right_is_blocked():
        print('OK')
    else:
        print('Unexpected')

    # 5 - Does Karel have any beepers in its bag?
    print('5a - beepers_in_bag(): ', end='')
    if beepers_in_bag():
        print('OK')
    else:
        print('Unexpected')

    print('5b - no_beepers_in_bag(): ', end='')
    if no_beepers_in_bag():
        print('Unexpected')
    else:
        print('OK')

    # 6 - Is Karel facing north?
    print('6a - facing_north(): ', end='')
    turn_left()
    if facing_north():
        print('OK')
    else:
        print('Unexpected')

    print('6b - not_facing_north(): ', end='')
    turn_back()
    if not_facing_north():
        print('OK')
    else:
        print('Unexpected')

    # 7 - Is Karel facing south?
    print('7a - facing_south(): ', end='')
    if facing_south():
        print('OK')
    else:
        print('Unexpected')

    print('7b - not_facing_south(): ', end='')
    turn_left()
    if not_facing_south():
        print('OK')
    else:
        print('Unexpected')

    # 8 - Is Karel facing east?
    print('8a - facing_east(): ', end='')
    if facing_east():
        print('OK')
    else:
        print('Unexpected')

    print('8b - not_facing_east(): ', end='')
    turn_back()
    if not_facing_east():
        print('OK')
    else:
        print('Unexpected')

    # 9 - Is Karel facing west?
    print('9a - facing_west(): ', end='')
    if facing_west():
        print('OK')
    else:
        print('Unexpected')

    print('9b - not_facing_west(): ', end='')
    turn_back()
    if not_facing_west():
        print('OK')
    else:
        print('Unexpected')


def turn_back():
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program("cip_ch07")
