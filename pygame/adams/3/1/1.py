"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat
"""

from typing import override
import pygame

WIN_RECT = pygame.Rect(0, 0, 300, 200)
TITLE = "Cat animation"


class Animation:
    def __init__(self, namelist: list[str], delta: int = 100, colorkey="black") -> None:
        self.images: list[pygame.Surface] = []
        self.timer = Timer(delta)
        for filename in namelist:
            bitmap = pygame.image.load(filename).convert()
            bitmap.set_colorkey(colorkey)
            self.images.append(bitmap)
        self.index = 0

    def current(self) -> pygame.Surface:
        if self.timer.tick():
            self.index = (self.index + 1) % len(self.images)
        return self.images[self.index]


class Timer:
    MIN_DURATION = 10

    def __init__(self, duration: int):
        self.duration = duration
        self.next = pygame.time.get_ticks() + duration

    def tick(self) -> bool:
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.duration
            return True
        return False

    def change_duration(self, delta: int):
        self.duration = max(Timer.MIN_DURATION, self.duration + delta)


class Cat(pygame.sprite.Sprite):
    FILE_TEMPLATE = "../images/cat-{:d}.bmp"
    TRANSPARENT_COLOR = "black"

    def __init__(self) -> None:
        super().__init__()
        self.animation = Animation([Cat.FILE_TEMPLATE.format(i) for i in range(6)])

        self.image: pygame.Surface = self.animation.current()
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = WIN_RECT.center

    @override
    def update(self) -> None:
        self.image = self.animation.current()

    def change_timing(self, delta: int) -> None:
        self.animation.timer.change_duration(delta)


class CatAnimation:
    FPS = 30

    def __init__(self) -> None:
        self.window = pygame.Window(TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 12)
        self.cat = Cat()
        self.cat_group = pygame.sprite.GroupSingle(self.cat)

    def run(self) -> None:
        while self.handle_events():
            self.clock.tick(CatAnimation.FPS)

            self.cat.update()
            self.draw()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_PLUS:
                    self.cat.change_timing(-10)
                elif event.key == pygame.K_MINUS:
                    self.cat.change_timing(10)
        return True

    def update(self) -> None:
        self.cat_group.update()

    def draw(self) -> None:
        self.screen.fill("gray")
        self.cat_group.draw(self.screen)
        text_image = self.font.render(
            f"animation time: {self.cat.animation.timer.duration}",
            True,
            "white",
        )
        text_rect = text_image.get_rect()
        text_rect.centerx = WIN_RECT.centerx
        text_rect.bottom = WIN_RECT.bottom - 50
        self.screen.blit(text_image, text_rect)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        CatAnimation().run()
    finally:
        pygame.quit()
        print("Done.")
