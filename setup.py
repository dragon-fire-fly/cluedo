# import built in modules
import os
import time

# import installed modules

# import custom modules
from gameboard import Gameboard
from cards import Cards
from players import AIPlayer, Player
from scorecard import Scorecard
from validation import clear, number_input_validation

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

scorecard_table = [
    [
        " ",
        "Miss Scarlett",
        "Colonel Mustard",
        "Mrs. White",
        "Reverend Green",
        "Mrs. Peacock",
        "Professor Plum",
    ],
    ["Miss Scarlett", " ", " ", " ", " ", " ", " "],
    ["Colonel Mustard", " ", " ", " ", " ", " ", " "],
    ["Mrs. White", " ", " ", " ", " ", " ", " "],
    ["Reverend Green", " ", " ", " ", " ", " ", " "],
    ["Mrs. Peacock", " ", " ", " ", " ", " ", " "],
    ["Professor Plum", " ", " ", " ", " ", " ", " "],
    [""],
    ["Dagger", " ", " ", " ", " ", " ", " "],
    ["Candlestick", " ", " ", " ", " ", " ", " "],
    ["Revolver", " ", " ", " ", " ", " ", " "],
    ["Rope", " ", " ", " ", " ", " ", " "],
    ["Lead piping", " ", " ", " ", " ", " ", " "],
    ["Spanner", " ", " ", " ", " ", " ", " "],
    [""],
    ["Kitchen", " ", " ", " ", " ", " ", " "],
    ["Ball Room", " ", " ", " ", " ", " ", " "],
    ["Conservatory", " ", " ", " ", " ", " ", " "],
    ["Billiard Room", " ", " ", " ", " ", " ", " "],
    ["Dining Room", " ", " ", " ", " ", " ", " "],
    ["Library", " ", " ", " ", " ", " ", " "],
    ["Lounge", " ", " ", " ", " ", " ", " "],
    ["Main Hall", " ", " ", " ", " ", " ", " "],
    ["Study", " ", " ", " ", " ", " ", " "],
]


def main_menu():
    menu_loop = True
    while menu_loop:
        print(
            "Please select from the following options:"
            "\n1. Play Game (with story)"
            "\n2. Play Game (skip story)"
            "\n3. View Rules"
        )
        choice = number_input_validation(3)
        if choice == "1" or choice == "2":
            menu_loop = False
            clear()
            if choice == "1":
                time.sleep(2)
                story()
                game_setup()
            elif choice == "2":
                game_setup()
        else:
            clear()
            show_rules()


def show_rules():
    clear()
    rule_1 = "1. The murderer, murder weapon and murder location have been \
placed inside the 'murder envelope'\n"
    rule_2 = "2. Roll the dice or use a secret passage each turn to move from \
room to room. You may move up, down or sideways, \n   but not diagonally. \n"
    rule_3 = "3. On your turn, if you are in a room, you may question the \
other suspects about any suspect, any weapon and \n   the location you are \
currently at.\n"
    rule_4 = "4. Starting with the player to your left, if that player has \
one of the three suggested cards, they must show you one. \n   If they don't \
have any cards, the player to their left is questioned next, and so on.\n"
    rule_5 = "5. Once you feel certain that you know the murderer, murder \
weapon and room, you may make an accusation. \n   You may only make one \
accusation per game.\n\n"
    rules = [rule_1, rule_2, rule_3, rule_4, rule_5]
    clear()
    print(LOGO)
    for rule in rules:
        for letter in rule:
            time.sleep(0.025)
            print(letter, end="", flush=True)
        time.sleep(0.5)

    input("Press enter to continue ")
    clear()


def game_setup():
    clear()
    chosen_character = player.choose_character()
    print(f"You have chosen to play as {chosen_character}.")
    player.set_starting_location(chosen_character)
    time.sleep(1)
    print("Shuffling cards...")
    time.sleep(1)
    clear()
    cards.deal_cards()

    # pop out the cards dealt to the chosen character
    user_hand = DEALT_CARDS.pop(chosen_character)
    for card in enumerate(user_hand):
        scorecard.update_scorecard(chosen_character, user_hand[card[0]])
    print(
        f"Your cards are: \n\t- {user_hand[0]}\n\t- {user_hand[1]}\n\t"
        f"- {user_hand[2]}\n\nThese cards have been added to your "
        f"investigation card which can be viewed at any time.\n"
    )
    generate_ai_characters()
    next = input(
        "\nEnter 'I' to view investigation card or press enter to "
        "continue game: "
    ).strip()
    if next.lower() == "i":
        scorecard.show_scorecard()
        back_to_game = input("Press enter to continue game: ")
        if back_to_game or back_to_game == "":
            clear()
    else:
        clear()


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


def story():
    story_1 = "You are attending a dinner party at the esteemed Dr Black's \
country Mansion for an evening of dinner, drinks,\ndancing and debauchery.\n"
    story_2 = "As the clock strikes midnight, a piercing scream \
reverberates throughout the Manor, caused by the discovery of \nDr \
Black's body. He has been murdered in cold blood.\n"
    story_3 = "You and the other five guests have gathered around Dr Black's \
body in the hallway, but something seems strange. \nThis is clearly not \
the scene of the crime.\nIn addition, a series of objects found around \
the Manor have been collected as potential murder weapons and lie \
\nstrewn around the body.\n"
    story_4 = "Your role now is to figure out WHO committed the crime, WHICH \
item was used and WHERE the murder took place. \n... and hopefully prove \
your innocence in the process!\n"
    story_5 = "Roll the die to move around the Mansion and perform \
investigations to eliminate suspects, items and locations \nin order to \
figure out the details of this murder most foul.\n"
    story_6 = "Once you think you know WHO, WHAT and WHERE, you may make an \
accusation. \nBe careful though, if you guess incorrectly, perhaps \
suspicion will fall on YOU.\n"
    story_7 = "Now what are you waiting for? There's no time to lose!\n"

    story_board_list = [story_1, story_2, story_3, story_4, story_5, story_6,
                        story_7]
    story_board = ""
    for story in story_board_list:
        clear()
        print(LOGO)
        print(story_board)
        story_board += story
        for letter in story:
            time.sleep(0.025)
            print(letter, end="", flush=True)

        input("\nPress enter to continue. ")
        clear()


# Instatiate classes
player_starting_location = [1, 1]
gameboard = Gameboard(ROOM_LOCATIONS, player_starting_location)
cards = Cards(CARDS, DEALT_CARDS, ["", "", ""])
player = Player(SUSPECTS, WEAPONS, ROOMS)
scorecard = Scorecard(scorecard_table)


ai_char_list = []


# print(ai_char_list[0].check_cards())

# Welcome message, logo, back story etc.
LOGO = """
 ██▓███ ▓██   ██▓ ▄████▄   ██▓     █    ██ ▓█████
▓██░  ██▒▒██  ██▒▒██▀ ▀█  ▓██▒     ██  ▓██▒▓█   ▀
▓██░ ██▓▒ ▒██ ██░▒▓█    ▄ ▒██░    ▓██  ▒██░▒███
▒██▄█▓▒ ▒ ░ ▐██▓░▒▓▓▄ ▄██▒▒██░    ▓▓█  ░██░▒▓█  ▄
▒██▒ ░  ░ ░ ██▒▓░▒ ▓███▀ ░░██████▒▒▒█████▓ ░▒████▒
▒▓▒░ ░  ░  ██▒▒▒ ░ ░▒ ▒  ░░ ▒░▓  ░░▒▓▒ ▒ ▒ ░░ ▒░ ░
░▒ ░     ▓██ ░▒░   ░  ▒   ░ ░ ▒  ░░░▒░ ░ ░  ░ ░  ░
░░       ▒ ▒ ░░  ░          ░ ░    ░░░ ░ ░    ░
         ░ ░     ░ ░          ░  ░   ░        ░  ░
         ░ ░     ░
"""
clear()
print("Welcome to .... ")
print(LOGO)

# insert fancy welcome screen
time.sleep(1)
main_menu()
