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
# ROOMS = {
#     "Kitchen": (1, 1),
#     "Ball Room": (1, 4),
#     "Conservatory": (1, 7),
#     "Billiard Room": (3, 7),
#     "Dining Room": (4, 1),
#     "Library": (5, 7),
#     "Lounge": (7, 1),
#     "Main Hall": (7, 4),
#     "Study": (7, 7),
# }


class Gameboard:
    def __init__(self, rooms, player_location):
        self.rooms = rooms
        self.player_location = player_location

    def update_player_location(self, new_location):
        """ Updates the player_location variable stored within Gameboard"""
        self.player_location = new_location
    
    def current_player_location(self):
        """ Returns the current player_location coordinates"""
        return self.player_location

    def calculate_distance(self, point1: tuple, point2: tuple):
        """Takes two points on the gameboard and calculates and returns the total
        number of spaces between the two points"""
        row_diff = abs(point1[0] - point2[0])
        column_diff = abs(point1[1] - point2[1])
        total_distance = row_diff + column_diff
        return f"{total_distance}"

    # player or run.py
    def room_distances(self):
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
        for room in self.rooms:
            distance_dict[room] = self.calculate_distance(
                self.rooms[room], self.player_location
            )
        return distance_dict

    def which_room(self):
        """Takes the current space of a player and returns which room they are in.
        If player is not in a room, returns hallway."""
        for room, space in self.rooms.items():
            if self.player_location[0] == space[0] and self.player_location[1] == space[1]:
                return room
        return "hallway"

    def which_coordinates(self, room):
        """Takes the current room of a player and returns the co-ordinates for that room.
        If player is not in a room, returns None."""
        return self.rooms[room]
            

    # needs a validation decorator
    def choose_room(self):
        """Collects and prints information about which room the player is currently in,
        the outcome of the die roll and the number of spaces to each room to
        the console. Requests input for which room the player wants to move to."""

        current_room = self.which_room()
        # print(f"You are currently in the {current_room}.")
        print("=" * 40)
        print(f"The rooms are the following distances: ")
        i = 0
        room_distances = self.room_distances()
        room_options = {}
        for k, v in self.room_distances().items():
            if v == "0":
                passageway_room = self.check_for_secret_passageway(current_room)
                # print(f"passageway_room: {passageway_room}")
                if passageway_room:
                    room_distances[passageway_room] = "0"

        for k, v in room_distances.items():
            i += 1
            room_options[i] = k
            if v == "0" and k == current_room:
                print(f"{i}- {k}: {v} space(s) (stay in room)")

            elif v == "0":
                print(f"{i}- {k}: {v} space(s) (Use secret passageway)")
            elif current_room not in room_options.keys() and len(v) <= 2:
                print(f"{i}- {k}: {v} space(s)")
            else:
                print(f"{i}- {k}: {v}")
        user_room_choice = int(input("Which room would you like to move towards?: "))
        print(f"room choices:{room_options}")
        desired_room = room_options.pop(user_room_choice)
        return desired_room
        # self.move(player, desired_room, die_roll, room_distances)

    # def move(self, player, desired_room, die_roll, room_distances):
    #     """
    #     Takes a player's current and desired location and moves
    #     the player towards the chosen room
    #     """
    #     print(room_distances[desired_room])
    #     if die_roll >= int(room_distances[desired_room]):
    #         player = self.rooms[desired_room]
    #         # print(player)
    #         print(f"You are now in the {desired_room}")
    #         return player
    #     # print(room_distances[desired_room])
    #     else:
    #         self.which_room()
    #         print(f"You have not rolled enough to reach the {desired_room}.")
    #         stay_or_move = input(
    #             f"1. Move {die_roll} spaces towards the {desired_room}\n2. Stay in current room\nYour answer (1 or 2): "
    #         )
    #         if stay_or_move == "1":
    #             # Calculating where on the board the player will end up after moving towards the chosen room
    #             while die_roll:
    #                 if self.rooms[desired_room][0] - player[0] > 0:
    #                     print("down")
    #                     die_roll -= 1
    #                     player[0] += 1
    #                 elif self.rooms[desired_room][0] - player[0] < 0:
    #                     print("up")
    #                     die_roll -= 1
    #                     player[0] -= 1
    #                 elif self.rooms[desired_room][0] - player[0] == 0:
    #                     print("No up and down movement")
    #                 # left or right?
    #                 if die_roll:
    #                     if self.rooms[desired_room][1] - player[1] > 0:
    #                         print("right")
    #                         die_roll -= 1
    #                         player[1] += 1
    #                     elif self.rooms[desired_room][1] - player[1] < 0:
    #                         print("left")
    #                         die_roll -= 1
    #                         player[1] -= 1
    #                     else:
    #                         print("No sideways movement")
    #                     return player

    #         elif stay_or_move == "2":
    #             print(f"You have chosen to stay in the {self.which_room()}")
    #             # investigate(self.which_room(player))

    def check_for_secret_passageway(self, current_room):
        """
        Takes a player's current location and determines if there is a secret
        passageway connecting that location to another.
        """
        if current_room == "Kitchen":
            return "Study"
        elif current_room == "Study":
            return "Kitchen"
        elif current_room == "Lounge":
            return "Conservatory"
        elif current_room == "Conservatory":
            return "Lounge"
