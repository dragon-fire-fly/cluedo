import random
import time
from tabulate import tabulate
import os
import copy

from setup import player
from setup import gameboard, ROOM_LOCATIONS

# print(tabulate(game_board))

# player_location = [4, 1]

# Game variables
win_condition_satisfied = False
hours_remaining = 24


def clear():
    os.system("clear")



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

print(f"You are currently in the {current_room}.\n")
print("Rolling die....")
time.sleep(2)
clear()
print(f"You are currently in the {current_room}.\nYou have rolled a {turn_die_roll}.\n")


# ask user for desired room
desired_room, room_distances = gameboard.choose_room()

# move towards the desired room
new_player_location = player.move_player(player_location, desired_room, current_room, turn_die_roll, room_distances, ROOM_LOCATIONS)
gameboard.update_player_location([new_player_location])


#3
# check whether in a room or in hallway (and if so, end turn)
current_room = gameboard.which_room()
# print(gameboard.current_player_location())
# print(current_room)
if current_room in ROOM_LOCATIONS:
    player.investigate(current_room)
else:
    print("End of turn")
    
#4


#5
# compare cards to other player decks
# for each AI player, check_cards()

# print()



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