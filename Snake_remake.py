import tkinter
import random
ROWS = 25
COLS = 25
TILE_SIZE = 25
WINDOW_WIDTH = TILE_SIZE * COLS  # 25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS  # 25*25 = 625
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y