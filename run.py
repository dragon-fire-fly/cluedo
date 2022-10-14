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


player = (4, 1)

print(room_distances(ROOMS, player))
