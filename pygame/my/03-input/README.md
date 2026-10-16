# User input

## Keyboard

### [One-shot event](change_color.py)

- When the user press the space bar, the background color changes

### [Continuous polling](move_player.py)

- A circle in the window represents the player
- When the user press the arrow keys (or a,s,d,w) the player moves
    - The player moves until a key is pressed
- The player is clamped to the window
    - It can't move out of it

### [Player as object](move-player)

- Refactor the previous example
    - [Game class](move-player/game.py) for the game structure
    - [Player class](move-player/player.py) for the player behavior
