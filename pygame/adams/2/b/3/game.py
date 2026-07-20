"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""
import pygame
from tank import Tank
from ground import Ground
from bullet import Bullet
from direction import Direction

FPS = 30
TITLE = "Stereo panning sound"
TILE_SIZE = 32  # square tile, in bit
MAP_SIZE = (25, 7)  # tiles, width, height
WIN_SIZE = (TILE_SIZE * MAP_SIZE[0], TILE_SIZE * MAP_SIZE[1])


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = screen.get_rect()
        self.running = True

        self.ground = Ground(self.viewport)
        self.tank = Tank(self.viewport)
        self.tank_group = pygame.sprite.GroupSingle(self.tank)
        self.all_bullets = pygame.sprite.Group()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        self.running = False
                    case pygame.K_UP:
                        self.tank.turn(Direction.UP)
                    case pygame.K_DOWN:
                        self.tank.turn(Direction.DOWN)
                    case pygame.K_LEFT:
                        self.tank.turn(Direction.LEFT)
                    case pygame.K_RIGHT:
                        self.tank.turn(Direction.RIGHT)
                    case pygame.K_SPACE:
                        self.fire()

    def fire(self) -> None:
        if self.tank.direction in [Direction.UP, Direction.DOWN]:
            print("North/South fire disabled!")
        elif len(self.all_bullets) < 5:
            self.all_bullets.add(Bullet(self.tank, self.viewport))

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            dt = clock.tick(FPS) / 1000

            self.handle_events()
            self.tank.update(dt)
            self.all_bullets.update(dt)

            self.ground.draw(self.screen)
            self.tank_group.draw(self.screen)
            self.all_bullets.draw(self.screen)
            self.window.flip()


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    Bullet.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
