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


player1 = (4, 1)

print(calculate_distance(player1, ROOMS["Kitchen"]))
print(calculate_distance(player1, ROOMS["Library"]))
