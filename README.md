# Cluedo Planning

## Rules:
1. The murderer, murder weapon and murder location have been placed inside the "murder envelope"
2. Miss Scarlet always goes first, then play moves clockwise.
3. Roll the dice or use a secret passage each turn to move from room to room. You may move up, down or sideways, but not diagonally. 
4. On your turn, if you are in a room, you may question the other suspects about any suspect, any weapon and the location you are currently at. 
5. Starting with the player to your left, if that player has one of the three suggested cards, they must show you one. If they don't have any cards, they player to their left is questioned next, and so on.
6. Once you feel certain that you know the murderer, murder weapon and room, you may make an accusation. You may only make one accusation per game.

# Setup

setup.py contains all information pertinent to the setup of the game. This includes:

1. instatiating 
    - the gameboard class
    - the cards class
    - player class
    - AI player class
2. containing all lists and dictionaries for game setup

# General Gameplay
Each turn consists of the following 11 steps:
## Player turn:
1. minus one hour from the game clock
2. player rolls dice and decides whether to move or stay in the room
    - player.move() (inc. player.roll_die()) - generates new player co-ordinates
    - gameboard.update() - update to new player location
3. if player moves to hallway, turn ends
    - gameboard.which_room() - returns which room player is in (or hallway)
4. if player in room, player chooses a suspect and weapon to investigate
    - player.investigate() - chooses three cards to compare (1 x suspect, 1 x weapon, 1 x room)
5. The three chosen cards (suspect, weapon, room) are compared to the next player (index 0 in player list)
    - for each AI player, check_cards()
6. if the next player has one or more investigation cards, they must show one
    - AI player show_card()
7. if the next player has none of the investigation cards, the next player's (index 1 in player list) cards are compared to investigation cards
    - AI player check_cards()
8. Play continues in this manner until a card is shown. Once a card is shown, turn ends
    - AI player show_card()
9. If no cards are shown by any player, turn still ends
10. Investigation card is updated with the card shown (if any)
    investigation_card.update()
11. Next turn begins...



## Potential OOP objects:
- Game board
- Player(s)/ player piece(s)
- Cards
- Dice
- Scorecard/ tracker

# Functions
## Gameboard
![Cluedo board](game_board_layout.png)



























![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome dragon-fire-fly,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!