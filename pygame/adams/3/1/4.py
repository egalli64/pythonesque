"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat - dt from main loop
"""

from typing import override
import pygame

WIN_RECT = pygame.Rect(0, 0, 300, 200)
TITLE = "Cat animation"


class Animation:
    MIN_DURATION = 0.01
    DEFAULT_DURATION_TIME = 0.1

    def __init__(self, filenames, colorkey, duration=DEFAULT_DURATION_TIME):
        self.frames: list[pygame.Surface] = []
        for filename in filenames:
            bitmap = pygame.image.load(filename).convert()
            bitmap.set_colorkey(colorkey)
            self.frames.append(bitmap)

        self.duration = duration
        self.timer = 0.0
        self.index = 0

    def update(self, dt):
        self.timer += dt

        while self.timer >= self.duration:
            self.timer -= self.duration
            self.index = (self.index + 1) % len(self.frames)

    def change_duration(self, increase: bool):
        delta = Animation.MIN_DURATION * (1 if increase else -1)
        self.duration = max(Animation.MIN_DURATION, self.duration + delta)

    @property
    def image(self):
        return self.frames[self.index]


class Cat(pygame.sprite.Sprite):
    FILE_TEMPLATE = "../images/cat-{:d}.bmp"
    TRANSPARENT_COLOR = "black"

    def __init__(self) -> None:
        super().__init__()
        filenames = [Cat.FILE_TEMPLATE.format(i) for i in range(6)]
        self.animation = Animation(filenames, Cat.TRANSPARENT_COLOR)

        self.image: pygame.Surface = self.animation.image
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = WIN_RECT.center

    @override
    def update(self, dt) -> None:
        self.animation.update(dt)
        self.image = self.animation.image


class Game:
    FPS = 30
    BACKGROUND_COLOR = "gray"
    TEXT_COLOR = "white"

    def __init__(self) -> None:
        self.window = pygame.Window(TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 12)
        self.cat = Cat()
        self.cat_group = pygame.sprite.GroupSingle(self.cat)

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.cat.update(dt)
            self.draw()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_PLUS:
                    self.cat.animation.change_duration(False)
                elif event.key == pygame.K_MINUS:
                    self.cat.animation.change_duration(True)
        return True

    def draw(self) -> None:
        self.screen.fill(Game.BACKGROUND_COLOR)
        self.cat_group.draw(self.screen)
        text = f"animation time: {self.cat.animation.duration:.2f}"
        caption = self.font.render(text, True, Game.TEXT_COLOR)
        text_rect = caption.get_rect()
        text_rect.centerx = WIN_RECT.centerx
        text_rect.bottom = WIN_RECT.bottom - 50
        self.screen.blit(caption, text_rect)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
