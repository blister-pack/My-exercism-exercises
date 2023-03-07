from ast import Mod

from random import randint


class Character:
    def __init__(self):
        self.strength = randint(3, 18)
        self.dexterity = randint(3, 18)
        self.constitution = randint(3, 18)
        self.intelligence = randint(3, 18)
        self.wisdom = randint(3, 18)
        self.charisma = randint(3, 18)
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return self.wisdom


def modifier(con):
    hp_modifier = (con - 10) / 2
    if (abs(hp_modifier) - 0.5) == abs(int(hp_modifier)):
        return round(hp_modifier - 0.1)
    else:
        return round(hp_modifier)


# ---------------------------------------------------------
char1 = Character()
print(char1.constitution)
print(char1.hitpoints)
# modifier(5)
print(modifier(5))
