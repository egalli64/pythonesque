"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Collision between a sprite and a group of sprites
"""
import pygame
from player import Player, Direction
from block import Block

FPS = 30
TITLE = "Collision kills"
WIN_RECT = pygame.Rect(0, 0, 640, 480)
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (200, 200, 200)
TEXT_POS = (10, 10)
FONT_SIZE = 24


def as_direction(keys: pygame.key.ScancodeWrapper) -> Direction:
    if keys[pygame.K_LEFT]:
        return Direction.LEFT
    elif keys[pygame.K_RIGHT]:
        return Direction.RIGHT
    elif keys[pygame.K_UP]:
        return Direction.UP
    elif keys[pygame.K_DOWN]:
        return Direction.DOWN
    else:
        return Direction.STOP


class Game:
    text: pygame.Surface

    @classmethod
    def load_resources(cls) -> None:
        cls._font = pygame.font.Font(None, FONT_SIZE)

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = screen.get_rect()
        self.running = True

        self.player = Player(self.viewport)
        self.blocks = pygame.sprite.Group()
        for x in range(80, 600, 80):
            for y in range(120, 400, 80):
                self.blocks.add(Block((x, y)))

        self.all_sprites = pygame.sprite.Group(self.player, self.blocks)
        self.update_text()

    def update_text(self):
        self.text = Game._font.render(f"Blocks remaining: {len(self.blocks)}", True, TEXT_COLOR)

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.player.update(dt)
            # by default rects are used to determine collisions
            if pygame.sprite.spritecollide(self.player, self.blocks, True):
                # the list of colliding blocks is not empty -> (at least) a block has been killed
                self.update_text()

            self.screen.fill(BACKGROUND_COLOR)
            self.all_sprites.draw(self.screen)
            self.screen.blit(self.text, TEXT_POS)
            self.window.flip()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

        keys = pygame.key.get_pressed()
        self.player.set_direction(as_direction(keys))


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_RECT.size)
    pg_screen = pg_window.get_surface()

    Game.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
