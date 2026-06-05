"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Load and Blit Bitmaps
"""

FPS = 30

TITLE = "Load and Draw of Bitmaps"
WIN_SIZE = (600, 400)
WIN_POS = (10, 50)

BACKGROUND_COLOR = "white"

SPRITE_DELTA_Y = 10

ALIEN_IMAGE = "images/alien_big.png"
ALIEN_SIZE = (50, 45)
ALIEN_TRANSPARENT_COLOR = "black"
ALIEN_COUNT = 7
ALIEN_GAP = (WIN_SIZE[0] - ALIEN_COUNT * ALIEN_SIZE[0]) // (ALIEN_COUNT + 1)

DEFENDER_IMAGE = "images/defender.png"
DEFENDER_SIZE = (30, 30)
DEFENDER_POS = (
    (WIN_SIZE[0] - DEFENDER_SIZE[0]) // 2,  # center
    WIN_SIZE[1] - DEFENDER_SIZE[1] - SPRITE_DELTA_Y,  # bottom
)
