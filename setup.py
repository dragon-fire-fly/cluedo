# import built in modules
import os
import time

# import installed modules

# import custom modules
from gameboard import Gameboard
from cards import Cards
from players import AIPlayer, Player
from scorecard import Scorecard


# Constants for game:
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
    [
        "Dagger", 
        "Candlestick", 
        "Revolver", 
        "Rope", 
        "Lead piping", 
        "Spanner"
    ],
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
    "1": "Miss Scarlett",
    "2": "Colonel Mustard",
    "3": "Mrs. White",
    "4": "Reverend Green",
    "5": "Mrs. Peacock",
    "6": "Professor Plum",
}
WEAPONS = {
    "1": "Dagger",
    "2": "Candlestick",
    "3": "Revolver",
    "4": "Rope",
    "5": "Lead piping",
    "6": "Spanner",
}
ROOMS = {
    "1": "Kitchen",
    "2": "Ball Room",
    "3": "Conservatory",
    "4": "Dining Room",
    "5": "Billiard Room",
    "6": "Library",
    "7": "Lounge",
    "8": "Hall",
    "9": "Study",
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

scorecard = [[
    " ",
    "Miss Scarlett",
    "Col Mustard", 
    "Mrs White", 
    "Rev Green", 
    "Mrs Peacock", 
    "Prof Plum"
    ],[
        'Miss Scarlett',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Col Mustard',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Mrs White',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Rev Green',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Mrs Peacock',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Prof Plum',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
    ],[
        'Rope',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Lead piping',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Candlestick',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Dagger',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Spanner',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Revolver',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
    ],[
        'Main Hall',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Dining Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Billiard Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Ball Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Library',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Conservatory',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Study',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Lounge',  ' ',  ' ', ' ', ' ', ' ', ' '
    ],[
        'Kitchen',  ' ',  ' ', ' ', ' ', ' ', ' '
    ]]


# custom functions
def clear():
    os.system("clear")

player_starting_location = [1, 1]

# Welcome message, logo, back story etc.
clear()
print("Welcome to Cluedo")
time.sleep(1)

# Instatiate classes
gameboard = Gameboard(ROOM_LOCATIONS, player_starting_location)
cards = Cards(CARDS, DEALT_CARDS)
player = Player(SUSPECTS,WEAPONS)
scorecard = Scorecard(scorecard)

# deal the game cards
cards.deal_cards()
print(DEALT_CARDS)

# Ask user which player they want to play:
clear()
chosen_character = player.choose_character()
print(f"You have chosen {chosen_character}.")
time.sleep(1)
print("Shuffling cards...")
time.sleep(1)
clear()


# pop out the cards dealt to the chosen character
user_hand = DEALT_CARDS.pop(chosen_character)
print(f"Your cards are: \n\t- {user_hand[0]}\n\t- {user_hand[1]}\n\t- {user_hand[2]}")
time.sleep(2)
clear()
#print(DEALT_CARDS)

# for the other characters, instatiate ai characters and assign hands

ai_char_list = []
if DEALT_CARDS.get("Miss Scarlett"):
    miss_scarlett = AIPlayer("Miss Scarlett", DEALT_CARDS["Miss Scarlett"])
    ai_char_list.append(miss_scarlett)
if DEALT_CARDS.get("Colonel Mustard"):
    col_mustard = AIPlayer("Colonel Mustard", DEALT_CARDS["Colonel Mustard"])
    ai_char_list.append(col_mustard)
if DEALT_CARDS.get("Mrs. White"):
    mrs_white = AIPlayer("Mrs. White", DEALT_CARDS["Mrs. White"])
    ai_char_list.append(mrs_white)
if DEALT_CARDS.get("Reverend Green"):
    rev_green = AIPlayer("Reverend Green", DEALT_CARDS["Reverend Green"])
    ai_char_list.append(rev_green)
if DEALT_CARDS.get("Mrs. Peacock"):
    mrs_peacock = AIPlayer("Mrs. Peacock", DEALT_CARDS["Mrs. Peacock"])
    ai_char_list.append(mrs_peacock)
if DEALT_CARDS.get("Professor Plum"):
    prof_plum = AIPlayer("Professor Plum", DEALT_CARDS["Professor Plum"])
    ai_char_list.append(prof_plum)

#print(ai_char_list[0].check_cards())



