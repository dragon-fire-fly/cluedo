import random
import time
from tabulate import tabulate

from setup import player
from setup import gameboard

print("Start")

# print(tabulate(game_board))

player_location = [4, 1]


player.investigate(gameboard.which_room(player_location))