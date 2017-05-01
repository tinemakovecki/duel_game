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


    def return_opponent(self):
        ''' returns the opponent of the current player '''
        if self.Current_player == self.Player1:
            return self.Player2
        elif self.Current_player == self.Player2:
            return self.Player1
        else:
            assert False, "invalid opponent"
        # TODO - better done with tags?


    def take_turn(self, Selected_attack):
        ''' completes a single game turn, returns pair (winner, damage dealt) '''
        Attacker_mods = self.Current_player.Active_modifiers
        Defender_mods = self.return_opponent().Active_modifiers
        Hit_check = check_hit(Selected_attack, Attacker_mods) # TODO BUG: almost never misses?
        Damage_dealt = calculate_damage(Selected_attack, Attacker_mods)

        # if the attack hits move on to the effects
        if Hit_check == True:
            self.return_opponent().HP -= Damage_dealt
            # a modifier activates sometimes, half the time for now
            if random.random() > 1/2:
                New_mod = Selected_attack.Modifier # direct call instead of constructor, MIGHT EDIT ORIGINAL!?
                if Selected_attack.Modifier[3] == True: # check if modifier targets opponent
                    Defender_mods.append((self.Turn_number, New_mod))
                else:
                    Attacker_mods.append((self.Turn_number, New_mod))

        # defines which player played the turn
        # change into Bool?
        if self.Current_player == self.Player1:
            active_player = 'Player 1'
        elif self.Current_player == self.Player2:
            active_player = 'Player 2'

        # game state update/check if game over
        self.check_game_state()
        if self.Game_active == False:
            return (active_player, Hit_check, Damage_dealt)

        # if game isn't over, update objects and move on to next turn
        else:
            self.Turn_number += 1
            self.update_modifiers()
            self.Current_player = self.return_opponent()
            return (active_player, Hit_check, Damage_dealt)
        # TODO unify capitalization


    def check_game_state(self):
        ''' checks if game continues/selects winner '''
        if self.return_opponent().HP <= 0:
            self.Game_active = False
            # find the winner
            if self.Current_player == self.Player1:
                self.Winner = 'Player 1'
            else:
                self.Winner = 'Player 2'
        return


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


    def copy(self):
        # TODO for minmax
        pass


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