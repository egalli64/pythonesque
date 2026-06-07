"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Self add a Sprite to a Group
"""

from random import randint

import pygame

WIN_RECT = pygame.Rect(0, 0, 300, 600)


class Ship(pygame.sprite.Sprite):
    IMAGE = "../images/defender.png"
    SIZE = (30, 30)
    DEFAULT_SPEED = -300  # pixel/second

    rect: pygame.FRect
    image: pygame.Surface

    def __init__(self, pos: tuple[int, int], group: pygame.sprite.Group) -> None:
        super().__init__(group)
        self.image = pygame.image.load(Ship.IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, Ship.SIZE)  # type: ignore
        self.rect = pygame.FRect(self.image.get_rect())  # type: ignore
        self.rect.left = pos[0]
        self.rect.bottom = pos[1]
        self.speed = Ship.DEFAULT_SPEED

    def update(self, dt) -> None:
        self.rect.move_ip(0, self.speed * dt)
        self.rect.clamp_ip(WIN_RECT)
        return super().update()


class Game:
    FPS = 30

    TITLE = "Sprite Group"
    SHIP_MAX_LEFT = WIN_RECT.right - Ship.SIZE[0]

    # see time.set_timer() + user event for a more elegant approach
    SPAWN_DELAY = 2 / 3  # in seconds
    BACKGROUND_COLOR = "white"

    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.Window(Game.TITLE, WIN_RECT.size)

        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.ships = pygame.sprite.Group()
        self.running = True
        # see time.set_timer() + user event for a more elegant approach
        self.spawn_timer = 0

    def run(self) -> None:
        """Run the main game loop"""

        running = True
        while running:
            dt = self.clock.tick(Game.FPS) / 1000

            running = self.event_loop()
            self.update(dt)
            self.draw()

    def event_loop(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self, dt) -> None:
        self.spawn_timer += dt
        if self.spawn_timer >= Game.SPAWN_DELAY:
            self.spawn_timer = 0
            left_bottom = (randint(0, Game.SHIP_MAX_LEFT), WIN_RECT.bottom)
            Ship(left_bottom, self.ships)
        self.ships.update(dt)

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.ships.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    Game().run()
    pygame.quit()
    print("Done.")
