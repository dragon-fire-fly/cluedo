# import built in modules
import random
import time
import copy

import setup
from validation import (
    clear,
    number_input_validation,
    number_dict_input_validation,
    y_n_input_validation,
)


class Player:
    def __init__(self, suspect_dict: dict, weapon_dict: dict, room_dict: dict):
        self.suspect_dict = suspect_dict
        self.weapon_dict = weapon_dict
        self.room_dict = room_dict

    def choose_character(self) -> str:
        """
        Allows the user to choose which character they want to play.
        """
        print("====== PLAYERS ======")
        for num, player in self.suspect_dict.items():
            print(num, player)
        user_character_choice = number_dict_input_validation(
            "character", self.suspect_dict
        )
        return self.suspect_dict[user_character_choice]

    def set_starting_location(self, character: str) -> None:
        starting_location = [1, 1]
        if character == "Miss Scarlett":
            starting_location = [1, 4]
        elif character == "Colonel Mustard":
            starting_location = [3, 7]
        elif character == "Mrs. White":
            starting_location = [1, 1]
        elif character == "Reverend Green":
            starting_location = [1, 7]
        elif character == "Mrs. Peacock":
            starting_location = [7, 1]
        elif character == "Professor Plum":
            starting_location = [7, 7]
        setup.gameboard.update_player_location(starting_location)

    def roll_die(self) -> int:
        """
        Returns a random number between 1 and 6.
        """
        return random.randint(1, 6)

    def move_player(
        self,
        player_location: list[int],
        desired_room: str,
        current_room: str,
        die_roll: int,
        room_distances: dict[str, int],
        room_dict: dict[str, tuple],
    ) -> list[int]:
        """
        Takes a player's current and desired location and moves
        the player towards the chosen room
        """
        if die_roll >= int(room_distances[desired_room]):
            player_location = list(room_dict[desired_room])
            if current_room != desired_room:
                print(f"Walking to the {desired_room}...")
                time.sleep(2)
                clear()
                print(f"You are now in the {desired_room}")
            else:
                clear()
                print(f"You chose to remain in the {desired_room}")
                time.sleep(1)
            return player_location
        else:
            total_die_roll = copy.deepcopy(die_roll)
            print(f"You have not rolled enough to reach the {desired_room}.")
            print(
                f"1. Move {die_roll} space(s) towards the {desired_room}\n"
                f"2. Stay at current location"
            )
            stay_or_move = number_input_validation(2)

            if stay_or_move == "1":
                while die_roll:
                    if room_dict[desired_room][0] - player_location[0] > 0:
                        die_roll -= 1
                        player_location[0] += 1
                    elif room_dict[desired_room][0] - player_location[0] < 0:
                        die_roll -= 1
                        player_location[0] -= 1
                    if die_roll:
                        if room_dict[desired_room][1] - player_location[1] > 0:
                            die_roll -= 1
                            player_location[1] += 1
                        elif room_dict[desired_room][1] - player_location[1]\
                                < 0:
                            die_roll -= 1
                            player_location[1] -= 1
                clear()
                print("Moving...")
                time.sleep(1.5)
                print(
                    f"You have moved {total_die_roll} space(s) towards the "
                    f"{desired_room}"
                )
                if current_room not in room_dict.keys():
                    time.sleep(1)
                    print("You are still in the hallway")
                    time.sleep(1)
                else:
                    time.sleep(1)
                    print("You are now in the hallway")
                    time.sleep(1)
                input("\nPress enter to continue ")
                return player_location

            elif stay_or_move == "2":
                if tuple(player_location) in room_dict.values():
                    print(f"You have chosen to stay in the {current_room}.")
                    time.sleep(1)
                else:
                    print("You have chosen to stay in the hallway.")
                    time.sleep(1)
            return player_location

    def choose_investigation_cards(self, current_room: str) -> list[str]:
        """
        Allows the player to choose a suspect and a weapon to investigate
        """
        clear()
        print("======== Investigation phase ========")
        confirm_choice = False
        suspect = ""
        weapon = 2
        while not confirm_choice:
            print(f"You are in the {current_room}\n\n ===== SUSPECTS =====")
            for num, suspect in self.suspect_dict.items():
                print(num, suspect)
            suspect = number_dict_input_validation(
                "suspect", self.suspect_dict, "investigation"
            )
            clear()
            print("===== WEAPONS =====")
            for num, weapon in self.weapon_dict.items():
                print(num, weapon)
            weapon = number_dict_input_validation(
                "weapon", self.weapon_dict, "investigation"
            )
            clear()
            print(
                f"Are you sure you want to investigate "
                f"{self.suspect_dict[suspect]} with the "
                f"{self.weapon_dict[weapon]} in the {current_room}?"
            )
            confirm_choice = y_n_input_validation("investigation")
        return [
            self.suspect_dict[suspect],
            self.weapon_dict[weapon],
            current_room
            ]

    def make_accusation(self) -> list[str]:
        clear()
        print("===== SUSPECTS =====")
        for num, suspect in self.suspect_dict.items():
            print(num, suspect)
        suspect = number_dict_input_validation(
            "suspect", self.suspect_dict, "accusation"
        )
        clear()
        print("===== WEAPONS =====")
        for num, weapon in self.weapon_dict.items():
            print(num, weapon)
        weapon = number_dict_input_validation(
            "weapon", self.weapon_dict, "accusation"
            )
        clear()
        print("===== ROOMS =====")
        for num, room in self.room_dict.items():
            print(num, room)
        room = number_dict_input_validation(
            "room", self.room_dict, "accusation"
            )
        clear()
        print(
            f"Are you sure you want to accuse "
            f"{self.suspect_dict[suspect]} with the "
            f"{self.weapon_dict[weapon]} in the {self.room_dict[room]}?"
            f"\nYou may only make one accusation per game."
        )
        confirm_choice = y_n_input_validation("accusation")
        accusation = []
        if confirm_choice is True:
            accusation = [
                self.suspect_dict[suspect],
                self.weapon_dict[weapon],
                self.room_dict[room],
            ]
        return accusation


class AIPlayer:
    def __init__(self, name: str, cards: list[str]):
        self.name = name
        self.cards = cards
