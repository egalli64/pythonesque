"""
Code in Place 2023 https://codeinplace.stanford.edu/cip3
My notes: https://github.com/egalli64/pythonesque/cip

Week 6: Baby Snake

Milestone #1: Set up the World
a blue square is the "player" the red square is the "goal". The player and the goal are both 20 pixels by 20 pixels. 
The player starts in the top left corner of the world.
The goal could be anywhere, as long as its x and y values are both multiplies of 20 e.g.: (360, 360)

Milestone #2: Animate
Each time through the animation loop you should move your player 20 pixels (this size of the player) in the direction it is traveling.
The directions are either left, right, up or down.
At the start the player should be traveling to the right

Milestone #3: Handle Key Press
The direction that the player is traveling can either be Left, Right, Up or Down and should be controlled by the keyboard.

Milestone #4: Detecting collisions
If the player goes out of bounds, the game is over. Write code that checks for, and handles, out of bounds cases.
"""
from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

DELAY = 0.1


def main():
    player_info = [0, 0, 'blue']
    target_info = [360, 360, 'red']

    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    direction = 'ArrowRight'

    player = place(canvas, player_info)
    target = place(canvas, target_info)

    while 0 <= player_info[0] < CANVAS_WIDTH and 0 <= player_info[1] < CANVAS_HEIGHT:
        key = canvas.get_last_key_press()
        if key != None:
            direction = key
        move(canvas, player, direction)

        player_info[0] = canvas.get_left_x(player)
        player_info[1] = canvas.get_top_y(player)

        time.sleep(DELAY)


def move(canvas, id, direction):
    deltas = {'ArrowLeft': (-SIZE, 0), 'ArrowRight': (SIZE, 0),
              'ArrowUp': (0, -SIZE), 'ArrowDown': (0, SIZE)}
    canvas.move(id, *deltas[direction])


def place(canvas, item):
    bot = (item[0] + SIZE, item[1] + SIZE)
    return canvas.create_rectangle(item[0], item[1], bot[0], bot[1], item[2])


if __name__ == '__main__':
    main()
