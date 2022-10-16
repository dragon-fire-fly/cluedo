import random
from tabulate import tabulate

from gameboard import Gameboard

# from cards import Cards

# Room Locations on board
ROOM_LOCATIONS = {
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

CARDS = [
    [
        "Colonel Mustard",
        "Professor Plum",
        "Reverend Green",
        "Mrs. Peacock",
        "Mrs. White",
        "Miss Scarlett",
    ],
    ["Dagger", "Candlestick", "Revolver", "Rope", "Lead piping", "Spanner"],
    [
        "Main Hall",
        "Study",
        "Billiard Room",
        "Lounge",
        "Library",
        "Kitchen",
        "Ball Room",
        "Conservatory",
        "Dining Room",
    ],
]

DEALT_CARDS = {
    "Miss Scarlett": [],
    "Colonel Mustard": [],
    "Mrs. White": [],
    "Reverend Green": [],
    "Mrs. Peacock": [],
    "Professor Plum": [],
}

SUSPECTS = {
    1: "Miss Scarlett",
    2: "Colonel Mustard",
    3: "Mrs. White",
    4: "Reverend Green",
    5: "Mrs. Peacock",
    6: "Professor Plum",
}
WEAPONS = {
    1: "Dagger",
    2: "Candlestick",
    3: "Revolver",
    4: "Rope",
    5: "Lead piping",
    6: "Spanner",
}
ROOMS = {
    1: "Kitchen",
    2: "Ball Room",
    3: "Conservatory",
    4: "Dining Room",
    5: "Billiard Room",
    6: "Library",
    7: "Lounge",
    8: "Hall",
    9: "Study",
}

game_board = (
    (("Kitchen*"), (" "), (" "), ("Ballroom"), (" "), (" "), ("Conservatory*")),
    ((" "), (" "), (" "), (" "), (" "), (" "), (" ")),
    ((" "), (" "), (" "), (" "), (" "), (" "), ("Billiard Room")),
    (("Dining Room"), (" "), (" "), (" "), (" "), (" "), (" ")),
    ((" "), (" "), (" "), (" "), (" "), (" "), ("Library")),
    ((" "), (" "), (" "), (" "), (" "), (" "), (" ")),
    (("Lounge*"), (" "), (" "), ("Main Hall"), (" "), (" "), ("Study*")),
)

print("Start")
# cards = Cards(CARDS, DEALT_CARDS)


# print(cards.dealt_cards)

# print(tabulate(game_board))

player = [4, 4]

gameboard = Gameboard(ROOM_LOCATIONS, player)
print(f"Player is at {player}")

gameboard.choose_room(player)
print(f"Player is at {player}")
