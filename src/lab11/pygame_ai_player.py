""" Create PyGameAIPlayer class here"""
import random
from turn_combat import CombatPlayer
import pygame

class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        return ord(random.choice([str(i) for i in range(10)]))


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        self.weapon=random.randint(0, 2)
        return self.weapon

