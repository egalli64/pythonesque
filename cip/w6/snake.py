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
"""
from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

DELAY = 0.1


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    player = [0, 0, 'blue']
    target = [360, 360, 'red']
    direction = 'ArrowRight'

    player_id = place(canvas, player)
    target_id = place(canvas, target)

    while 0 <= player[0] < CANVAS_WIDTH and 0 <= player[1] < CANVAS_HEIGHT:
        key = canvas.get_last_key_press()
        if key != None:
            direction = key
        delta = move(canvas, player_id, direction)
        player[0] += delta[0]
        player[1] += delta[1]

        time.sleep(DELAY)


def move(canvas, id, direction):
    deltas = {'ArrowLeft': (-SIZE, 0), 'ArrowRight': (SIZE, 0),
              'ArrowUp': (0, -SIZE), 'ArrowDown': (0, SIZE)}

    delta = deltas[direction]
    canvas.move(id, *delta)
    return delta


def place(canvas, item):
    bot = (item[0] + SIZE, item[1] + SIZE)
    return canvas.create_rectangle(item[0], item[1], bot[0], bot[1], item[2])


if __name__ == '__main__':
    main()
