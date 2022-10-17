import time

def number_input_validation(user_input, chosen_dict= None):
    """
    Takes an input and a relevant dictionary and prompts the user to choose an option.
    If the user input is valid, returns 
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
    
    def choose_player(self):
        print("====== PLAYERS ======")
        for num, player in self.suspect_dict.items():
            print(num, player)
        user_character_choice = number_input_validation("character", self.suspect_dict)
        print(f"You have chosen {self.suspect_dict[user_character_choice]}.")


    def check_scorecard(self):
        pass

    def move_player(self):
        pass


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
            suspect = number_input_validation("suspect", self.suspect_dict)
            print("===== WEAPONS =====")
            for num, weapon in self.weapon_dict.items():
                print(num, weapon)
            weapon = number_input_validation("weapon", self.weapon_dict)
            
            print(f"Are you sure you want to investigate {self.suspect_dict[suspect]} with the {self.weapon_dict[weapon]} in the {current_room}?")
            check_choice = input("y/n: ")
            confirm_choice = y_n_input_validation(check_choice)

    def make_accusation():
        pass

    def roll_die():
        pass





# AI Player class
class AIPlayer:
    def __init__(self):
        pass

    def check_cards():
        pass