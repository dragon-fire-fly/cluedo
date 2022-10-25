# import built in modules
import os
import random
import time
import copy

import setup
from validation import (
            clear,
            number_input_validation,
            number_dict_input_validation,
            y_n_input_validation
            )


# User player class
class Player:
    def __init__(self, suspect_dict, weapon_dict):
        self.suspect_dict = suspect_dict
        self.weapon_dict = weapon_dict

    def choose_character(self):
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

    def move_player(
        self,
        player_location,
        desired_room,
        current_room,
        die_roll,
        room_distances,
        room_dict,
    ):
        """
        Takes a player's current and desired location and moves
        the player towards the chosen room
        """
        # print(room_distances[desired_room])
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
        # print(room_distances[desired_room])
        else:
            total_die_roll = copy.deepcopy(die_roll)
            print(f"You have not rolled enough to reach the {desired_room}.")
            print(
                f"1. Move {die_roll} spaces towards the {desired_room}\n"
                f"2. Stay at current location"
            )
            stay_or_move = number_input_validation(2)

            if stay_or_move == "1":
                # Calculating where on the board the player will end up after
                # moving towards the chosen room
                while die_roll:
                    if room_dict[desired_room][0] - player_location[0] > 0:
                        die_roll -= 1
                        player_location[0] += 1
                    elif room_dict[desired_room][0] - player_location[0] < 0:
                        die_roll -= 1
                        player_location[0] -= 1
                    # left or right?
                    if die_roll:
                        if room_dict[desired_room][1] - player_location[1] > 0:
                            die_roll -= 1
                            player_location[1] += 1
                        elif room_dict[desired_room][1] - player_location[1] \
                                < 0:
                            die_roll -= 1
                            player_location[1] -= 1
                print("Moving...")
                time.sleep(1.5)
                print(
                    f"You have moved {total_die_roll} spaces towards the "
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
                return player_location

            elif stay_or_move == "2":
                if player_location in room_dict.values():
                    print(f"You have chosen to stay in the {current_room}.")
                else:
                    print("You have chosen to stay in the hallway.")
                return player_location

    def choose_investigation_cards(self, current_room, player_location=[1, 1]):
        """
        Allows the player to investigate other player's cards
        """
        clear()
        print("======== Investigation phase ========")
        confirm_choice = False
        while not confirm_choice:
            print(f"You are in the {current_room}\n\n ===== SUSPECTS =====")
            for num, suspect in self.suspect_dict.items():
                print(num, suspect)
            suspect = number_dict_input_validation(
                "suspect", self.suspect_dict
                )
            clear()
            print("===== WEAPONS =====")
            for num, weapon in self.weapon_dict.items():
                print(num, weapon)
            weapon = number_dict_input_validation("weapon", self.weapon_dict)

            clear()
            print(
                f"Are you sure you want to investigate "
                f"{self.suspect_dict[suspect]} with the "
                f"{self.weapon_dict[weapon]} in the {current_room}?"
            )
            check_choice = input("y/n: ").strip()
            confirm_choice = y_n_input_validation(check_choice)
        return [
            self.suspect_dict[suspect], self.weapon_dict[weapon], current_room
            ]

    def make_accusation():
        pass

    def roll_die(self):
        """
        Returns a random number between 1 and 6.
        """
        return random.randint(1, 6)


# AI Player class
class AIPlayer:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards