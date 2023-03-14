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
        """we use _ because we don't care about the name; 
        we use () instead of [] to make it a generator expression, 
        which saves memory by only creating requested values instead
        of the entire list all at once
        """
        dice_throws = sorted(randint(1, 6) for _ in range(4)) 
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
