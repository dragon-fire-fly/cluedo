# Cluedo Planning

## Rules:
1. The murderer, murder weapon and murder location have been placed inside the "murder envelope"
2. Miss Scarlet always goes first, then play moves diagonally.
3. Roll the dice or use a secret passage each turn to move from room to room. You may move up, down or sideways, but not diagonally. 
4. On your turn, if you are in a room, you may question the other suspects about any suspect, any weapon and the location you are currently at. 
5. Starting with the player to your left, if that player has one of the three suggested cards, they must show you one. If they don't have any cards, they player to their left is questioned next, and so on.
6. Once you feel certain that you know the murderer, murder weapon and room, you may make an accusation. You may only make one accusation per game.


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