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