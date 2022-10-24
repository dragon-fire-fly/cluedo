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
    (("Kitchen*"), (" "), (" "), ("Ballroom"), (" "), (" "),
        ("Conservatory*")),
    ((" "), (" "), (" "), (" "), (" "), (" "), (" ")),
    ((" "), (" "), (" "), (" "), (" "), (" "), ("Billiard Room")),
    (("Dining Room"), (" "), (" "), (" "), (" "), (" "), (" ")),
    ((" "), (" "), (" "), (" "), (" "), (" "), ("Library")),
    ((" "), (" "), (" "), (" "), (" "), (" "), (" ")),
    (("Lounge*"), (" "), (" "), ("Main Hall"), (" "), (" "), ("Study*")),
)

scorecard_table = [[
    " ",
    "Miss Scarlett",
    "Colonel Mustard",
    "Mrs. White",
    "Reverend Green",
    "Mrs. Peacock",
    "Professor Plum"
    ], [
        'Miss Scarlett',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Colonel Mustard',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Mrs. White',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Reverend Green',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Mrs. Peacock',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Professor Plum',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
    ], [
        'Rope',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Lead piping',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Candlestick',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Dagger',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Spanner',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Revolver',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
    ], [
        'Main Hall',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Dining Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Billiard Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Ball Room',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Library',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Conservatory',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Study',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Lounge',  ' ',  ' ', ' ', ' ', ' ', ' '
    ], [
        'Kitchen',  ' ',  ' ', ' ', ' ', ' ', ' '
    ]]


# custom functions
def clear():
    os.system("clear")


def number_input_validation(no_options):
    """
    Takes a number as input and prompts the user to choose an option.
    If the user input is a number between 1 and the input, returns the number.
    """
    options = ""
    for num in range(1, no_options+1):
        if num != no_options:
            options += f"{str(num)}, "
        elif num == no_options:
            options = options.strip(", ")
            options += f" or {str(no_options)}"

    while True:
        user_ans = input(f"Your answer ({options}): ")
        # print(type(user_ans))

        for num in range(1, no_options+1):
            if user_ans == str(num):
                return str(num)
        print(
            f"Sorry, {user_ans} is not a valid input, please enter a number"
            f"between 1 and {no_options}."
            )


def main_menu():
    print(
        "Please select from the following options:"
        "\n1. Play Game (with story)"
        "\n2. Play Game (skip story)"
        "\n3. View Rules"
    )
    choice = number_input_validation(3)
    if choice == "1":
        game_setup()
        # Need to add background story
    elif choice == "2":
        game_setup()
    else:
        show_rules()


# Rules:
def show_rules():
    print("The rules will go here")
    pass


def game_setup():
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
    for card in enumerate(user_hand):
        scorecard.update_scorecard(chosen_character, user_hand[card[0]])
    print(
        f"Your cards are: \n\t- {user_hand[0]}\n\t- {user_hand[1]}\n\t"
        f"- {user_hand[2]}\n\nThese cards have been added to your scorecard "
        f"which can be viewed at any time."
        )
    ai_char_list = generate_ai_characters()
    print(f"You are {chosen_character} and you are playing against:")
    for char in ai_char_list:
        print(char.name)
    next = input(
        "Press 'S' to view scorecard. Press any other key to "
        "continue game: "
        )
    if next.lower() == 's':
        print(scorecard.show_scorecard())
        back_to_game = input("Press any key to continue game: ")
        if back_to_game or back_to_game == "":
            clear()
    else:
        clear()
    # print(DEALT_CARDS)


# for the other characters, instatiate ai characters and assign hands
def generate_ai_characters():
    global ai_char_list
    if DEALT_CARDS.get("Miss Scarlett"):
        miss_scarlett = AIPlayer("Miss Scarlett", DEALT_CARDS["Miss Scarlett"])
        ai_char_list.append(miss_scarlett)
    if DEALT_CARDS.get("Colonel Mustard"):
        col_mustard = AIPlayer(
            "Colonel Mustard", DEALT_CARDS["Colonel Mustard"]
            )
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
    return ai_char_list


player_starting_location = [1, 1]

# Instatiate classes
gameboard = Gameboard(ROOM_LOCATIONS, player_starting_location)
cards = Cards(CARDS, DEALT_CARDS)
player = Player(SUSPECTS, WEAPONS)
scorecard = Scorecard(scorecard_table)


ai_char_list = []
# deal the game cards
cards.deal_cards()
print(DEALT_CARDS)

# print(ai_char_list[0].check_cards())

# Welcome message, logo, back story etc.
clear()
print("Welcome to Cluedo")
# insert fancy welcome screen
time.sleep(1)
main_menu()
