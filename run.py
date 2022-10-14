import random
# Gameboard

# (#, ##) where # is the row and ## is the column
GAME_BOARD = (
    ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)),
    ((2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)),
    ((3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)),
    ((4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)),
    ((5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)),
    ((6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)),
    ((7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)),
)

# Room Locations on board
ROOMS = {
    "Kitchen": (1, 1),
    "Ball Room": (1, 4),
    "Conservatory": (1, 7),
    "Billiard Room": (3, 7),
    "Dining Room": (4, 1),
    "Library": (5, 7),
    "Lounge": (7, 1),
    "Main Hall": (7, 4),
    "Study": (7, 7),
}

# print(GAME_BOARD[0])
# print(ROOMS)


def calculate_distance(point1, point2):
    """Takes two points on the gameboard and calculates and returns the total
    number of spaces between the two points"""
    row_diff = abs(point1[0] - point2[0])
    column_diff = abs(point1[1] - point2[1])
    total_distance = row_diff + column_diff
    return f"{total_distance} space(s)"


def room_distances(rooms, player_location):
    """Calls the calculate_distances() function to calculate the distance
    between the player's current location and each of the rooms on the board.
    Returns an updated dictionary of current distances to each room."""
    distance_dict = {
        "Kitchen": 0,
        "Ball Room": 0,
        "Conservatory": 0,
        "Billiard Room": 0,
        "Dining Room": 0,
        "Library": 0,
        "Lounge": 0,
        "Main Hall": 0,
        "Study": 0,
    }
    for room in rooms:
        distance_dict[room] = calculate_distance(ROOMS[room], player_location)
    return distance_dict


def which_room(current_space):
    """ Takes the current space of a player and returns which room they are in. 
    If player is not in a room, returns hallway. """
    for room, space in ROOMS.items():
        if current_space == space:
            return f"You are currently in the {room}."
    return f"You are currently in the hallway"

def roll_die():
    """ Returns a random number between 1 and 6. """
    return random.randint(1, 6)

player1 = (4, 1)
# needs a validation decorator
def choose_room():
    """ Collects and prints information about which room the player is currently in,
    the outcome of the die roll and the number of spaces to each room to
    the console. Requests input for which room the player wants to move to."""
    
    print(which_room(player1))
    print(f"You have rolled a {roll_die()}.")
    print("=" * 40)
    print(f"The rooms are the following distances: ")
    i = 0
    room_choices = {}
    for k, v in room_distances(ROOMS, player1).items():
        i += 1
        room_choices[i] = k
        if v == "0 space(s)":
            print(f"{i}- {k}: {v} (stay in room)")
        else:
            print(f"{i}- {k}: {v}")
    desired_room = input("Which room would you like to move towards?")
    print(room_choices)





choose_room()