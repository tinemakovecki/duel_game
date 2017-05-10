### - CLASSES - ###


# ATTACK CLASS
class Attack:
    def __init__(self, name, damage, hit_chance, modifier): # modifier = (name, DMG effect, hit effect, target opponent)
        self.name = name
        self.damage = damage
        self.hit_chance = hit_chance
        self.modifier = modifier
        # TODO empty modifier?

    # methods for calling retrieving properties
    def modifier_name(self):
        """ return the name of the modifier"""
        return self.modifier[0]

    def modifier_damage(self):
        """ return modifier effect on damage"""
        return self.modifier[1]

    def modifier_hit_chance(self):
        """ return modifier effect on hit chance"""
        return self.modifier[2]

    def target_opponent(self):
        """ checks if the modifier affects the opponent"""
        # if it doesn't target the opponent it's modifies the active player
        return self.modifier[3]


# MONSTER CLASS
class Monster:
    def __init__(self, name, hp, attack1, attack2, attack3, attack4): # the attack arguments should belong to Attack() class!
        self.name = name
        self.hp = hp # TODO seperate current and full health?
        self.attack1 = attack1
        self.attack2 = attack2
        self.attack3 = attack3
        self.attack4 = attack4
        self.active_modifiers = []


# CONSTRUCTION FUNCTIONS
def create_char():
    """ constructs and returns Monster "charmander" """
    # create the attacks first
    # attack = (name, damage, hit chance, modifier)
    # modifier = (name, DMG effect, hit effect, target opponent)
    attack1 = Attack('Fire', 55, 70, ('Burn', -15, -5, True))
    attack2 = Attack('Scratch', 50, 80, ('Bleed', -10, 0, True))
    attack3 = Attack('Kick', 45, 70, ('Knockdown', -5, -12, True))
    attack4 = Attack('Bite', 60, 60, ('Frenzy', 10, 0, False))

    # monster = (name, HP, attack1, attack2, attack3, attack4)
    char = Monster('Charmander', 500, attack1, attack2, attack3, attack4)

    return char


def create_pika():
    """ constructs and returns Monster "pikachu" """
    # create the attacks first
    # attack = (name, damage, hit chance, modifier)
    # modifier = (name, DMG effect, hit effect, target opponent)
    attack1 = Attack('Lightning', 70, 60, ('Shock', -10, -10, True))
    attack2 = Attack('Scratch', 50, 80, ('Bleed', -10, 0, True))
    attack3 = Attack('Tackle', 50, 67, ('Knockdown', -5, -12, True))
    attack4 = Attack('Paralyze', 20, 80, ('Paralysis', -10, -25, True))

    # monster = (name, HP, attack1, attack2, attack3, attack4)
    pika = Monster('Pikachu', 500, attack1, attack2, attack3, attack4)

    return pika


def copy_monster(monster):
    """ returns a copy of the given monster """
    # generate a monster of the right type
    if monster.name == 'Pikachu':
        monster_copy = create_pika()
    elif monster.name == 'Charmander':
        monster_copy = create_char()

    # change life and modifier to match the given monster's
    monster_copy.hp = monster.hp
    monster_copy.active_modifiers = [mod for mod in monster.active_modifiers]
    # TODO copy mods?

    # return the copy
    return monster_copy


# UTILITY
def possible_attacks(monster):
    """ returns a list of the attacks a monster can make """
    attacks = [monster.attack1, monster.attack2, monster.attack3, monster.attack4]
    return attacks