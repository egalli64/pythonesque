"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame


class AttackAnimationSprite(pygame.sprite.Sprite):
    def __init__(self, target, frames, groups):
        super().__init__(groups)
        self.frames, self.frame_index = frames, 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_frect(center=target.rect.center)

    def update(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()
