import random
import time
from tabulate import tabulate
import os
import copy

from setup import player
from setup import gameboard, ROOM_LOCATIONS

print("Start")

# print(tabulate(game_board))

player_location = [4, 1]

# Game variables
win_condition_satisfied = False
hours_remaining = 24




''' Player turn:
1. minus one hour from the game clock
2. player rolls dice and decides whether to move or stay in the room
3. if player moves to hallway, turn ends
4. if player in room, player chooses a suspect and weapon to investigate
5. The three chosen cards (suspect, weapon, room) are compared to the next player (index 0 in player list)
6. if the next player has one or more investigation cards, they must show one
7. if the next player has none of the investigation cards, the next player's (index 1 in player list) cards are compared to investigation cards
8. Play continues in this manner until a card is shown. Once a card is shown, turn ends
9. If no cards are shown, turn still ends
10. Investigation card is updated with the card shown (if any)
11. Next turn begins...
'''

#1
# minus one hour

#2
# obtain current player location
player_location = gameboard.current_player_location()
old_player_location = copy.deepcopy(player_location)

# obtain current room
current_room = gameboard.which_room()
# die roll for the turn:
turn_die_roll = player.roll_die()


print(f"You are currently in the {current_room}.\nYou have rolled a {turn_die_roll}.")

# ask user for desired room
desired_room = gameboard.choose_room()
# distances to each room
room_distances = gameboard.room_distances()

# move towards the desired room
new_player_location = player.move_player(player_location, desired_room, current_room, turn_die_roll, room_distances, ROOM_LOCATIONS)
gameboard.update_player_location([new_player_location])

# if new_player_location != old_player_location:
#     print(f"Walking towards the {desired_room}...")
#     time.sleep(2)
#     os.system("clear")
#     if new_player_location in ROOM_LOCATIONS.values():
#         print(f"You are now in the {desired_room}.")
#     else:
#         print(f"You are now in the hallway.")
# else:
#     print(f"You have chosen to stay in the {current_room}")


# print(f"New player location is: {gameboard.current_player_location()}")
# print(type(gameboard.current_player_location()[0]))





# desired room is either same room or different room
# desired room is input into move_player() function
# if enough spaces, move and update current location. 

#3
# check whether in hallway and if so, end turn

#4
# player.investigate(gameboard.which_room(player_location))

#5
# compare cards to other player decks
# for each AI player, check_cards()

#6
# if card found, show_card() function 

#7
# move to next AI player, if relevant

#8
# if card found, show_card() function 

#9


#10
# update investigation card 
#11


# player.move_player(player_location)


# check_cards() for each  