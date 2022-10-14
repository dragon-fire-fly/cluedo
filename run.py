import random

# Gameboard

# (#, ##) where # is the row and ## is the column
# GAME_BOARD = (
#     ((1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)),
#     ((2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7)),
#     ((3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)),
#     ((4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)),
#     ((5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7)),
#     ((6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7)),
#     ((7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)),
# )

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


class Gameboard:
    def __init__(self, rooms, player):
        self.rooms = rooms
        self.player = player

    def calculate_distance(self, point1, point2):
        """Takes two points on the gameboard and calculates and returns the total
        number of spaces between the two points"""
        row_diff = abs(point1[0] - point2[0])
        column_diff = abs(point1[1] - point2[1])
        total_distance = row_diff + column_diff
        return f"{total_distance}"

    def room_distances(self, rooms, player_location):
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
            distance_dict[room] = self.calculate_distance(
                ROOMS[room], player_location
            )
        return distance_dict

    def which_room(self, current_space):
        """Takes the current space of a player and returns which room they are in.
        If player is not in a room, returns hallway."""
        for room, space in ROOMS.items():
            if current_space == space:
                return f"You are currently in the {room}."
        return f"You are currently in the hallway"

    def roll_die(self):
        """Returns a random number between 1 and 6."""
        return random.randint(1, 6)

    # needs a validation decorator
    def choose_room(self, player):
        """Collects and prints information about which room the player is currently in,
        the outcome of the die roll and the number of spaces to each room to
        the console. Requests input for which room the player wants to move to."""

        print(self.which_room(player))
        turn_die_roll = self.roll_die()
        print(f"You have rolled a {turn_die_roll}.")
        print("=" * 40)
        print(f"The rooms are the following distances: ")
        i = 0
        room_options = {}
        for k, v in self.room_distances(ROOMS, player).items():
            i += 1
            room_options[i] = k
            if v == "0":
                print(f"{i}- {k}: {v} space(s) (stay in room)")
            else:
                print(f"{i}- {k}: {v} space(s)")
        user_room_choice = int(input("Which room would you like to move towards?: "))
        print(f"room choices:{room_options}")
        desired_room = room_options.pop(user_room_choice)
        print(f"You have chosen the {desired_room}")
        self.move(player, desired_room, turn_die_roll)

    def move(self, player, desired_room, die_roll):
        """
        Takes a player's current and desired location and moves
        the player towards the chosen room
        """
        print(self.room_distances(ROOMS, player)[desired_room])
        if die_roll >= int(self.room_distances(ROOMS, player)[desired_room]):
            player = ROOMS[desired_room]
            print(player)
            print(f"You are now in the {desired_room}")
        # print(room_distances(ROOMS, player)[desired_room])
        else:
            self.which_room(player)
            print(f"You have not rolled enough to reach the {desired_room}.")
            input(
                f"1. Move {die_roll} spaces towards the {desired_room}\n2. Stay in current room\nYour answer (1 or 2): "
            )




player1 = (4, 1)

gameboard = Gameboard(ROOMS, player1)

print(gameboard.choose_room(player1))
