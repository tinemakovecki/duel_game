### GAME LOGIC FILE
import random
import Class # TODO put the file in the right place

class Game():
    def __init__(self):
        # TODO add monster choice option
        self.player1 = Class.create_pika()
        self.player2 = Class.create_char()

        self.current_player = self.player1
        self.turn_number = 1
        self.game_active = True
        self.winner = 'undefined' # change to None?
        self.history = []


    def save_state(self):
        """ adds current state of the game to history """
        # add (turn number, active player, player 1, player 2) to game history
        # player 1 and player 2 contain data about active mods
        turn_number = self.turn_number
        player_1 = Class.copy_monster(self.player1)
        player_2 = Class.copy_monster(self.player2)
        # save which player's turn it is
        if self.current_player == self.player1:
            active_player = 'player 1'
        else:
            active_player = 'player 2'

        self.history.append((turn_number, active_player, player_1, player_2))


    def copy(self):
        """ copies the game in its current state without history and returns the copy """
        # generate new game and adjust it
        game_copy = Game()
        game_copy.turn_number = self.turn_number
        game_copy.player1 = Class.copy_monster(self.player1)
        game_copy.player2 = Class.copy_monster(self.player2)
        # reference the right player as the current player
        if self.current_player == self.player1:
            game_copy.current_player = game_copy.player1
        else:
            game_copy.current_player = game_copy.player2

        return game_copy


    def reverse_move(self):
        """ reverses one move and returns to the previous game state """
        # assign previous values to game variables and remove one entry from game history
        (self.turn_number, active_player, self.player1, self.player2) = self.history.pop()
        # assign the right Current_player
        if active_player == 'player 1':
            self.current_player = self.player1
        elif active_player == 'player 2':
            self.current_player = self.player2
        else:
            assert False, " reversing moves player assignment broke "


    def return_opponent(self):
        ''' returns the opponent of the current player '''
        if self.current_player == self.player1:
            return self.player2
        elif self.current_player == self.player2:
            return self.player1
        else:
            assert False, "invalid opponent"
        # TODO - better done with tags?


    def take_turn(self, selected_attack, certain_hit):
        ''' completes a single game turn, returns pair (winner, damage dealt) '''
        self.save_state()  # save current state before doing anything
        attacker_mods = self.current_player.active_modifiers
        defender_mods = self.return_opponent().active_modifiers
        damage_dealt = calculate_damage(selected_attack, attacker_mods)

        # check if an attack hits
        if certain_hit is None:
            hit_check = check_hit(selected_attack, attacker_mods)
        # options for certain hit/miss to use for computer player decisions
        elif certain_hit:
            hit_check = True
        elif not certain_hit:
            hit_check = False

        # if the attack hits move on to the effects
        if hit_check:
            self.return_opponent().hp -= damage_dealt
            # a modifier activates sometimes, half the time for now
            if random.random() > 1/2:
                new_mod = selected_attack.modifier # direct call instead of constructor, MIGHT EDIT ORIGINAL!?
                if new_mod[3]: # check if modifier targets opponent
                    same_mod = None
                    for (turn_number, mod) in defender_mods:
                        if mod[0] == new_mod[0]:
                            same_mod = mod
                            same_mod_turn = turn_number
                    if same_mod is not None:
                        defender_mods.remove((same_mod_turn, same_mod))
                    defender_mods.append((self.turn_number, new_mod))
                else:
                    same_mod = None
                    for (turn_number, mod) in attacker_mods:
                        if mod[0] == new_mod[0]:
                            same_mod = mod
                            same_mod_turn = turn_number
                    if same_mod is not None:
                        attacker_mods.remove((same_mod_turn, same_mod))
                    attacker_mods.append((self.turn_number, new_mod))

        # defines which player played the turn
        # change into Bool?
        if self.current_player == self.player1:
            active_player = 'Player 1'
        elif self.current_player == self.player2:
            active_player = 'Player 2'

        # game state update/check if game over
        self.check_game_state()
        if not self.game_active:
            return (active_player, hit_check, damage_dealt)

        # if game isn't over, update objects and move on to next turn
        else:
            self.turn_number += 1
            self.update_modifiers()
            self.current_player = self.return_opponent()
            return (active_player, hit_check, damage_dealt)
        # TODO unify capitalization


    def check_game_state(self):
        ''' checks if game continues/selects and return possible winner '''
        if self.return_opponent().hp <= 0:
            self.game_active = False
            # find the winner
            if self.current_player == self.player1:
                self.winner = 'Player 1'
            else:
                self.winner = 'Player 2'
        return self.winner

    # TODO change from modifier[x][y] to actual methods fo calling attributes
    def update_modifiers(self):
        ''' updates list of active modifiers for both players '''
        # update current player modifiers
        updated_mods = []
        for modifier in self.current_player.active_modifiers:
            if self.turn_number - modifier[0] <= 6:
                updated_mods.append(modifier)
        self.current_player.active_modifiers = updated_mods

        # update opponent modifiers
        updated_mods = []
        for modifier in self.current_player.active_modifiers:
            if self.turn_number - modifier[0] <= 6:
                updated_mods.append(modifier)
        self.current_player.active_modifiers = updated_mods

        return


def check_hit(selected_attack, attacker_mods):
    ''' decies if an attack will hit, returns True/False '''
    hit_chance = selected_attack.hit_chance
    for modifier in attacker_mods: # percent scaling?
        hit_chance += modifier[1][2]

    if hit_chance / 100 > random.random():
        return True
    else:
        return False

def calculate_damage(selected_attack, attacker_mods):
    ''' returns the damage an attack deals '''
    damage_dealt = selected_attack.damage
    for modifier in attacker_mods:
        damage_dealt += modifier[1][1]

    return damage_dealt