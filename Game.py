### GAME LOGIC FILE
import random

Player_1 = "1"
Player_2 = "2"
Not_over = "game isn't over"

def opponent(Current_player):
    '''returns the opponent of the current player'''
    if Current_player == Player_1:
        return Player_2
    elif Current_player == Player_2:
        return Player_1
    else:
        assert False, "invalid opponent"

class Game():
    def __init__(self):
        # attacks written as (damage, hit chance)
        self.Player_1 = {HP: 100, attack1: (20, 80), attack2: (10, 90), attack3: (50, 40), attack4: (90, 5), modifiers: []}
        self.Player_2 = {HP: 100, attack1: (20, 80), attack2: (10, 90), attack3: (50, 40), attack4: (90, 5), modifiers: []}
        # saving player character data somewhere else?

        self.Active_player = Player_1

    def copy(self):
        '''returns a game copy'''
        ## TODO for minmax
        pass

    def take_turn(self, Selected_attack):
        '''does one game turn'''
        # miss/hit -> deal damage -> check game state -> next turn
        # TODO unified attack names for reference
        # hit/miss
        base_hit_chance = self.Active_player[Selected_attack][1]
        # hit_chance = base_hit_chance * modifier_effect
        hit = random.random() < base_hit_chance # TODO check what exactly random function does

        # dealing damage
        if hit:
            damage = self.Active_player[Selected_attack][0]# is going to be: calculate_damage(Selected_attack, modifiers)
            self.opponent(self.Active_player)[HP] -= damage

        # check game state
        winner = self.game_state()
        if winner == Not_over:
            self.Active_player = self.opponent(self.Active_player)
        else:
            self.Active_player = None
        return winner

        pass


    def game_state(self):
        '''describes game state, possible game over'''
        # check if HP > 0
        # return "winner/Not_over"
        pass

def calculate_damage(attack, modifiers):
    '''calculates the damage of an attack'''
    pass

