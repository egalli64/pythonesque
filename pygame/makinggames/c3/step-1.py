"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 1: place cards on the board
"""

import random
import pygame
from enum import Enum, auto

# timing
FPS = 30
CHEAT_TIME = 2000

# screen constants: size (in pixel), title
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Memory Game"

# constants for placing the cards on the screen
N_ROWS = 4
N_COLS = 5

BOX_SIZE = 40
GAP_SIZE = 10

X_MARGIN = (SCREEN_WIDTH - (N_COLS * (BOX_SIZE + GAP_SIZE))) // 2
Y_MARGIN = (SCREEN_HEIGHT - (N_ROWS * (BOX_SIZE + GAP_SIZE))) // 2


class GameColor:
    """Colors used in the game (not in the cards)"""

    BOX = (255, 255, 255)  # white
    BACKGROUND = (60, 60, 100)  # navy blue


class Color(Enum):
    """Colors showed on cards"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)


class Image(Enum):
    """Images showed on cards"""

    DONUT = auto()
    SQUARE = auto()
    DIAMOND = auto()
    LINES = auto()
    OVAL = auto()


class Game:
    def __init__(self) -> None:
        """Initialize pygame and then the actual game"""
        pygame.init()
        pygame.display.set_caption(SCREEN_TITLE)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.board = self.build_board()
        self.status = self.build_cards_visibility(False)

    def flash_cards(self):
        """Show all the cards for a couple of seconds"""
        self.clock.tick(FPS)
        self.screen.fill(GameColor.BACKGROUND)

        self.draw_board(True)

        pygame.display.update()
        pygame.time.wait(CHEAT_TIME)

    def show_cards(self):
        """Show the visible cards, or their back"""
        self.clock.tick(FPS)
        self.screen.fill(GameColor.BACKGROUND)

        self.draw_board()

        pygame.display.update()

    def run(self):
        """Run he main game loop"""
        self.flash_cards()

        running = True
        while running:
            self.show_cards()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE
                ):
                    running = False

            pygame.display.update()

        pygame.quit()

    def get_xy(self, i: int, j: int):
        """
        Convert position on board to pixel coordinates for the left-top corner

        For example: i = 0, j = 0 -> (270, 140); i = 0, j = 1 -> (320, 140)
        """
        x = j * (BOX_SIZE + GAP_SIZE) + X_MARGIN
        y = i * (BOX_SIZE + GAP_SIZE) + Y_MARGIN
        return x, y

    def get_card_info(self, i: int, j: int):
        """Get image and color for the (i, j) card"""
        return self.board[i][j][0], self.board[i][j][1]

    def build_cards_visibility(self, x: bool):
        """Build a card visibility matrix (True for visible)"""
        return [[x] * N_COLS for _ in range(N_ROWS)]

    def draw_card(self, image: Image, color: Color, x: int, y: int):
        """Draw the image/color card from the top-left position x, y"""
        QUARTER = BOX_SIZE // 4
        HALF = BOX_SIZE // 2

        if image == Image.DONUT:
            center = (x + HALF, y + HALF)
            pygame.draw.circle(self.screen, color.value, center, HALF - 5)
            pygame.draw.circle(self.screen, GameColor.BACKGROUND, center, QUARTER - 5)
        elif image == Image.SQUARE:
            area = (x + QUARTER, y + QUARTER, HALF, HALF)
            pygame.draw.rect(self.screen, color.value, area)
        elif image == Image.DIAMOND:
            area = (
                (x + HALF, y),
                (x + BOX_SIZE - 1, y + HALF),
                (x + HALF, y + BOX_SIZE - 1),
                (x, y + HALF),
            )
            pygame.draw.polygon(self.screen, color.value, area)
        elif image == Image.LINES:
            for i in range(0, BOX_SIZE, 4):
                start_end = (x, y + i), (x + i, y)
                pygame.draw.line(self.screen, color.value, *start_end)
                start_end = (x + i, y + BOX_SIZE - 1), (x + BOX_SIZE - 1, y + i)
                pygame.draw.line(self.screen, color.value, *start_end)
        elif image == Image.OVAL:
            area = (x, y + QUARTER, BOX_SIZE, HALF)
            pygame.draw.ellipse(self.screen, color.value, area)

    def draw_back_card(self, x, y):
        """Draw the card back in the given position"""
        pygame.draw.rect(self.screen, GameColor.BOX, (x, y, BOX_SIZE, BOX_SIZE))

    def build_board(self):
        """A shuffled matrix with the game cards"""

        # shuffle all the image/color combinations
        items = [(image, color) for color in Color for image in Image]
        random.shuffle(items)

        # take just the required ones, make them double, and shuffle
        count = N_COLS * N_ROWS // 2
        items = items[:count] * 2
        random.shuffle(items)

        # put the chosen cards in matrix format
        return [items[i : i + N_COLS] for i in range(0, len(items), N_COLS)]

    def draw_board(self, cheat=False):
        """
        Draws all of the boxes in their covered or revealed state

        When plain is False, the cards are always showed
        """
        for i in range(N_ROWS):
            for j in range(N_COLS):
                x, y = self.get_xy(i, j)
                if cheat or self.status[i][j]:
                    self.draw_card(*self.get_card_info(i, j), x, y)
                else:
                    self.draw_back_card(x, y)


if __name__ == "__main__":
    game = Game()
    game.run()
    print("Done!")
