[Click here](https://github.com/dragon-fire-fly/cluedo/blob/main/README.md) to return to the main PyClue README.

# Testing

## Manual Testing

### Main Menu
|What is being tested?   |  What is the input? |  Expected response? | Works as expected?  | Screenshot  |
|---|---|---|---|---|
| Select option 1  | "1"  | plays game with story  | yes  | ![](documentation/testing/manual_testing/main_menu/main_menu_1.png) ![](documentation/testing/manual_testing/main_menu/main_menu_1_result.png) |
| Select option 2  | "2"  | plays game without story  | yes  | ![](documentation/testing/manual_testing/main_menu/main_menu_2.png)![](documentation/testing/manual_testing/main_menu/main_menu_2_result.png)  |
| Select option 3  | "3"  | displays rules  | yes  | ![](documentation/testing/manual_testing/main_menu/main_menu_3.png)![](documentation/testing/manual_testing/main_menu/main_menu_3_result.png)  |
| Input validation (too many spaces)  | " 1 " (with lots of spaces)  | plays game with story  | yes  | ![](documentation/testing/manual_testing/main_menu/main_menu_1_spaces.png) ![](documentation/testing/manual_testing/main_menu/main_menu_spaces_result.png)  |
| Input validation (number outside range)  | "4"  | input not accepted  | yes  | ![](documentation/testing/manual_testing/main_menu/main_menu_4.png) |
| Input validation (invalid string)  | "cat"  | input not accepted  |  yes | ![](documentation/testing/manual_testing/main_menu/main_menu_cat.png)  |

### Player Selection

|What is being tested?   |  What is the input? |  Expected response | Works as expected?  | Screenshot  |
|---|---|---|---|---|
| Select character 1  | "1"  |  select Miss Scarlett | yes  | ![select character 1](documentation/testing/manual_testing/character_selection/character_select_1.png)  |
| Select Miss Scarlett  | "Miss Scarlett"  | select Miss Scarlett  | yes | ![select Miss Scarlett](documentation/testing/manual_testing/character_selection/miss_scarlett.png)  |
| Select character 2  | "2"  | select Colonel Mustard  | yes  | ![select character 2](documentation/testing/manual_testing/character_selection/player_select_2.png)  |
| Select character 3  | "3"  | select Mrs. White  | yes  | ![select character 3](documentation/testing/manual_testing/character_selection/player_select_3.png)  |
| Input validation (too many spaces)  | "  4  " (with many spaces)  | select player 4 (Reverend Green)  | yes  | ![select character 4](documentation/testing/manual_testing/character_selection/character_select_spaces.png)  |
| Input validation (number outside range)  | "7"  |  input not accepted | yes  | ![input validation invalid number](documentation/testing/manual_testing/character_selection/player_select_7.png)  |
| Input validation (invalid string)  | "cat"  | input not accepted |  yes  | ![input validation invalid string](documentation/testing/manual_testing/character_selection/cat.png)  |
| Input validation (does not exist)  | "Dr Black" | input not accepted  | yes  | ![input validation does not exist](documentation/testing/manual_testing/character_selection/dr_black.png)  |
| Input validation (shortened name)  | "col mustard  |  input not accepted (only accepts specific dictionary keys/values) |  yes  | ![input validation shortened name](documentation/testing/manual_testing/character_selection/col_mustard.png)  |


### Investigation Card

|What is being tested?   |  What is the input? |  Expected response | Works as expected?  | Screenshot  |
|---|---|---|---|---|
| Open investigation card with "i"  | "i"  | opens investigation card  | yes  |  ![open investigation card with "i"](documentation/testing/manual_testing/investigation_card/investigation_card_i.png) |
| Open investigation card with "I"   | "I"  | opens investigation card   | yes  | ![open investigation card with "I"](documentation/testing/manual_testing/investigation_card/investigation_card_I.png)  |
| Input validation - open investigation card with "investigation"  | "investigation"  |  input not accepted  | yes  | ![open investigation card with "investigation"](documentation/testing/manual_testing/investigation_card/invalid_input.png)  |
| Input validation - open investigation card with number  | "0"  |  input not accepted  | yes  | ![open investigation card with "0"](documentation/testing/manual_testing/investigation_card/invalid_number.png)  |
| Update investigation card when card shown  | completes an investigation round  | card shown and "x" placed in correct place in investigation card  |  yes |  ![update investigation card](documentation/testing/manual_testing/investigation_card/investigation_card_updated.png)![successfully updated](documentation/testing/manual_testing/investigation_card/peacock_rope.png) |
| Correct cards added at start of game  | select character  |  The three cards printed at the start should correcpond to the three cards marked on the investigation card | yes  | ![correct cards?](documentation/testing/manual_testing/investigation_card/correct_cards_1.png)![correct cards added](documentation/testing/manual_testing/investigation_card/correct_cards_2.png)  |
|   |   |   | yes  |   |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   |  yes | ![](documentation/testing/manual_testing)  |

### Moving Between Rooms

|What is being tested?   |  What is the input? |  Expected response | Works as expected?  | Screenshot  |
|---|---|---|---|---|
| Move to a new room when die roll is high enough  | "5" (a room 6 spaces away)  | end up in the dining room  | yes  |  ![choice of room](documentation/testing/manual_testing/gameboard_movement/move_to_new_room_1.png)![You are in the dining room](documentation/testing/manual_testing/gameboard_movement/move_to_new_room_2.png) |
| Move towards a new room when die roll is not high enough  | select a room further away than the available moves and chose to move towards that room  | should print "you have moved x spaces towards y room" and finish turn in the hallway  | yes  | ![move towards room 1](documentation/testing/manual_testing/gameboard_movement/not_enough_moves.png)![move towards room 2](documentation/testing/manual_testing/gameboard_movement/not_enough_moves_2.png)![move towards room 3](documentation/testing/manual_testing/gameboard_movement/not_enough_moves_3.png)![move towards room 4](documentation/testing/manual_testing/gameboard_movement/not_enough_moves_4.png)  |
| Stay in room  |   |   | yes  | ![stay in room](documentation/testing/manual_testing/gameboard_movement/stay_in_room.png)![still in same room](documentation/testing/manual_testing/gameboard_movement/still_in_dining_room.png)   |
| Stay in room (after selecting far away room)  | select a room further than moves available, then when asked whether to move or to stay, choose stay  | stay in the current room  | a bug was discovered here and can be found under the bug section (Printing "You chose to stay in the hallway" instead of stay in current room - issue #12). This is now fixed.  | ![stay in room after picking faraway room](documentation/testing/manual_testing/gameboard_movement/stay_after_far_away_room.png)  |
| Use a secret passageway  | select a room that is connected by secret passageway  | move to connected room  | yes  | ![move through secret passageway 1](documentation/testing/manual_testing/gameboard_movement/use_secret_passageway_1.png)![move through secret passageway 2](documentation/testing/manual_testing/gameboard_movement/use_secret_passageway_2.png)   |
| Cross through another room  | select a room that is further away than available moves but that has other rooms on the way  | unfortunately, the way the game board was designed, if the number of available spaces would land you in another room, it does  |  this is a known, unresolved bug and details can be found in the bugs section under "Sometimes end in wrong room bug" - issue #9 |  ![end in wrong room 1](documentation/testing/manual_testing/gameboard_movement/end_in_wrong_room_1.png)![end in wrong room 2](documentation/testing/manual_testing/gameboard_movement/end_in_wrong_room_2.png)![end in wrong room 3](documentation/testing/manual_testing/gameboard_movement/end_in_wrong_room_3.png) |
| You are now in the hallway  |  choose a room too far away to reach this turn, starting from a room | print "You are now in the hallway"  | yes  | ![](documentation/testing/manual_testing/gameboard_movement/move_to_hallway_from_room.png)  |
| You are still in the hallway  | choose a room too far away to reach this turn, starting from the hallway  | print "You are still in the hallway"  | yes  | ![](documentation/testing/manual_testing/gameboard_movement/stay_in_hallway.png)  |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   |  yes | ![](documentation/testing/manual_testing)  |




|What is being tested?   |  What is the input? |  Expected response | Works as expected?  | Screenshot  |
|---|---|---|---|---|
|   |   |   | yes  |  ![](documentation/testing/manual_testing/) |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   |  yes |  ![](documentation/testing/manual_testing) |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   | yes  | ![](documentation/testing/manual_testing)  |
|   |   |   |  yes | ![](documentation/testing/manual_testing)  |