import commands
from game_map import GameMap
from room import *
from commands import *

class Player:
    """
    This class represents the user/player character.
    """
    game_map = GameMap()

    def __init__(self, name, room):
        """
        Parameters:
             Name - The name of the non player character.
             Items - A list that shows the current items held by the player.
             Room - Keeps track of what room the player is currently in.
             game_over - Flag state that indicates whether the player has lost the game or not.
        """
        self.name = name
        self.room = room
        self.game_over = False
        self.current_coordinates = (1, 0)
        self.direction_map = {
            'north': (-1, 0),
            'south': (1, 0),
            'east': (0, 1),
            'west': (0, -1),
        }
        self.is_member = False
        self.given_scarf = False

    def move_rooms(self, direction, backpack):
        """
        Move the player to a new room based on the specified direction.
        Also updates the players internal coordinates and calls a gamemap function to update the tilemap.

        Parameters:
            Direction -  The direction in which the player wants to move.
        """
        blocked = False
        current_row, current_col = self.current_coordinates
        direction_change = self.direction_map.get(direction)

        if direction_change:
            if isinstance(self.room, Lobby) and direction("north"):
                commands.end_game(self.player, backpack)
            else:
                new_row, new_col = current_row + direction_change[0], current_col + direction_change[1]
                new_coordinates = (new_row, new_col)
                new_room = self.game_map.get_room_at(*new_coordinates)

                if new_room:
                    if isinstance(self.room, Bank) and isinstance(new_room, ElectronicsStore):
                        blocked = True
                    elif isinstance(self.room, FoodCourt) and isinstance(new_room, Lobby):
                        blocked = True
                    elif isinstance(self.room, ElectronicsStore) and isinstance(new_room, Lobby):
                        blocked = True
                    if not blocked:
                        self.current_coordinates = new_coordinates
                        self.room = new_room
                        self.game_map.set_player_coordinates(self)
                        self.game_map.update_tilemap(current_row, current_col)
                        print(f"You moved {direction}.")
                        print(f"You have arrived in the {new_room.name}.")
                        print(f"These are your previous values {current_row, current_col}")
                        print(f"These are your current values{self.current_coordinates}")
                    else:
                        print("It looks like you can't proceed through here at the moment.")
                else:
                    print("Invalid direction. Try again.")
        else:
            print("Invalid direction. Try again.")
