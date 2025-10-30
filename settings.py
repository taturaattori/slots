#Display settings
DEFAULT_IMG_SIZE = (300, 300)
FPS = 120
HEIGHT = 1000
WIDTH = 1600
START_X, START_Y = 0, -300
X_OFFSET, Y_OFFSET = 20, 0

# Images
BG_IMG_PATH = "graphics/haunted.png"
GAME_INDICES = [1, 2, 3] # 0, 4 and 5 are outside of reels
SYMBOL_PATH = "graphics/symbols"

# Symbols
symbols = {
    "ghost": f"{SYMBOL_PATH}/ghost.png",
    "grave": f"{SYMBOL_PATH}/grave.png",
    "potion": f"{SYMBOL_PATH}/potion.png",
    "pumpkin": f"{SYMBOL_PATH}/pumpkin.png",
    "skull": f"{SYMBOL_PATH}/skull.png",
    "wild": f"{SYMBOL_PATH}/wild.png"
}

# Winning lines
WINNING_LINES = {
    "line1": [(0,0), (0,1), (0,2), (0,3), (0,4)],
    "line2": [(1,0), (1,1), (1,2), (1,3), (1,4)],
    "line3": [(2,0), (2,1), (2,2), (2,3), (2,4)],
    "line4": [(0,0), (1,1), (2,2), (1,3), (0,4)],
    "line5": [(2,0), (1,1), (0,2), (1,3), (2,4)]
}