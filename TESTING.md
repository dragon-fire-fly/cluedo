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




|What is being tested?   |  What is the input? |  Expected response | Actual response  | Screenshot  |
|---|---|---|---|---|
|   |   |   |   |  ![](documentation/testing/manual_testing/) |
|   |   |   |   | ![](documentation/testing/manual_testing)  |
|   |   |   |   | ![](documentation/testing/manual_testing)  |
|   |   |   |   | ![](documentation/testing/manual_testing)  |
|   |   |   |   |  ![](documentation/testing/manual_testing) |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |




|What is being tested?   |  What is the input? |  Expected response | Actual response  | Screenshot  |
|---|---|---|---|---|
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |




|What is being tested?   |  What is the input? |  Expected response | Actual response  | Screenshot  |
|---|---|---|---|---|
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |