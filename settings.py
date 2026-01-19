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
    "candle": f"{SYMBOL_PATH}/candle.png",
    "potion": f"{SYMBOL_PATH}/potion.png",
    "pumpkin": f"{SYMBOL_PATH}/pumpkin.png",
    "skull": f"{SYMBOL_PATH}/skull.png",
    "ten": f"{SYMBOL_PATH}/ten.png",
    "jack": f"{SYMBOL_PATH}/jack.png",
    "queen": f"{SYMBOL_PATH}/queen.png",
    "king": f"{SYMBOL_PATH}/king.png",
    "ace": f"{SYMBOL_PATH}/ace.png",
    "wild": f"{SYMBOL_PATH}/wild.png"
}

REELS = {
    "reel1" : ["ten", "ten", "ten", "ten", "ten", "ten", "jack", "jack", "jack", "jack", "jack", "jack", "queen", "queen", "queen", "queen", "queen", "queen", "king", "king", "king", "king", "king", "king", "ace", "ace", "ace", "ace", "ace", "ace", "pumpkin", "pumpkin", "ghost", "ghost", "skull", "skull", "potion", "potion", "candle", "candle"],
    "reel2" : ["ten", "ten", "ten", "ten", "ten", "ten", "jack", "jack", "jack", "jack", "jack", "jack", "queen", "queen", "queen", "queen", "queen", "queen", "king", "king", "king", "king", "king", "king", "ace", "ace", "ace", "ace", "ace", "ace", "pumpkin", "pumpkin", "ghost", "ghost", "skull", "skull", "potion", "potion", "candle", "candle", "wild", "wild"],
    "reel3" : ["ten", "ten", "ten", "ten", "ten", "ten", "jack", "jack", "jack", "jack", "jack", "jack", "queen", "queen", "queen", "queen", "queen", "queen", "king", "king", "king", "king", "king", "king", "ace", "ace", "ace", "ace", "ace", "ace", "pumpkin", "pumpkin", "ghost", "ghost", "skull", "skull", "potion", "potion", "candle", "candle", "wild", "wild"],
    "reel4" : ["ten", "ten", "ten", "ten", "ten", "ten", "jack", "jack", "jack", "jack", "jack", "jack", "queen", "queen", "queen", "queen", "queen", "queen", "king", "king", "king", "king", "king", "king", "ace", "ace", "ace", "ace", "ace", "ace", "pumpkin", "pumpkin", "ghost", "ghost", "skull", "skull", "potion", "potion", "candle", "candle", "wild", "wild"],
    "reel5" : ["ten", "ten", "ten", "ten", "ten", "ten", "jack", "jack", "jack", "jack", "jack", "jack", "queen", "queen", "queen", "queen", "queen", "queen", "king", "king", "king", "king", "king", "king", "ace", "ace", "ace", "ace", "ace", "ace", "pumpkin", "pumpkin", "ghost", "ghost", "skull", "skull", "potion", "potion", "candle", "candle"]
}

# Winning lines
WINNING_LINES = {
    "line1": [(0,0), (0,1), (0,2), (0,3), (0,4)],
    "line2": [(1,0), (1,1), (1,2), (1,3), (1,4)],
    "line3": [(2,0), (2,1), (2,2), (2,3), (2,4)],
    "line4": [(0,0), (1,1), (2,2), (1,3), (0,4)],
    "line5": [(2,0), (1,1), (0,2), (1,3), (2,4)]
}

# Payout multipliers for each symbol
PAYOUT_MULTIPLIERS = {
    "pumpkin": {3: 2.22, 4: 13.11, 5: 111.11},
    "ghost": {3: 2.22, 4: 11.01, 5: 91.33},
    "skull": {3: 2.00, 4: 9.99, 5: 41.11},
    "potion": {3: 1.66, 4: 7.77, 5: 31.11},
    "candle": {3: 1.33, 4: 5.67, 5: 20.22},
    "ace": {3: 1.11, 4: 2.87, 5: 10.11},
    "king": {3: 0.67, 4: 2.11, 5: 9.11},
    "queen": {3: 0.55, 4: 1.67, 5: 7.77},
    "jack": {3: 0.33, 4: 1.11, 5: 5.55},
    "ten": {3: 0.22, 4: 1.11, 5: 3.33},
    "wild": {3: 0, 4: 0, 5: 0}
}