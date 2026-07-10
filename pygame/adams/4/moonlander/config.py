"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
# Physical constants (Moon conditions)
MOON_GRAVITY = 1.62  # m/s²
EARTH_GRAVITY = 9.81  # m/s²
PIXELS_PER_METER = 10  # Scaling 1m = 10px
GRAVITY = MOON_GRAVITY * PIXELS_PER_METER  # = 16.2 px/s²
THRUST = -2.1 * PIXELS_PER_METER  # = 21.0 px/s²
SAVE_SPEED_LANDING = 2.5 * PIXELS_PER_METER  # Safe landing velocity in px/s
LEVEL = {"easy": 5000, "fair": 500, "hard": 450, "ai": 380}
