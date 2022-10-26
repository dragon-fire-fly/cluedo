import os
import time

import setup


def number_input_validation(no_options):
    """
    Takes a number as input and prompts the user to choose an option.
    If the user input is a number between 1 and the input, returns the number.
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


def number_dict_input_validation(user_input, chosen_dict, phase=None):
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
                    f"{phase}?:").strip()
        elif user_input == "character":
            choice = input(
                f"\nWhich character would you like to play?: ").strip()
        for k, v in chosen_dict.items():
            if choice == k:
                return k
            elif choice.lower() == v.lower():
                return k
        print(
            f"Sorry, that is not a valid input, please enter a number between "
            f"1-{len(chosen_dict)}"
        )


def y_n_input_validation(user_input):
    """
    Takes user input and checks whether it is a valid yes or no answer
    """
    choice = user_input
    while True:
        if choice.lower() in [
            "y",
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
            print("Please make new choices for the investigation")
            time.sleep(1.5)
            clear()
            return
        else:
            choice = input(f"Sorry, {choice} was an invalid choice. \
        y/n? ").strip()


def clear():
    os.system("clear")
