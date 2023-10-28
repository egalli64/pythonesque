"""
Cisco Network Academy
Python Essentials 2: https://skillsforall.com/course/python-essentials-2
My notes: https://github.com/egalli64/pythonesque - cisco/pe2 folder

PE2: Module 1 Section 4 – Python Package Installer (PIP)
- pip list
- pip install pygame
- or, to update: pip install -U pygame
- pip show pygame
- to get rid of it: pip uninstall pygame
"""
import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text,
            ((width - text.get_width()) // 2,
             (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        #        if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYUP:
        if event.type in [pygame.QUIT, pygame.MOUSEBUTTONUP, pygame.KEYUP]:
            run = False
        else:
            print(event)
