Tetris in Python
================

Mostly complete implementation of Tetris in Python using PyGame.

Based on: https://www.freecodecamp.org/news/python-projects-for-beginners/#tetris-python-project

Mechanics
---------
Movement:
* A = move left
* D = move right
* W = rotate piece
* S = drop piece one space

Scoring:
* 1 row = 1 pt
* 2 rows = 2 pts
* 3 rows = 6 pts
* 4 rows = 12 pts

Current limitations
-------------------
* You _can_ move the pieces before they appear on the screen but the bounds-checking along the sides of the play area don't validate those moves, so it **IS** possible to get the piece into an invalid position before it appears and, as a result, crash the game.
* Scores are not saved between games.
* There is no "insta-drop"
* There is no menu. /shrug/