import sys
import pygame
import random
import matplotlib.pyplot as plt
import pygad
import numpy as np
from sprite import Sprite
from pygame_combat import run_pygame_combat
from pygame_human_player import PyGameHumanPlayer
from lab5.landscape import get_landscape, elevation_to_rgba, get_elevation
from pygame_ai_player import PyGameAIPlayer
from generate_sprites import generate_hero
from pathlib import Path
from lab3.travel_cost import get_route_cost
from lab7.ga_cities import setup_GA, game_fitness


sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab2.cities_n_routes import get_randomly_spread_cities, get_routes

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)


def get_landscape_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def get_combat_surface(game_map):
    
    landscape = elevation_to_rgba(game_map)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])


class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
        money,
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes
        self.money=random.randint(150, 250)


if __name__ == "__main__":
    generate_hero()
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = 9
    sprite_path = "hero_sprite.png"
    sprite_speed = 1

    screen = setup_window(width, height, "Game World Gen Practice")

    landscape_surface = get_landscape_surface(size)
    game_map = get_elevation(size)  #now can use travel cost in main
    combat_surface = get_combat_surface(game_map)
    city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]

    city_locations = get_randomly_spread_cities(size, len(city_names))
    routes = get_routes(city_locations)
    #FIX ROUTES HERE
    random.shuffle(routes)
    routes = routes[:3]
    required_routes = [(city_locations[0], city_locations[1]), (city_locations[1], city_locations[2]),
                       (city_locations[2], city_locations[3]), (city_locations[3], city_locations[4]), 
                       (city_locations[4], city_locations[5]), (city_locations[5], city_locations[6]), 
                       (city_locations[6], city_locations[7]), (city_locations[7], city_locations[8]),
                       (city_locations[8], city_locations[9]),]
    for reqd_route in required_routes:
        if reqd_route not in routes:
            routes.append(reqd_route)

    player_sprite = Sprite(sprite_path, city_locations[start_city])

    player = PyGameHumanPlayer()
    #Comment out above line and uncomment below to make AI play the game
    #player=PyGameAIPlayer()

    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=city_locations,
        routes=routes,
        money=200
    )

    while True:
        action = player.selectAction(state)
        if 0 <= int(chr(action)) <= 9:
            if int(chr(action)) != state.current_city and not state.travelling:
                ''' 
                Check if a route exist between the current city and the destination city.
                '''
                if (city_locations[state.current_city], city_locations[int(chr(action))]) not in routes and (city_locations[int(chr(action))], city_locations[state.current_city]) not in routes:
                    print("There's no roads to that city!")
                    continue

                start = city_locations[state.current_city]
                state.destination_city = int(chr(action))
                destination = city_locations[state.destination_city]
                travel_cost = round(abs(get_route_cost((start, destination), game_map)), 2)

                player_sprite.set_location(city_locations[state.current_city])
                state.travelling = True
                print(
                    "Travelling from", state.current_city, "to", state.destination_city, " costs $", travel_cost
                )
                state.money -= travel_cost
                print("You now have $", round(state.money, 2))

        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in city_locations:
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        displayCityNames(city_locations, city_names)
        if state.travelling:
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2
            if not state.travelling:
                print('Arrived at', state.destination_city)

        if not state.travelling:
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            #run_pygame_combat returns false if the player loses
            win = run_pygame_combat(combat_surface, screen, player_sprite)
            state.encounter_event = False
            if not win:
                print("You died and lost! Game over.")
                break
            else:
                loot = random.randrange(20)
                print("The bandit dropped $", loot)
                state.money+=loot
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.update()
        if state.money <= 0:
            print("You ran out of money! Game over.")
            break

        if state.current_city == end_city:
            print('You have reached the end of the game!')
            break
