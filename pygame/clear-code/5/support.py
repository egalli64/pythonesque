"""
Master Python by making 5 games - 5: Monster battle

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs&t=32960s
GitHub: https://github.com/clear-code-projects/5games/tree/main/Monster%20battle
Google Drive: https://drive.google.com/drive/folders/15VQ37pgCwXxHZ8oBK0yc_CzKQeP2qSSl

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from os.path import join
from os import walk


def folder_importer(*path):
    surfs = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            surfs[file_name.split(".")[0]] = pygame.image.load(
                full_path
            ).convert_alpha()
    return surfs


def audio_importer(*path):
    audio_dict = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            audio_dict[file_name.split(".")[0]] = pygame.mixer.Sound(
                join(folder_path, file_name)
            )
    return audio_dict


def tile_importer(cols, *path):
    attack_frames = {}
    for folder_path, _, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            surf = pygame.image.load(full_path).convert_alpha()
            attack_frames[file_name.split(".")[0]] = []
            cutout_width = surf.get_width() / cols
            for col in range(cols):
                cutout_surf = pygame.Surface(
                    (cutout_width, surf.get_height()), pygame.SRCALPHA
                )
                cutout_rect = pygame.FRect(
                    cutout_width * col, 0, cutout_width, surf.get_height()
                )
                cutout_surf.blit(surf, (0, 0), cutout_rect)
                attack_frames[file_name.split(".")[0]].append(cutout_surf)
    return attack_frames
