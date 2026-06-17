"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""

import random
import pygame

WIN_RECT = pygame.Rect(0, 0, 300, 200)


class Timer:
    def __init__(self, delta: int):
        self.delta = delta
        self.next = pygame.time.get_ticks() + self.delta

    def tick(self) -> bool:
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.delta
            return True
        return False


class Animation:
    def __init__(self, namelist: list[str], delta: int) -> None:
        self.images: list[pygame.Surface] = []
        self.timer = Timer(delta)
        for filename in namelist:
            bitmap = pygame.image.load(filename).convert_alpha()
            self.images.append(bitmap)
        self.index = 0
        self.running = True

    def current(self) -> pygame.Surface:
        if self.timer.tick():
            if self.index < len(self.images) - 1:
                self.index += 1
            else:
                self.running = False
        return self.images[self.index]

    def done(self) -> bool:
        return not self.running


class Rock(pygame.sprite.Sprite):
    FILENAME = "../images/rock.png"
    EXPLOSION_TEMPLATE = "../images/explosion-{:d}.png"

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Rock.FILENAME).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect()
        max_pos = (WIN_RECT.width - self.rect.width, WIN_RECT.height - self.rect.height)
        self.rect.centerx = random.randint(self.rect.width, max_pos[0])
        self.rect.centery = random.randint(self.rect.height, max_pos[1])
        explosions = [Rock.EXPLOSION_TEMPLATE.format(i) for i in range(1, 5)]
        self.animation = Animation(explosions, 100)
        self.timer = Timer(random.randint(100, 2000))
        self.explosion = False

    def update(self) -> None:
        if self.timer.tick():
            self.explosion = True
        if self.explosion:
            self.image = self.animation.current()
            center = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = center
        if self.animation.done():
            self.kill()


class ExplosionAnimation(object):
    FPS = 30
    TITLE = "Exploding rocks"
    BACKGROUND_COLOR = "black"

    def __init__(self) -> None:
        self.window = pygame.Window(ExplosionAnimation.TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.all_rocks = pygame.sprite.Group()
        self.timer = Timer(500)

    def run(self) -> None:
        while self.handle_events():
            self.clock.tick(ExplosionAnimation.FPS)

            if self.timer.tick():
                self.all_rocks.add(Rock())
            self.all_rocks.update()

            self.screen.fill(ExplosionAnimation.BACKGROUND_COLOR)
            self.all_rocks.draw(self.screen)
            self.window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True


if __name__ == "__main__":
    pygame.init()

    try:
        ExplosionAnimation().run()
    finally:
        pygame.quit()
        print("Done.")
