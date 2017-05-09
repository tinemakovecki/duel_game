### GAME LOGIC FILE
import random
import Class # TODO put the file in the right place

class Game():
    def __init__(self):
        # TODO add monster choice option
        self.Player1 = Class.createPika()
        self.Player2 = Class.createChar()

        self.Current_player = self.Player1
        self.Turn_number = 1
        self.Game_active = True
        self.Winner = 'undefined' # change to None?
        self.history = []


    def save_state(self):
        """ adds current state of the game to history """
        # add (turn number, current player, player 1, player 2) to game history
        # player 1 and player 2 contain data about active mods
        turn_number = self.Turn_number
        current_player = Class.copy_monster(self.Current_player)
        player_1 = Class.copy_monster(self.Player1)
        player_2 = Class.copy_monster(self.Player2)

        self.history.append((turn_number, current_player, player_1, player_2))


    def copy(self):
        """ copies the game in its current state without history and returns the copy """
        # generate new game and adjust it
        game_copy = Game()
        game_copy.Turn_number = self.Turn_number
        game_copy.Player1 = Class.copy_monster(self.Player1)
        game_copy.Player2 = Class.copy_monster(self.Player2)
        # reference the right player as the current player
        if self.Current_player == self.Player1:
            game_copy.Current_player = game_copy.Player1
        else:
            game_copy.Current_player = game_copy.Player2

        return game_copy


    def reverse_move(self):
        """ reverses one move and returns to the previous game state """
        # assign previous values to game variables and remove one entry from game history
        (self.Turn_number, self.Current_player, self.Player1, self.Player2) = self.history.pop()


    def return_opponent(self):
        ''' returns the opponent of the current player '''
        if self.Current_player == self.Player1:
            return self.Player2
        elif self.Current_player == self.Player2:
            return self.Player1
        else:
            assert False, "invalid opponent"
        # TODO - better done with tags?


    def take_turn(self, selected_attack, certain_hit):
        ''' completes a single game turn, returns pair (winner, damage dealt) '''
        attacker_mods = self.Current_player.Active_modifiers
        defender_mods = self.return_opponent().Active_modifiers
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
            self.return_opponent().HP -= damage_dealt
            # a modifier activates sometimes, half the time for now
            if random.random() > 1/2:
                new_mod = selected_attack.Modifier # direct call instead of constructor, MIGHT EDIT ORIGINAL!?
                if new_mod[3]: # check if modifier targets opponent
                    same_mod = None
                    for (turn_number, mod) in defender_mods:
                        if mod[0] == new_mod[0]:
                            same_mod = mod
                            same_mod_turn = turn_number
                    if same_mod is not None:
                        defender_mods.remove((same_mod_turn, same_mod))
                    defender_mods.append((self.Turn_number, new_mod))
                else:
                    same_mod = None
                    for (turn_number, mod) in attacker_mods:
                        if mod[0] == new_mod[0]:
                            same_mod = mod
                            same_mod_turn = turn_number
                    if same_mod is not None:
                        attacker_mods.remove((same_mod_turn, same_mod))
                    attacker_mods.append((self.Turn_number, new_mod))

        # defines which player played the turn
        # change into Bool?
        if self.Current_player == self.Player1:
            active_player = 'Player 1'
        elif self.Current_player == self.Player2:
            active_player = 'Player 2'

        # game state update/check if game over
        self.check_game_state()
        if not self.Game_active:
            return (active_player, hit_check, damage_dealt)

        # if game isn't over, update objects and move on to next turn
        else:
            self.Turn_number += 1
            self.update_modifiers()
            self.Current_player = self.return_opponent()
            return (active_player, hit_check, damage_dealt)
        # TODO unify capitalization


    def check_game_state(self):
        ''' checks if game continues/selects and return possible winner '''
        if self.return_opponent().HP <= 0:
            self.Game_active = False
            # find the winner
            if self.Current_player == self.Player1:
                self.Winner = 'Player 1'
            else:
                self.Winner = 'Player 2'
        return self.Winner

    # TODO change from modifier[x][y] to actual methods fo calling attributes
    def update_modifiers(self):
        ''' updates list of active modifiers for both players '''
        # update current player modifiers
        Updated_mods = []
        for modifier in self.Current_player.Active_modifiers:
            if self.Turn_number - modifier[0] <= 6:
                Updated_mods.append(modifier)
        self.Current_player.Active_modifiers = Updated_mods

        # update opponent modifiers
        Updated_mods = []
        for modifier in self.Current_player.Active_modifiers:
            if self.Turn_number - modifier[0] <= 6:
                Updated_mods.append(modifier)
        self.Current_player.Active_modifiers = Updated_mods

        return


def check_hit(Selected_attack, Attacker_mods):
    ''' decies if an attack will hit, returns True/False '''
    Hit_chance = Selected_attack.Hit_chance
    for modifier in Attacker_mods: # percent scaling?
        Hit_chance += modifier[1][2]

    if Hit_chance / 100 > random.random():
        return True
    else:
        return False

def calculate_damage(Selected_attack, Attacker_mods):
    ''' returns the damage an attack deals '''
    Damage_dealt = Selected_attack.Damage
    for modifier in Attacker_mods:
        Damage_dealt += modifier[1][1]

    return Damage_dealt