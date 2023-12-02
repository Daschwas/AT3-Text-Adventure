from room import *


class GameMap:
    def __init__(self):
        self.rooms = {}
        self.tilemap = [
            ["0", "0",],
            ["0", "O",],
            ["-", "O"],
        ]
        self.create_rooms()

    def create_rooms(self):
        food_court = FoodCourt()
        lobby = Lobby()
        bank = Bank()
        clothing_boutique = ClothingBoutique()
        electronics_store = ElectronicsStore()

        self.rooms[(2, 1)] = food_court
        self.rooms[(1, 1)] = lobby
        self.rooms[(2, 2)] = bank
        self.rooms[(1, 2)] = electronics_store
        self.rooms[(3, 2)] = clothing_boutique

    def get_room_at(self, row, column):
        return self.rooms.get((row, column))

    def display_map(self):
        for i, line in enumerate(self.tilemap):
            if i == self.player_coordinates[0]:
                line[self.player_coordinates[1]] = "Y"
            print(line)

    def set_player_coordinates(self, player):
        self.player_coordinates = player.current_coordinates

    def update_tilemap(self, row, column):
        previous_row, previous_col = row, column
        self.tilemap[previous_row][previous_col] = "X"


