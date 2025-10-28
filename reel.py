from settings import *
import pygame, random

class Reel:
    def __init__(self, pos):
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(symbols.keys())
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:6]

        self.reels_is_spinning = False

        # TODO: Sounds

        for i, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(symbols[item], pos, i))
            pos = list(pos)
            pos[1] += 300
            pos = tuple(pos)

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