""" Create PyGameAIPlayer class here"""
import random
import pygame

class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        return random.randit(0, 9)


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer:
    def __init__(self, name):
        super().__init__(name)
        """self.initial_weapon = 1
        self.agentGuess=-1
        self.round=0
        self.opponentchoices=[]
        self.mychoices=[] """

    def weapon_selecting_strategy(self):
        while True:
            self.weapon=random.randint(0,2)
            return self.weapon

