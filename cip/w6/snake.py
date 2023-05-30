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
"""
from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
LAST_X = CANVAS_WIDTH - SIZE
LAST_Y = CANVAS_HEIGHT - SIZE

DELAY = 0.1


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    player = [0, 0, 'blue']
    target = [360, 360, 'red']

    player_id = place(canvas, player)
    target_id = place(canvas, target)

    while player[0] < LAST_X and player[1] < LAST_Y:
        time.sleep(DELAY)
        canvas.move(player_id, SIZE, 0)
        player[0] += SIZE


def place(canvas, top):
    bot = (top[0] + SIZE, top[1] + SIZE)
    return canvas.create_rectangle(top[0], top[1], bot[0], bot[1], top[2])


if __name__ == '__main__':
    main()
