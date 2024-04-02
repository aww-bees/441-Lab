''' 
Lab 12: Beginnings of Reinforcement Learning

Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
from lab11.pygame_combat import run_turn
from lab11.turn_combat import Combat

def run_episode(player1, player2):
    season_one=[]
    currentGame=Combat()
    while not currentGame.gameOver:
        run_turn(currentGame, player1, player2)
        health_tuple=(player1.health, player2.health)
        reward=1 if player1.health>player2.health else 0
        if (player1.weapon==player2.weapon+1 or (player1.weapon==2 and player2.weapon==0)):
            reward=1
        elif (player1.weapon==player2.weapon):
            reward=.5
        else:
            reward=0

        season_one.append((player1.weapon, health_tuple, reward))
    return season_one