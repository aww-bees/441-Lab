# Abstract
This is a game in which the hero, the player character, journeys through the country and fights bandits as they travel from Morkomasto to Forthyr. In doing so, several artificial intelligence components are utilized to make the experience of playing the game change each time.

The game includes money, a travel cost when using routes, and thirteen routes, three of which are random. Random battles with bandits can occur while traveling. If the player dies in battle or runs out of money, they lose. If the player successfully reaches the ninth city, Forthyr, they win.

The game takes input in the form of numbers when traveling. If the number corresponds to a city they can go to, the sprite is moved to that location and the travel cost is deducted. If the player enters combat, they may enter 'S', 'A', or 'F' to attack the bandit. Upon defeating the bandit, the player receives a small, random amount of money and returns to travel mode.

# AI Components
OpenAI's DALL-E 2
Perlin noise (not AI)
Pygad -- Genetic Algorithms
AI Agent

# Problems Solved
OpenAI's DALL-E is a text to image generator. In this project, a prompt is sent to DALL-E, which responds with a json file with base64 encoding. Pillow is used to process the json file, and save it as a png. I've created two functions for this program -- generate_hero and generate_bandit, which create the sprites for the adventurer and the enemies respectively. This allows the user to have interesting new sprites every time they play. For further notes regarding the operation of the DALL-E component, read the Usage section.

Perlin Noise is not counted as artificial intelligence, though it is important to the project. Perlin noise creates a procedurally generated landscape that is natural looking and allows for the implementation of travel cost that isn't entirely random (instead, it's related to elevation changes).

Pygad's genetic algorithm is used to create more ideal city placement. The fitness function encourages the cities to be further away from each other (preventing overlap), not too high (on mountains), and not too low (underwater). This creates a more realistic looking city layout.

Unused in the final product, but an AI agent can be created to allow for an automated playthrough of the game. This agent undergoes 10,000 episodes of reinforcement to ensure it can win combat encounters.
# Usage 
The sprite generation for this program requires the use of DALL-E 2.

For the sprite generation, the user must run "pip install --upgrade openai" for image generation and "pip install pillow" for image processing. Even if openai is installed, the command above should be run to ensure it's up to date.

It is possible, though extreme unlikely, my OpenAI account runs out of funds, in which case the sprite generation will not function. If this happens, or the program must be run many times for testing, comment out line 75 in agent_environment.py and line 11 in pygame_combat.py. This will make the sprite files stop generating, but as long as one exists for the player character and the bandit, the game should function as intended.

# Appendix
I did not use ChatGPT in the creation of this report.
