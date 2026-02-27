"""D&D Character"""

import random


class Character:
    """A basic Dungeon's and Dragons character"""
    def __init__(self):
        self.strength = best_3_of_4()
        self.dexterity = best_3_of_4()
        self.constitution = best_3_of_4()
        self.intelligence = best_3_of_4()
        self.wisdom = best_3_of_4()
        self.charisma = best_3_of_4()

        con_mod = modifier(self.constitution)
        self.hitpoints = 10 + con_mod

    def ability(self):
        """An arbitrary ability"""
        return best_3_of_4()


def best_3_of_4():
    """Returns the sum of the best 3 results from rolling 4 six-sided dice"""
    rolls = []
    for _ in range(4):
        rolls.append(random.randint(1, 6))
    rolls.remove(min(rolls))
    return sum(rolls)


def modifier(number):
    return (number - 10) // 2
