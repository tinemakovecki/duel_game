####### - MINIMAX ALGORITHM FILE - #######

import logging
from Class import *

class Minimax():
    def __init__(self, depth):
        self.depth = depth
        self.interrupted = False
        self.game = None
        self.selected_attack = None  # the attack selected by the algorithm


    def interrupt(self):
        """ interrupts the algorithm when current game is cancelled by the player """
        self.interrupted = True


    def select_attack(self, game):
        """ select an attack to make in the current game state """
        self.game = game
        self.interrupted = False
        self.selected_attack = None

        # use minimax
        (attack, value) = self.minimax(self.depth, True)

        # forget current game state
        self.game = None
        if not self.interrupted:
            # select and make the attack if not interrupted
            logging.debug("minimax: attack {0}, value {1}".format(attack, value))
            self.selected_attack = attack


    # game value constants
    VICTORY = 200000  # TODO adjust values
    INFINITY = VICTORY + 27

    def evaluate_state(self):
        """ assigns a value to the current state of the game """
        # positive is good for Player 1, negative is good for Player 2

        if self.game.return_opponent().HP <= 0:
            return Minimax.VICTORY
        elif self.game.Current_player.HP <= 0:
            return -Minimax.VICTORY

        # the basis is the health difference
        value = (self.game.Current_player.HP - self.game.return_opponent().HP) * 100

        # also look at active modifiers
        # first for Player 1
        for element in self.game.Player1.Active_modifiers:
            x, mod = element
            # mod = (name, damage effect, accuracy effect, target opponent)
            value += mod[1] * 110
            value += mod[2] * 120

        # check Player 2 modfiers
        for element in self.game.Player2.Active_modifiers:
            x, mod = element
            value -= mod[1] * 110
            value -= mod[2] * 120

        return value


    def minimax(self, depth, maximizing):
        """ our minimax algorithm """

        # cancel and quit minimax if interrupted
        if self.interrupted:
            logging.debug("interrupting and quitting minimax, depth = {0}".format(globina))
            return (None, 0)

        # check if the game is over, if so, return (None, game state value)
        if not self.game.Game_active:
            if self.game.Winner == self.game.Player1:
                return (None, Minimax.VICTORY)
            elif self.game.Winner == self.game.Player2:
                return (None, -Minimax.VICTORY)
            else:
                assert (self.game.Winner != 'undefined'), 'minimax: game is over without a winner'

        # game isn't over
        else:
            if depth == 0:
                # we are at the deepest level
                # evaluate the situation and return the situation value
                return (None, self.evaluate_state())

            else:
                # do an iteration of maximization/minimization
                if maximizing:
                    best_attack = None
                    best_attack_value = - Minimax.INFINITY

                    for attack in possible_attacks(self.game.Current_player):
                        # we separate the options of hitting or missing
                        # the attack hits
                        self.game.take_turn(attack, certain_hit=True)
                        hit_value = self.minimax(depth-1, not maximizing)[1]
                        self.game.reverse_move()

                        # the attack misses
                        self.game.take_turn(attack, certain_hit=False)
                        miss_value = self.minimax(depth-1, not maximizing)[1]
                        self.game.reverse_move()

                        # calculate total attack value depending on hit chance
                        hit_chance = attack.Hit_chance / 100
                        miss_chance = 1 - hit_chance
                        attack_value = hit_value * hit_chance + miss_value * miss_chance

                        if attack_value > best_attack_value:
                            best_attack = attack
                            best_attack_value = attack_value


                else:
                    # minimizing
                    best_attack = None
                    best_attack_value = Minimax.INFINITY

                    for attack in possible_attacks(self.game.Current_player):
                        # we separate the options of hitting or missing
                        # the attack hits
                        self.game.take_turn(attack, certain_hit=True)
                        hit_value = self.minimax(depth-1, not maximizing)[1]
                        self.game.reverse_move()

                        # the attack misses
                        self.game.take_turn(attack, certain_hit=False)
                        miss_value = self.minimax(depth-1, not maximizing)[1]
                        self.game.reverse_move()

                        # calculate total attack value depending on hit chance
                        hit_chance = attack.Hit_chance / 100
                        miss_chance = 1 - hit_chance
                        attack_value = hit_value * hit_chance + miss_value * miss_chance

                        if attack_value < best_attack_value:
                            best_attack = attack
                            best_attack_value = attack_value


                assert (best_attack is not None), "minimax: best_attack is None"
                return (best_attack, best_attack_value)
