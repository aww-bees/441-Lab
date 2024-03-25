""" Create PyGameAIPlayer class here"""
import random
import pygame

class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        return ord(random.choice([str(i) for i in range(10)]))


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer:
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        self.weapon=random.randint(0, 2)
        return self.weapon

