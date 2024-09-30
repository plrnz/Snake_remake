import tkinter
import random

ROWS = 30
COLS - 30
TILE_SIZE = 30

WINDOW_WIDTH = TILE_SIZE * COLS   # 30*30 = 900
WINDOW_HEIGHT = TILE_SIZE * ROWS  # 30*30 = 900


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# game window
window = tkinter.Tk()
window.title("The Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0
                        highlightthickness=0)
canvas.pack()
window.update()
