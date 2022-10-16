import random

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


print("Start")

player1 = (7, 1)

gameboard = Gameboard(ROOMS, player1)

gameboard.choose_room(player1)
