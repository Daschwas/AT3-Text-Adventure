from room import *


class GameMap:
    """
    Class to represent the in game map and handle different map based functions.

    Attributes:
        rooms (dict) - A dictionary to store room coordinates as keys and corresponding room objects.
        tilemap (list) - A 2d list representing the visual map including markers for the player and visited locations.
        player_coordinates (tuple) - A tuple representing the current coordinates of the player object.
    """
    def __init__(self):

        self.rooms = {}
        self.tilemap = [
            ["0", "0"],
            ["0", "O"],
            ["-", "O"]
        ]
        self.create_rooms()
        self.player_coordinates = (1, 0)

    def create_rooms(self):
        """
        Initializes all the room objects and populates the room dictionary with said objects.
        """
        food_court = FoodCourt()
        lobby = Lobby()
        bank = Bank()
        clothing_boutique = ClothingBoutique()
        electronics_store = ElectronicsStore()

        self.rooms[(1, 0)] = food_court
        self.rooms[(0, 0)] = lobby
        self.rooms[(1, 1)] = bank
        self.rooms[(0, 1)] = electronics_store
        self.rooms[(2, 1)] = clothing_boutique

    def get_room_at(self, row, column):
        """
        Retrieves the relevant Room object at the specified coordinates.
        :param row: Corresponds to the row of the room in the tile based map.
        :param column: Corresponds to the column of the room in the tile based map.
        :return: room: The room object at the given coordinates.
        """
        return self.rooms.get((row, column))

    def display_map(self):
        """
        Brings up a visual representation of the map, including where the player is and where they have been.
        """
        print(f"Current location: {self.player_coordinates}")
        current_row, current_col = self.player_coordinates
        display_tilemap = [line.copy() for line in self.tilemap]
        display_tilemap[current_row][current_col] = "Y"
        print("Key: X: Where you've been; Y: Where you are; O: Yet to visit.")
        for line in display_tilemap:
            print(line)

    def set_player_coordinates(self, player):
        """
        Update's the player's personal coordinates (ie; what room they are currently in).
        :param player: The player.
        """
        self.player_coordinates = player.current_coordinates if player else (0, 0)

    def update_tilemap(self, row, column):
        """
        Updates the visual map to keep track of where the player has visited.
        :param row: Corresponds to the row of the room in the tile based map.
        :param column: Corresponds to the columns of the room in the tile based map.
        """
        previous_row, previous_col = row, column
        self.tilemap[previous_row][previous_col] = "X"
