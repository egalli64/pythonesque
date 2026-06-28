"""
Master Python by making 5 games - 4: Platformer

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=26735s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Platform
Google Drive: https://drive.google.com/drive/folders/1FCSPHzD9R4RBUypDTB_FIfwlyiCLA5WN

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, image: pygame.Surface, groups):
        super().__init__(groups)
        self.image = image
        self.rect: pygame.FRect = self.image.get_frect(topleft=pos)


class AnimatedSprite(Sprite):
    ANIMATION_SPEED = 10

    def __init__(self, pos, frames, groups):
        self.frames = frames
        self.frame_index = 0
        super().__init__(pos, self.frames[self.frame_index], groups)

    def animate(self, dt):
        self.frame_index += AnimatedSprite.ANIMATION_SPEED * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]
