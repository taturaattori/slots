from player import Player
from reel import *
from settings import *
from wins import *
import pygame

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.machine_balance = 10000.00
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False

        # Results
        self.prev_result = {0: None, 1: None, 2: None, 3: None, 4: None}
        self.spin_result = {0: None, 1: None, 2: None, 3: None, 4: None}

        self.spawn_reels()
        self.currPlayer = Player()

    def cooldowns(self):
        for reel in self.reel_list:
            if self.reel_list[reel].reels_is_spinning:
                self.can_toggle = False
                self.spinning = True                
        # Check that none of the reels are spinning before player can spin
        if not self.can_toggle and [self.reel_list[reel].reels_is_spinning for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True
            self.spin_result = self.get_result()
            
            if self.check_wins(self.spin_result):
                self.win_data = self.check_wins(self.spin_result)
                # Win sound
                self.pay_player(self.win_data, self.currPlayer)
                #self.win_animation_ongoing = True
                #self.ui.win_text_angle = random.randint(-4, 4)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.can_toggle and self.currPlayer.balance >= self.currPlayer.bet_size:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            self.currPlayer.place_bet()
            self.machine_balance += self.currPlayer.bet_size
            self.currPlayer.last_payout = None
            print(self.currPlayer.get_data())

    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 10, -300
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (DEFAULT_IMG_SIZE[0] + X_OFFSET), y_topleft

            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft)) 
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            for reel in self.reel_list:
                self.reel_list[reel].start_spin(int(reel) * 200)
                # TODO: add sound effect

    def get_result(self):
        for reel in self.reel_list:
            self.spin_result[reel] = self.reel_list[reel].reel_spin_result()
        return self.spin_result
    
    def check_wins(self, result):
        hits = {}
        horizontal = flip_horizontal(result)
        for row in horizontal:
            for sym in row:
                if row.count(sym) > 2:
                    possible_win = [i for i, val in enumerate(row) if sym == val]

                    if len(longest_seq(possible_win)) > 2:
                        hits[horizontal.index(row) + 1] = [sym, longest_seq(possible_win)]
        if hits:
            return hits
        
    def pay_player(self, win_data, curr_player):
        multiplier = 0
        spin_payout = 0

        for v in win_data.values():
            multiplier += len(v[1])
            
        spin_payout = (multiplier * curr_player.bet_size)
        curr_player.balance += spin_payout
        self.machine_balance -= spin_payout
        curr_player.last_payout = spin_payout
        curr_player.total_won += spin_payout

    def update(self, delta_time):
        self.cooldowns()
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()