"""
Memory Puzzle - A simple memory matching game

From: Making Games with Python & Pygame by Al Sweigart - https://inventwithpython.com/pygame/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/makinggames

Step 3: win a game and iterate
"""

import random
import pygame
from enum import Enum, auto

# timing
FPS = 30
VIEW_TIME = 750

# screen constants: size (in pixel), title
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Memory Game"

# constants for placing the cards on the screen
N_ROWS = 3
N_COLS = 6

CARD_SIZE = 40
GAP_SIZE = 10
BLOCK_SIZE = CARD_SIZE + GAP_SIZE
REVEAL_STEP = CARD_SIZE // 5

X_MARGIN = (SCREEN_WIDTH - (N_COLS * BLOCK_SIZE)) // 2
Y_MARGIN = (SCREEN_HEIGHT - (N_ROWS * BLOCK_SIZE)) // 2


class GameColor:
    """Colors in the game (not in the cards)"""

    CARD_BACK = (255, 255, 255)  # white
    BACKGROUND = (60, 60, 100)  # navy blue
    HIGHLIGHT = (173, 216, 230)  # light blue
    ALT_BACKGROUND = (180, 120, 60)  # amber-orange


class Color(Enum):
    """Colors on cards"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 128, 0)
    PURPLE = (255, 0, 255)
    CYAN = (0, 255, 255)


class Image(Enum):
    """Images on cards"""

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
        self.visibility = self.build_cards_visibility(False)
        self.current_card = None
        self.first_ij = None

    def cover_cards(self, xy_cards):
        """gradually cover the cards"""
        for coverage in range(0, CARD_SIZE + 1, REVEAL_STEP):
            self.clock.tick(FPS)
            for xy in xy_cards:
                area = (*xy, coverage, CARD_SIZE)
                pygame.draw.rect(self.screen, GameColor.CARD_BACK, area)
            pygame.display.flip()

    def flash_cards(self):
        """Show all the cards for a couple of seconds"""
        self.clock.tick(FPS)
        self.screen.fill(GameColor.BACKGROUND)

        self.draw_board(True)

        pygame.display.flip()
        pygame.time.wait(VIEW_TIME)

        for i in range(N_ROWS):
            card_group = []
            for j in range(N_COLS):
                card_group.append(self.get_xy(i, j))
            self.cover_cards(card_group)

    def get_card_pos(self, xy):
        """Get the card xy (top-left) and ij coordinates, if we are in its rectangle"""
        for i in range(N_ROWS):
            for j in range(N_COLS):
                top_left = self.get_xy(i, j)
                rect = pygame.Rect(*top_left, CARD_SIZE, CARD_SIZE)
                if rect.collidepoint(xy[0], xy[1]):
                    return top_left, (i, j)
        return None

    def highlight_card(self, pos, on=True):
        """Place a border around the card with the given position, or do nothing"""
        if pos:
            color = GameColor.HIGHLIGHT if on else GameColor.BACKGROUND
            area = (pos[0][0] - 5, pos[0][1] - 5, CARD_SIZE + 10, CARD_SIZE + 10)
            pygame.draw.rect(self.screen, color, area, 4)

    def set_highlight(self):
        """Set the card in the mouse position to highlighted"""
        candidate = self.get_card_pos(pygame.mouse.get_pos())

        if candidate != self.current_card:
            self.clock.tick(FPS)

            self.highlight_card(self.current_card, False)
            self.highlight_card(candidate)
            pygame.display.flip()

            self.current_card = candidate

    def select_card(self, pos):
        """Reveal the card in the passed position, when required"""
        if pos and not self.visibility[pos[1][0]][pos[1][1]]:
            self.reveal_card(pos)
            self.visibility[pos[1][0]][pos[1][1]] = True
            return pos[1]
        else:
            return None

    def play(self, mouse_xy):
        """
        Turn the card in the passed position.
        If it is the second card in a pair:
        compare two cards
        if they don't match turn them back
        in any case make invalid first_ij.
        Return True if a match is found.
        """
        match = False
        if card_ij := self.select_card(self.get_card_pos(mouse_xy)):
            if self.first_ij:
                if self.get_card_info(*self.first_ij) == self.get_card_info(*card_ij):
                    match = True
                else:
                    cards = [self.get_xy(*self.first_ij), self.get_xy(*card_ij)]
                    self.cover_cards(cards)
                    self.visibility[self.first_ij[0]][self.first_ij[1]] = False
                    self.visibility[card_ij[0]][card_ij[1]] = False
                self.first_ij = None
            else:
                self.first_ij = card_ij
        return match

    def flash_win(self):
        c1 = GameColor.BACKGROUND
        c2 = GameColor.ALT_BACKGROUND

        for _ in range(10):
            c1, c2 = c2, c1
            self.screen.fill(c1)
            self.draw_board()
            pygame.display.flip()
            pygame.time.wait(300)

    def check_win(self):
        if all(all(row) for row in self.visibility):
            self.flash_win()

            # reset
            self.visibility = self.build_cards_visibility(False)
            self.board = self.build_board()
            self.draw_board()

            pygame.display.flip()

    def run(self):
        """Run the main game loop"""
        self.flash_cards()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE
                ):
                    running = False
                elif event.type == pygame.MOUSEMOTION:
                    self.set_highlight()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.play(event.pos):
                        self.check_win()

        pygame.quit()

    def get_xy(self, i: int, j: int):
        """
        Convert position on board to pixel coordinates for the left-top corner

        For example: i = 0, j = 0 -> (270, 140); i = 0, j = 1 -> (320, 140)
        """
        return j * BLOCK_SIZE + X_MARGIN, i * BLOCK_SIZE + Y_MARGIN

    def build_cards_visibility(self, x: bool):
        """Build a card visibility matrix (True for visible)"""
        return [[x] * N_COLS for _ in range(N_ROWS)]

    def draw_card(self, image: Image, color: Color, x: int, y: int):
        """Draw the image/color card from the top-left position x, y"""
        QUARTER = CARD_SIZE // 4
        HALF = CARD_SIZE // 2

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
                (x + CARD_SIZE - 1, y + HALF),
                (x + HALF, y + CARD_SIZE - 1),
                (x, y + HALF),
            )
            pygame.draw.polygon(self.screen, color.value, area)
        elif image == Image.LINES:
            for i in range(0, CARD_SIZE, 4):
                start_end = (x, y + i), (x + i, y)
                pygame.draw.line(self.screen, color.value, *start_end)
                start_end = (x + i, y + CARD_SIZE - 1), (x + CARD_SIZE - 1, y + i)
                pygame.draw.line(self.screen, color.value, *start_end)
        elif image == Image.OVAL:
            area = (x, y + QUARTER, CARD_SIZE, HALF)
            pygame.draw.ellipse(self.screen, color.value, area)

    def draw_back_card(self, x, y):
        """Draw the card back in the given position"""
        pygame.draw.rect(self.screen, GameColor.CARD_BACK, (x, y, CARD_SIZE, CARD_SIZE))

    def get_card_info(self, i: int, j: int):
        """Get image and color for the (i, j) card"""
        return self.board[i][j]

    def reveal_card(self, pos):
        """gradually reveal a card"""
        if pos:
            for back in range(CARD_SIZE, -1, -REVEAL_STEP):
                self.clock.tick(FPS)
                area = (*pos[0], CARD_SIZE, CARD_SIZE)
                pygame.draw.rect(self.screen, GameColor.BACKGROUND, area)
                self.draw_card(*self.get_card_info(*pos[1]), *pos[0])
                area = (*pos[0], back, CARD_SIZE)
                pygame.draw.rect(self.screen, GameColor.CARD_BACK, area)
                pygame.display.flip()
            pygame.time.wait(VIEW_TIME)

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

        When cheat is True, the cards are always showed
        """
        for i in range(N_ROWS):
            for j in range(N_COLS):
                x, y = self.get_xy(i, j)
                if cheat or self.visibility[i][j]:
                    self.draw_card(*self.board[i][j], x, y)
                else:
                    self.draw_back_card(x, y)


if __name__ == "__main__":
    game = Game()
    game.run()
    print("Done!")
