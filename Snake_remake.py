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

# center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenheight()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int ((screen_height / 2) - (window_height / 2))

