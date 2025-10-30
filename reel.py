from settings import *
import pygame, random

class Reel:
    def __init__(self, pos):
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(symbols.keys())
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:5]

        self.reels_is_spinning = False

        # TODO: Sounds

        for i, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(symbols[item], pos, i))
            pos = list(pos)
            pos[1] += 300
            pos = tuple(pos)

    def animate(self, delta_time):
        if self.reels_is_spinning:
            self.delay_time -= (delta_time * 1000)
            self.spin_time -= (delta_time * 1000)
            reel_is_stopping = False

            if self.spin_time < 0:
                reel_is_stopping = True
            
            if self.delay_time <= 0:

                # Iterate through all symbols in reel, remove last, add new one to top of the stack
                for symbol in self.symbol_list:
                    symbol.rect.bottom += 100

                    # Correct spacing is dependent on the above addition eventually hitting 1200
                    if symbol.rect.top == 1200:
                        if reel_is_stopping:
                            self.reels_is_spinning = False
                            # stop sound effect?

                        symbol_i = symbol.i
                        symbol.kill()
                        # Spawn random symbol in place of the above
                        self.symbol_list.add(Symbol(symbols[random.choice(self.shuffled_keys)], ((symbol.x_val), -300), symbol_i))

    def start_spin(self, delay_time):
        self.delay_time = delay_time
        self.spin_time = 1000 + delay_time
        self.reels_is_spinning = True

    def reel_spin_result(self):
        spin_symbols = []
        for i in GAME_INDICES:
            spin_symbols.append(self.symbol_list.sprites()[i].sym_type)
        return spin_symbols[::-1]

class Symbol(pygame.sprite.Sprite):
    def __init__(self, pathTofile, pos, i):
        super().__init__()

        self.sym_type = pathTofile.split("/")[2].split(".")[0]

        self.pos = pos
        self.i = i
        self.image = pygame.image.load(pathTofile)
        self.rect = self.image.get_rect(topleft = pos)
        self.x_val = self.rect.left

    def update(self):
        pass