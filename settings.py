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
    "candle": f"{SYMBOL_PATH}/candle.png",
    "ghost": f"{SYMBOL_PATH}/ghost.png",
    "grave": f"{SYMBOL_PATH}/grave.png",
    "potion": f"{SYMBOL_PATH}/potion.png",
    "pumpkin": f"{SYMBOL_PATH}/pumpkin.png",
    "skull": f"{SYMBOL_PATH}/skull.png"
}