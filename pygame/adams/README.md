# Introduction to Pygame-ce by Ralf Adams

- https://github.com/adamsralf/pygame_book
- My notes: https://github.com/egalli64/pythonesque/ pygame/adams folder
- Ensure pygame is available: pip install pygame-ce

# Chapter 2 - Basics
## Section 1 - Kind of Hello World!
- 1: [Hello pygame](2/1/1.py) - init and quit
- 2: [Hello again, pygame](2/1/2.py) - Window
- 3: [It's me again, pygame](2/1/3.py) - Clock
- 4: [Multiple windows](2/1/4.py) - WINDOWCLOSE event

## Section 2 - Graphic primitives
- 1: [Introduction](2/2/1.py) - functions in module draw 
- 2: [Particle swarm /1](2/2/2.py) - draw.circle, pygame mouse support
- 3: [Particle swarm /2](2/2/3.py) - some randomness
- 4: [Particle swarm /3](2/2/4.py) - mutable particles, fountain effect
- 5: [Particle swarm /4](2/2/5.py) - add x-scattering
- 6: [Particle swarm /6](2/2/6.py) - more features added
- 7: [Landscape example](2/2/7.py)

## Section 3 - Load and Blit Bitmaps
- 1: [Load and blit](2/3/1.py)
- 2: [Partial blitting](2/3/2.py)
- 3: [Message boxes](2/3/3.py)
- 4: [Landscape blit](2/3/4.py) - !!! Caching surfaces is not useful in such simple cases !!!

## Section 4 - Moving Bitmaps
- 1: [Using Rect and its attributes](2/4/1.py)
- 2: [Speed in pixel for frame](2/4/2.py) - simple but unreliable
- 3: [Normalizing speed](2/4/3.py) - pixel for second, based on delta time, using FRect

## Section 5 - Class Sprite
- 1: [Defender as a Sprite](2/5/1.py)
- 2: [Sprite collision](2/5/2.py)
- 3: [Sprite Group](2/5/3.py)
