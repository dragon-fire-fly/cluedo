import random
import time
from tabulate import tabulate

from gameboard import Gameboard

from cards import Cards

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

print("Start")
cards = Cards(CARDS, DEALT_CARDS)


print(cards.deal_cards())

# print(tabulate(game_board))

player = [1, 1]

gameboard = Gameboard(ROOM_LOCATIONS)

def number_input_validation(user_input, chosen_dict= None):
    """
    Takes an input and a relevant dictionary and prompts the user to choose an option.
    If the user input is valid, returns 
    """
    while True:
        if user_input == "suspect" or user_input == "weapon":
            choice = input(f"Which {user_input} would you like to investigate?: ")
            for k, v in chosen_dict.items():
                if choice == k:
                    return k
                elif choice == v:
                    return k
            print(f"Sorry, that is not a valid input, please enter a number between 1-{len(chosen_dict)}")


def y_n_input_validation(user_input):   
    """
    Takes user input and checks whether it is a valid yes or no answer
    """
    choice = user_input
    while True:
        if choice.lower() == "y" or choice.lower() == "yes":
            return True
        elif choice.lower() == "n" or choice.lower() == "no":
            print("Please make new choices for the investigation")
            time.sleep(1)
            return
        else:
            choice = input("Sorry, that was an invalid choice. y/n? ")



## Investigation phase

# need 1-6 validation
def investigate(player):
    """
    Allows the player to investigate other player's cards
    """
    player_location = gameboard.choose_room(player)
    current_room = gameboard.which_room(player)
    print(player)
    print("======== Investigation phase ========")
    confirm_choice = False
    while not confirm_choice:
        print(f"You are in the {current_room}\n ===== SUSPECTS =====")
        for num, suspect in SUSPECTS.items():
            print(num, suspect)
        suspect = number_input_validation("suspect", SUSPECTS)
        print("===== WEAPONS =====")
        for num, weapon in WEAPONS.items():
            print(num, weapon)
        weapon = number_input_validation("weapon", WEAPONS)
        
        print(f"Are you sure you want to investigate {SUSPECTS[suspect]} with the {WEAPONS[weapon]} in the {current_room}?")
        check_choice = input("y/n: ")
        confirm_choice = y_n_input_validation(check_choice)

        
investigate(player)