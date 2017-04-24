### GAME LOGIC FILE
import random

Player_1 = "1"
Player_2 = "2"
Not_over = "game isn't over"


class Game():
    def __init__(self):
        # players are the same monster for now
        self.Player_1 = Monster('Pik')
        self.Player_2 = Monster('Char')
        self.Active_modifiers1 = {} # (modifier, turn started) # TODO check if modifier is over each turn
        self.Active_modifiers2 = {}
        # saving player character data somewhere else?

        self.Current_player = Player_1
        self.Game_active = True
        self.Turn_number = 0

    def copy(self):
        '''returns a game copy'''
        ## TODO for minmax
        pass

    def take_turn(self, Selected_attack):
        '''does one game turn'''
        # miss/hit -> deal damage -> check game state -> next turn
        # TODO unified attack names for reference
        self.Turn_number += 1
        self.update_modifiers()

        # checking hit/miss
        Chance = Selected_attack[1] #   TODO better name for chance
        Hit = hit_check(Chance, self.Active_modifiers)

        # dealing damage
        if Hit == True:
            Damage = calculate_damage(Selected_attack, self.Active_modifiers)
            self.Opponent(self.Current_player).HP -= Damage

        # activating new modifiers
        if random.random() < 0.3:
            Modifier_try = Player_1.Modifiers[self.Current_player[Selected_attack[2]]] #recimo, da je tut selected_attack samo ime!
            if self.Opponent(self.Current_player) == self.Player1:
                if Selected_attack[2][2] == "opponent":
                    self.Active_modifiers1[Selected_attack[2]] #TODO finish <- this
                elif Selected_attack[2][2] == "self":
                    self.Active_modifiers2[Selected_attack[2]]
            else:
                self.Active_modifiers1
                self.Active_modifiers2


        # checks the game state
        Winner = self.check_game_state()
        if self.Game_active == True:
            self.Current_player = self.Opponent(self.Current_player)
            return "Not over"
        else:
            self.Current_player = None
            return Winner


    def check_game_state(self):
        '''describes game state, possible game over'''
        # check if HP > 0, if not -> self.Game_active = False
        if self.Opponent(self.Current_player).HP <= 0:
            self.Game_active = False
            return self.Current_player # return not self.player but player?!
        return "Not over"
        # TODO better names?

    def Opponent(self, player): # TODO: CHECK PLAYER_1 PLAYER2 ... MIX UP!!!!!!!!!!!!!!!!!!!!!!!!!
        '''returns the opponent of the current player'''
        if player == self.Player_1:
            return self.Player_2
        elif player == self.Player_2:
            return self.Player_1
        else:
            assert False, "invalid opponent"

    def update_modifiers(self):
        '''checks active modifiers and removes expired ones'''
        for mod in self.Active_modifiers1:
            if self.Turn_number - mod[1] < 3:
                del self.Active_modifiers1[mod]

        for mod in self.Active_modifiers2:
            if self.Turn_number - mod[1] < 3:
                del self.Active_modifiers2


def hit_check(player, attack_chance, modifiers): # TODO attack as paramaeter instead of attack chance?
    '''checks if an attack hits or misses'''
    if len(modifiers) == 0:
        modifier_effect = 1
    hit_chance = attack_chance * modifier_effect / 100
    return random.random() < hit_chance

# TODO calculate modifier effect
def calculate_damage(attack_damage, modifiers):
    '''calculates the damage of an attack'''
    if len(modifiers) == 0:
        modifier_effect = 1
    damage_dealt = attack_damage * modifier_effect
    return damage_dealt


#### MONSTER CLASS - WILL BE IN OWN FILE

class Monster():
    def __init__(self, Name):
        self.Name = Name
        self.HP = 10000
        # TODO attack names
        self.attack1 = (50, 50, "knockdown")
        self.attack2 = (20, 80, "blind")
        self.attack3 = (90, 5, "focus")
        self.attack4 = (10, 90, "berserk")

        # TODO modifiers
        # meaning: knockdown(accuracy: -10, damage: -5)
        # percent accuracy/damage reduction?
        self.modifiers = {"knockdown": (-10, -5, "opponent"), "blind":(-20, 0, "opponent"), "focus":(10, 0, "self"), "berserk":(-10, 10, "both")}


    # TODO define modifiers as subclass???
    # TODO try to fix
    #def change_attack(self, old_attack, new_attack):
    #    '''changes an attack of a monster'''
    #    # not sure if need
    #    self.old_attack = new_attack

    #def attack_damage(self, attack):
    #    '''returns attack damage'''
    #    return self.attack[0]

    #def hit_chance(self, attack):
    #    '''returns hit chance'''
    #    return self.attack[1]

Pikachu = Monster('Pikachu')