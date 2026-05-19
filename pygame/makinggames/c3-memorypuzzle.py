"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames
"""

import random
import pygame
import sys

# frame setup (usually FPS is at least 60)
FPS = 15

# screen size (in pixel)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# speed boxes' sliding reveals and covers
REVEAL_SPEED = 8

# the board is structured in a even number of squared boxes with gaps between boxes
BOX_SIZE = 40
GAP_SIZE = 10
N_COLS = 6
N_ROWS = 3
assert (N_COLS * N_ROWS) % 2 == 0, "Even number of boxes expected"

X_MARGIN = int((SCREEN_WIDTH - (N_COLS * (BOX_SIZE + GAP_SIZE))) / 2)
Y_MARGIN = int((SCREEN_HEIGHT - (N_ROWS * (BOX_SIZE + GAP_SIZE))) / 2)

# colors - RGB format
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
COLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)

BG_COLOR = NAVYBLUE
LIGHT_BG_COLOR = GRAY
BOX_COLOR = WHITE
HIGHLIGHT_COLOR = BLUE

# shapes - what the player sees
DONUT = "donut"
SQUARE = "square"
DIAMOND = "diamond"
LINES = "lines"
OVAL = "oval"
SHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

assert (
    len(COLORS) * len(SHAPES) * 2 >= N_COLS * N_ROWS
), "Board is too big for given shapes/colors"


def main():
    global clock, screen
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # mouse coordinates
    mouse_x = 0
    mouse_y = 0
    pygame.display.set_caption("Memory Game")

    board = build_board()
    visible_cards = build_cards_visibility(False)

    # stores the (x, y) of the first box clicked
    firstSelection = None

    screen.fill(BG_COLOR)
    startGameAnimation(board)

    while True:  # main game loop
        mouseClicked = False

        screen.fill(BG_COLOR)  # drawing the window
        drawBoard(board, visible_cards)

        for event in pygame.event.get():  # event handling loop
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mouse_x, mouse_y)
        if boxx != None and boxy != None:
            # The mouse is currently over a box.
            if not visible_cards[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not visible_cards[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(board, [(boxx, boxy)])
                visible_cards[boxx][boxy] = True  # set the box as "revealed"
                if firstSelection == None:  # the current box was the first box clicked
                    firstSelection = (boxx, boxy)
                else:  # the current box was the second box clicked
                    # Check if there is a match between the two icons.
                    icon1shape, icon1color = getShapeAndColor(
                        board, firstSelection[0], firstSelection[1]
                    )
                    icon2shape, icon2color = getShapeAndColor(board, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Icons don't match. Re-cover up both selections.
                        pygame.time.wait(1000)  # 1000 milliseconds = 1 sec
                        coverBoxesAnimation(
                            board,
                            [(firstSelection[0], firstSelection[1]), (boxx, boxy)],
                        )
                        visible_cards[firstSelection[0]][firstSelection[1]] = False
                        visible_cards[boxx][boxy] = False
                    elif hasWon(visible_cards):  # check if all pairs found
                        gameWonAnimation(board)
                        pygame.time.wait(2000)

                        # Reset the board
                        board = build_board()
                        visible_cards = build_cards_visibility(False)

                        # Show the fully unrevealed board for a second.
                        drawBoard(board, visible_cards)
                        pygame.display.flip()
                        pygame.time.wait(1000)

                        # Replay the start game animation.
                        startGameAnimation(board)
                    firstSelection = None  # reset firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.flip()
        clock.tick(FPS)


def build_cards_visibility(x: bool):
    """
    Build a col-row list for the cards visibility

    Notice that, following the original code, the resulting order is inverted:
    given N_COLS = 2 and N_ROWS = 4, a list with 2 lines of 4 items is returned
    """
    return [[x] * N_ROWS for _ in range(N_COLS)]


def build_board():
    """
    Build a shuffled col-row list that could contain any possible shape in any possible color

    Notice that, following the original code, the board is inverted:
    given N_COLS = 2 and N_ROWS = 4, a list with 2 lines of 4 items is returned
    """
    items = [(shape, color) for color in COLORS for shape in SHAPES]
    random.shuffle(items)

    # take just the required ones
    count = N_COLS * N_ROWS // 2
    items = items[:count] * 2
    random.shuffle(items)

    return [items[i : i + N_ROWS] for i in range(0, len(items), N_ROWS)]


def splitIntoGroupsOf(groupSize, theList):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i : i + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOX_SIZE + GAP_SIZE) + X_MARGIN
    top = boxy * (BOX_SIZE + GAP_SIZE) + Y_MARGIN
    return (left, top)


def getBoxAtPixel(x, y):
    for boxx in range(N_COLS):
        for boxy in range(N_ROWS):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOX_SIZE, BOX_SIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOX_SIZE * 0.25)  # syntactic sugar
    half = int(BOX_SIZE * 0.5)  # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy)  # get pixel coords from board coords
    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(screen, color, (left + half, top + half), half - 5)
        pygame.draw.circle(screen, BG_COLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(
            screen,
            color,
            (left + quarter, top + quarter, BOX_SIZE - half, BOX_SIZE - half),
        )
    elif shape == DIAMOND:
        pygame.draw.polygon(
            screen,
            color,
            (
                (left + half, top),
                (left + BOX_SIZE - 1, top + half),
                (left + half, top + BOX_SIZE - 1),
                (left, top + half),
            ),
        )
    elif shape == LINES:
        for i in range(0, BOX_SIZE, 4):
            pygame.draw.line(screen, color, (left, top + i), (left + i, top))
            pygame.draw.line(
                screen,
                color,
                (left + i, top + BOX_SIZE - 1),
                (left + BOX_SIZE - 1, top + i),
            )
    elif shape == OVAL:
        pygame.draw.ellipse(screen, color, (left, top + quarter, BOX_SIZE, half))


def getShapeAndColor(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(screen, BG_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0:  # only draw the cover if there is an coverage
            pygame.draw.rect(screen, BOX_COLOR, (left, top, coverage, BOX_SIZE))
    pygame.display.flip()
    clock.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):
    # Do the "box reveal" animation.
    for coverage in range(BOX_SIZE, (-REVEAL_SPEED) - 1, -REVEAL_SPEED):
        drawBoxCovers(board, boxesToReveal, coverage)


def coverBoxesAnimation(board, boxesToCover):
    # Do the "box cover" animation.
    for coverage in range(0, BOX_SIZE + REVEAL_SPEED, REVEAL_SPEED):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(N_COLS):
        for boxy in range(N_ROWS):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(screen, BOX_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(
        screen,
        HIGHLIGHT_COLOR,
        (left - 5, top - 5, BOX_SIZE + 10, BOX_SIZE + 10),
        4,
    )


def startGameAnimation(board):
    # Randomly reveal the boxes 8 at a time.
    coveredBoxes = build_cards_visibility(False)
    boxes = []
    for x in range(N_COLS):
        for y in range(N_ROWS):
            boxes.append((x, y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)


def gameWonAnimation(board):
    # flash the background color when the player has won
    coveredBoxes = build_cards_visibility(True)
    color1 = LIGHT_BG_COLOR
    color2 = BG_COLOR

    for i in range(13):
        color1, color2 = color2, color1  # swap colors
        screen.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.flip()
        pygame.time.wait(300)


def hasWon(revealedBoxes):
    # Returns True if all the boxes have been revealed, otherwise False
    for i in revealedBoxes:
        if False in i:
            return False  # return False if any boxes are covered.
    return True


if __name__ == "__main__":
    main()
