from random import randint


class Character:
    def __init__(self):
        self.strength = (
            self.ability()
        )  #  if we didn't use the self. it would look for a
        self.dexterity = (
            self.ability()
        )  #  function ability() defined outside the class, which doesn't exist
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dice_throws = [randint(1, 6) for dice in range(4)]
        dice_throws.sort()
        dice_throws.remove(dice_throws[0])
        return sum(dice_throws)


def modifier(con):
    return (con - 10) // 2


# ---------------------------------------------------------
char1 = Character()
print(char1.constitution)
print(char1.hitpoints)
# modifier(5)
print(modifier(5))
print(char1.ability())
