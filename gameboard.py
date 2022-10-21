# import built in modules
import random

# Gameboard

class Gameboard:
    def __init__(self, rooms, player_location):
        self.rooms = rooms
        self.player_location = player_location

    def update_player_location(self, new_location):
        """ Updates the player_location variable stored within Gameboard"""
        self.player_location = new_location[0]
    
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
        user_room_choice = int(input("\nWhich room would you like to move towards?: "))
        # print(f"room choices:{room_options}")
        desired_room = room_options.pop(user_room_choice)
        return (desired_room,room_distances)
        # self.move(player, desired_room, die_roll, room_distances)

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
