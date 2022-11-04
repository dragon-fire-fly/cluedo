import os
import time

import setup


def number_input_validation(no_options: int) -> str:
    """
    Takes a number as input and prompts the user to choose an option.
    If the user input is a number between 1 and the input, returns the
    number as a string.
    """
    options = ""
    for num in range(1, no_options + 1):
        if num != no_options:
            options += f"{str(num)}, "
        elif num == no_options:
            options = options.strip(", ")
            options += f" or {str(no_options)}"

    while True:
        user_ans = input(f"Your answer ({options}): ").strip()

        for num in range(1, no_options + 1):
            if user_ans == str(num):
                return str(num)
        print(
            f"Sorry, {user_ans} is not a valid input, please enter a number "
            f"between 1 and {no_options}."
        )


def room_choice_input_validation(no_options: int) -> int:
    """
    Takes a number as input and prompts the user to choose an option.
    If the user input is a number between 1 and the input, returns the number.
    If the user input is "i" or "I", show the scorecard.
    """
    while True:
        user_ans = input(
            f"\nEnter 1 - {no_options} to choose a room or enter 'I' to view "
            "the investigation card: "
        ).strip()
        if user_ans.isnumeric():
            for num in range(1, no_options + 1):
                if user_ans == str(num):
                    return int(user_ans)
            print(
                f"Sorry, '{user_ans}' is not a valid input, please enter "
                f"'I' or a number between 1 and {no_options}."
            )
        elif user_ans == "i" or user_ans == "I":
            setup.scorecard.show_scorecard()
        else:
            print(
                f"Sorry, '{user_ans}' is not a valid input, please enter "
                f"'I' or a number between 1 and {no_options}."
            )


def number_dict_input_validation(
    user_input: str, chosen_dict: dict, phase=None
        ) -> str:
    """
    Takes an input and a relevant dictionary and prompts the user to choose
    an option. If the user input is valid, returns the key of the chosen
    dictionary. Else prompts for new input.
    """
    while True:
        choice = ""
        if user_input in ["suspect", "weapon", "room"]:
            choice = input(
                f"\nWhich {user_input} would you like to include in your "
                f"{phase}? (press 'I' to view investigation card): "
            ).strip()
            if choice == "i" or choice == "I":
                setup.scorecard.show_scorecard()
                choice = input(
                    f"\nWhich {user_input} would you like to include in your "
                    f"{phase}?:"
                ).strip()
        elif user_input == "character":
            choice = input(
                f"\nWhich character would you like to play?: "
                ).strip()
        for k, v in chosen_dict.items():
            if choice == k:
                return k
            elif choice.lower() == v.lower():
                return k
        print(
            f"Sorry, {choice} is not a valid input, please enter a number \
                between 1-{len(chosen_dict)}"
        )


def y_n_input_validation(phase: str) -> bool:
    """
    Takes user input and checks whether it is a valid yes or no answer
    """

    while True:
        choice = input("y/n: ").strip()
        if choice.lower() in [
            "y",
            "ye",
            "yes",
            "yeah",
            "ok",
            "aye",
            "aye aye captain",
            "definitely",
        ]:
            return True
        elif choice.lower() in [
            "n",
            "no",
            "nah",
            "nope",
            "no way",
            "no way José",
            "nay",
        ]:
            if phase == "investigation":
                print(f"Please make new choices for the {phase}")
                time.sleep(1.5)
                clear()
                return False
            elif phase == "accusation":
                print(f"No {phase} made this round")
                time.sleep(1.5)
                return False
            elif phase == "end of game":
                return False
        print(f"Sorry, {choice} was an invalid choice.")


def clear():
    os.system("clear")
