import tkinter
import random

ROWS = 25
COLS - 25 # type: ignore
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS   # type: ignore # 25*25 = 625
WINDOW_HEIGHT = TILE_SIZE * ROWS  # 25*25 = 625


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# game window
window = tkinter.Tk()
window.title("The Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0,
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

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# initialize game
snake = Tile(TILE_SIZE * 5, TILE_SIZE * 5)  # single tile, snake's head
food = Tile(TILE_SIZE * 10, TILE_SIZE *10)
velocityX = 0
velocityY = 0
snake_body = []  # multiple snake tiles
game_over = False
score = 0


# game loop
def change_direction(e): velocityY, game_over
    # print(e)
    # print(e.keysym)

global velocityX, velocityY, game_over
if (game_over):
    return  # edit this code to reset game variables to play again

if (exec.keysym == "Up" and velocityY != 1):
    velocityX = 0
    velocityY = -1

elif (exec.keysym == "Down" and velocityX != -1):
    velocityX = 0
    velocityY = 1

elif (exec.keysym == "Right" and velocityX != 1):
    velocityX = 1
    velocityY = 0

elif (exec.keysym == "Left" and velocityX != -1):
    velocityX = 1
    velocityY = 0

def move():
    global snake, food, snake_body, game_over, score
    if (game_over):
        return

    if(snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return

    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
        return
    
    # collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
        score += 1