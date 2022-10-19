import time
import random
import os
import copy

def number_dict_input_validation(user_input, chosen_dict= None):
    """
    Takes an input and a relevant dictionary and prompts the user to choose an option.
    If the user input is valid, returns the key of the chosen dictionary. Else prompts for new input
    """
    while True:
        if user_input == "suspect" or user_input == "weapon":
            choice = input(f"Which {user_input} would you like to investigate?: ")
        elif user_input == "character":
            choice = input(f"Which character would you like to play?: ")
        for k, v in chosen_dict.items():
            if choice == k:
                return k
            elif choice == v:
                return k
        print(f"Sorry, that is not a valid input, please enter a number between 1-{len(chosen_dict)}")

def number_input_validation(user_input):
    """
    Takes a number as input and prompts the user to choose an option.
    If the user input is a number between 1 and the input, returns the number.
    """
    options = ""
    for num in range(1, user_input+1):
        if num != user_input:
            options += f"{str(num)}, "
        elif num == user_input:
            options = options.strip(", ")
            options += f" or {str(user_input)}"

    while True:
        user_ans = input(f"Your answer ({options}): ")
        print(type(user_ans))

        for num in range(1, user_input+1):
            if user_ans == str(num):
                return num
        print(f"Sorry, that is not a valid input, please enter a number between 1 and {user_input}.")


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
        user_character_choice = number_dict_input_validation("character", self.suspect_dict)
        return self.suspect_dict[user_character_choice]


    def check_scorecard(self):
        pass

    def move_player(self, player_location, desired_room, current_room, die_roll, room_distances, room_dict):
        """
        Takes a player's current and desired location and moves
        the player towards the chosen room
        """
        # print(room_distances[desired_room])
        if die_roll >= int(room_distances[desired_room]):
            player_location = list(room_dict[desired_room])
            print(f"Walking to the {desired_room}...")
            time.sleep(2)
            os.system("clear")
            print(f"You are now in the {desired_room}")
            return player_location
        # print(room_distances[desired_room])
        else:
            total_die_roll = copy.deepcopy(die_roll)
            print(f"You have not rolled enough to reach the {desired_room}.")
            print(f"1. Move {die_roll} spaces towards the {desired_room}\n2. Stay at current location"
            )
            stay_or_move = number_input_validation(2)
            
            
            if stay_or_move == "1":
                # Calculating where on the board the player will end up after moving towards the chosen room
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
                        elif room_dict[desired_room][1] - player_location[1] < 0:
                            die_roll -= 1
                            player_location[1] -= 1
                print("Moving...")
                time.sleep(1.5)
                print(f"You have moved {total_die_roll} spaces towards the {desired_room}")
                if current_room not in room_dict.keys():
                    time.sleep(1)
                    print("You are still in the hallway")
                else:
                    time.sleep(1)
                    print("You are now in the hallway")
                return player_location

            elif stay_or_move == "2":
                if player_location in room_dict.values():
                    print(f"You have chosen to stay in the {current_room}.")
                else:
                    print("You have chosen to stay in the hallway.")
                return player_location


    def investigate(self, current_room, player_location=[1,1]):
        """
        Allows the player to investigate other player's cards
        """
        # player_location = gameboard.choose_room(player)
        # current_room = gameboard.which_room(player)
        print(player_location)
        print("======== Investigation phase ========")
        confirm_choice = False
        while not confirm_choice:
            print(f"You are in the {current_room}\n ===== SUSPECTS =====")
            for num, suspect in self.suspect_dict.items():
                print(num, suspect)
            suspect = number_dict_input_validation("suspect", self.suspect_dict)
            print("===== WEAPONS =====")
            for num, weapon in self.weapon_dict.items():
                print(num, weapon)
            weapon = number_dict_input_validation("weapon", self.weapon_dict)
            
            print(f"Are you sure you want to investigate {self.suspect_dict[suspect]} with the {self.weapon_dict[weapon]} in the {current_room}?")
            check_choice = input("y/n: ")
            confirm_choice = y_n_input_validation(check_choice)

    def make_accusation():
        pass

    def roll_die(self):
        """
        Returns a random number between 1 and 6.
        """
        return random.randint(1, 6)





# AI Player class
class AIPlayer:
    def __init__(self, cards):
        self.cards = cards

    def check_cards(self):
        print(self.cards)
    
    def show_card(self):
        pass