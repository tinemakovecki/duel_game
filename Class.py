### - CLASSES - ###
# TODO connect class and game file

# ATTACK CLASS
class Attack():
    def __init__(self, Name, Damage, Hit_chance, Modifier): # modifier = (name, DMG effect, hit effect, target opponent)
        self.Name = Name
        self.Damage = Damage
        self.Hit_chance = Hit_chance
        self.Modifier = Modifier
        # TODO empty modifier?

    # methods for calling retrieving properties
    def Modifier_name(self):
        '''return the name of the modifier'''
        return self.Modifier[0]

    def Modifier_damage(self):
        '''return modifier effect on damage'''
        return self.Modifier[1]

    def Modifier_hit_chance(self):
        '''return modifier effect on hit chance'''
        return self.Modifier[2]

    def Modifier_target(self):
        '''return which player the modifier affects'''
        return self.Modifier[3]

# MONSTER CLASS
class Monster():
    def __init__(self, Name, HP, Attack1, Attack2, Attack3, Attack4): # the attack arguments should belong to Attack() class!
        self.Name = Name
        self.HP = HP
        self.Attack1 = Attack1
        self.Attack2 = Attack2
        self.Attack3 = Attack3
        self.Attack4 = Attack4

# CONSTRUCTION FUNCTIONS
def createChar():
    '''constructs and returns Monster "charmander" '''
    # create the attacks first
    # attack = (name, damage, hit chance, modifier)
    # modifier = (name, DMG effect, hit effect, target opponent)
    Attack1 = Attack('Fire', 55, 70, ('Burn', -15, -5, True))
    Attack2 = Attack('Scratch', 50, 80, ('Bleed', -10, 0, True))
    Attack3 = Attack('Kick', 45, 70, ('Knockdown', -5, -12, True))
    Attack4 = Attack('Bite', 60, 60, ('Frenzy', 10, 0, False))

    # monster = (name, HP, attack1, attack2, attack3, attack4)
    Char = Monster('charmander', 500, Attack1, Attack2, Attack3, Attack4)

    return Char


def createPika():
    '''constructs and returns Monster "pikachu" '''
    # create the attacks first
    # attack = (name, damage, hit chance, modifier)
    # modifier = (name, DMG effect, hit effect, target opponent)
    Attack1 = Attack('Lightning', 70, 60, ('Shock', -10, -10, True))
    Attack2 = Attack('Scratch', 50, 80, ('Bleed', -10, 0, True))
    Attack3 = Attack('Tackle', 50, 67, ('Knockdown', -5, -12, True))
    Attack4 = Attack('Paralyze', 20, 80, ('Paralysis', -10, -25, True))

    # monster = (name, HP, attack1, attack2, attack3, attack4)
    Pika = Monster('pikachu', 500, Attack1, Attack2, Attack3, Attack4)

    return Pika

# TODO other construction functions
