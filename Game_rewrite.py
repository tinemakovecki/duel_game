### GAME LOGIC FILE
import random
import Class.py as Class # TODO put the file in the right place

class Game():
    def __init__(self):
        # TODO add monster choice option
        self.player1 = Class.createChar()
        self.player2 = Class.createPika()

        self.Current_player = self.Player1
        self.Turn_number = 1
        self.Game_active = True
        self.Winner = 'undefined' # change to None?


    def return_opponent(self):
        ''' returns the opponent of the current player '''
        if self.Current_player == self.Player1:
            return self.Player2
        else:
            return self.Player1
        pass
        # TODO - better done with tags?


    def take_turn(self, Selected_attack):
        ''' completes a single game turn '''
        Attacker_mods = self.Current_player.Active_modifiers
        Defender_mods = self.return_opponent().Active_modifiers
        Hit_check = check_hit(Selected_attack, Attacker_mods, Defender_mods)

        # if the attack hits move on to the effects
        if Hit_check == True:
            Damage_dealt = calculate_damage(Selected_attack, Attacker_mods, Defender_mods)
            self.return_opponent().HP -= Damage_dealt
            # a modifier activates sometimes, half the time for now
            if random.random() > 1/2:
                New_mod = (value for value in Selected_attack.Modifier)
                if New_mod[3] == True: # check if modifier targets opponent
                    Defender_mods.append((self.Turn_number, New_mod))
                else:
                    Attacker_mods.append((self.Turn_number, New_mod))

        # game state update/check if game over
        self.check_game_state()
        if self.Game_active == False:
            return self.Winner

        # if game isn't over, update objects and move on to next turn
        else:
            self.Turn_number += 1
            self.update_modifiers()
            self.Current_player = self.return_opponent()
            return


    def check_game_state(self):
        ''' checks if game continues/selects winner '''
        # TODO
        pass


    def update_modifiers(self):
        ''' updates list of active modifiers for both players '''
        # TODO
        pass


    def copy(self):
        # TODO for minmax
        pass

def check_hit(Selected_attack, modifier):
    ''' decies if an attack will hit '''
    # TODO
    # return True/False
    pass

def calculate_damage(Selected_attack, Attacker_modifier, Defender_modifiers):
    ''' calculates the damage an attack deals '''
    # TODO
    # return damage dealt
    pass