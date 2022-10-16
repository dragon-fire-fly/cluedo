import random
from tabulate import tabulate

from gameboard import Gameboard

# Room Locations on board
ROOMS = {
    "Kitchen": (1, 1),
    "Ball Room": (1, 4),
    "Conservatory": (1, 7),
    "Billiard Room": (3, 7),
    "Dining Room": (4, 1),
    "Library": (5, 7),
    "Lounge": (7, 1),
    "Main Hall": (7, 4),
    "Study": (7, 7),
}

game_board = (
(("Kitchen*"), (" "), (" "), ("Ballroom"), (" "), (" "), ("Conservatory*")),
((" "), (" "), (" "), (" "), (" "), (" "), (" ")),
((" "), (" "), (" "), (" "), (" "), (" "), ("Billiard Room")),
(("Dining Room"), (" "), (" "), (" "), (" "), (" "), (" ")),
((" "), (" "), (" "), (" "), (" "), (" "), ("Library")),
((" "), (" "), (" "), (" "), (" "), (" "), (" ")),
(("Lounge*"), (" "), (" "), ("Main Hall"), (" "), (" "), ("Study*"))
)

print("Start")
print(tabulate(game_board))

player = [4, 4]

gameboard = Gameboard(ROOMS, player)
print(f"Player is at {player}")

gameboard.choose_room(player)
print(f"Player is at {player}")

