# import built in modules
import time

# import custom modules
from setup import (
    player,
    ai_char_list,
    scorecard,
    gameboard,
    ROOM_LOCATIONS,
    cards
    )
from validation import number_input_validation, clear


def main_game_loop(hours_remaining):
    player_location = gameboard.current_player_location()
    print(f"You have {hours_remaining} hour(s) remaining...")
    time.sleep(2)
    # obtain current room
    current_room = gameboard.which_room()
    # die roll for the turn:
    turn_die_roll = player.roll_die()
    print(f"You are currently in the {current_room}.\n")
    print("Rolling die....")
    time.sleep(2)
    clear()
    print(
        f"You are currently in the {current_room}.\nYou have rolled a "
        f"{turn_die_roll}.\n"
    )
    # ask user for desired room
    desired_room, room_distances = gameboard.choose_room()

    # move towards the desired room
    new_player_location = player.move_player(
        player_location,
        desired_room,
        current_room,
        turn_die_roll,
        room_distances,
        ROOM_LOCATIONS,
    )
    gameboard.update_player_location(new_player_location)
    # check whether in a room or in hallway (and if so, end turn)
    current_room = gameboard.which_room()

    if current_room in ROOM_LOCATIONS:
        investigation_list = player.choose_investigation_cards(current_room)
        investigate(investigation_list)
    else:
        print("End of turn")


def investigate(investigation_cards):
    character_name = ""
    card_to_show = ""
    for character in ai_char_list[::-1]:
        for card in investigation_cards:
            if card == character.cards[0]:
                character_name = character.name
                card_to_show = card
            elif card == character.cards[1]:
                character_name = character.name
                card_to_show = card
            elif card == character.cards[2]:
                character_name = character.name
                card_to_show = card
    if not character_name and not card_to_show:
        print("No other characters had any cards to show.")
        input("Press enter to continue ")
    else:
        if character_name in ["Miss Scarlett", "Mrs. White", "Mrs. Peacock"]:
            pronoun = "she"
            pronoun2 = "her"
        else:
            pronoun = "he"
            pronoun2 = "his"

        print(
            f"\n{character_name} has one or more investigation cards in "
            f"{pronoun2} hand. {pronoun.capitalize()} showed you the "
            f"{card_to_show} card.\n"
            "Your investigation card has been updated."
        )
        scorecard.update_scorecard(character_name, card_to_show)
        input("\nPress enter to continue. ")


def end_of_turn():
    global hours_remaining
    clear()
    print("It's the end on your turn, What would you like to do?")
    print("1. End turn\n2. Make accusation\n3. View investigation card ")
    choice = number_input_validation(3)
    if choice == "3":
        scorecard.show_scorecard()
        print("It's the end on your turn, What would you like to do?")
        print("1. End turn\n2. Make accusation ")
        choice = number_input_validation(2)
    if choice == "2":
        print("")
        accusation = player.make_accusation()
        if accusation != []:
            clear()
            print(
                f"You have chosen: {accusation[0]}, {accusation[1]} and \
{accusation[2]}."
            )
            time.sleep(1)
            win_or_lose = cards.check_murder_envelope(accusation)
            hours_remaining = 0
            return win_or_lose
        else:
            clear()
    else:
        clear()


hours_remaining = 24

if __name__ == "__main__":
    while hours_remaining >= 1:
        main_game_loop(hours_remaining)
        result = end_of_turn()
        hours_remaining -= 1
        clear()
        if hours_remaining == 0 or result == "lose":
            end_1 = "The clock strikes midnight once again and the air around \
you grows cold.\n\nSadly your investigation efforts were not enough to find \
the culprit this time. \nYou'd better hope that the professional \
investigation finds you innocent."
            end_2 = "..."
            end_3 = "You ARE innocent... right? \n"
            end_list = [end_1, end_2, end_3]
            end_message = ""
            for part in end_list:
                clear()
                print(end_message)
                time.sleep(1)
                end_message += part
                for letter in part:
                    time.sleep(0.025)
                    print(letter, end="", flush=True)

    print("\nThank you for playing PyClue!\n\
If you would like to play again, please click the orange 'Run Program' \
button at the top of the screen to restart.")
    time.sleep(1)
    print("Goodbye!")
