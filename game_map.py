from room import *


class GameMap:
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
        return self.rooms.get((row, column))

    def display_map(self):
        print(f"Current location: {self.player_coordinates}")
        current_row, current_col = self.player_coordinates
        display_tilemap = [line.copy() for line in self.tilemap]
        display_tilemap[current_row][current_col] = "Y"
        print("Key: X: Where you've been; Y: Where you are; O: Yet to visit.")
        for line in display_tilemap:
            print(line)


    def set_player_coordinates(self, player):
        self.player_coordinates = player.current_coordinates if player else (0, 0)

    def update_tilemap(self, row, column):
        previous_row, previous_col = row, column
        self.tilemap[previous_row][previous_col] = "X"


