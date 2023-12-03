import commands
from game_map import GameMap
from room import *


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
             game_over - A bool flag state that indicates whether the player has lost the game or not.
             current coordinates: A tuple that stores where the player currently is in the map via row and column value.
             direction_map - A dictionary containing cardinal directions mapped to coordinate changes used when moving.
             is_member - A bool flag that denotes whether the player has got membership to the club.
             given_scarf - A bool flag that tracks whether the player has completed the scarf sidequest.

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

    def move_rooms(self, direction, backpack, turn_counter):
        """
        Move the player to a new room based on the specified direction.
        Also updates the players internal coordinates and calls a gamemap function to update the tilemap.

        Parameters:
            Direction -  The direction in which the player wants to move.
            Backpack - The player's backpack.
            Turn_counter - The current turn counter in game representing the time.
        """
        blocked = False
        current_row, current_col = self.current_coordinates
        direction_change = self.direction_map.get(direction)

        if direction_change:
            if isinstance(self.room, Lobby) and direction == "north":
                commands.end_game(self, backpack)
            else:
                new_row, new_col = current_row + direction_change[0], current_col + direction_change[1]
                new_coordinates = (new_row, new_col)
                new_room = self.game_map.get_room_at(*new_coordinates)

                # Prevents coordinates and map being updated unless the player has moved to a valid room.
                if new_room:
                    # There are three block events in the game - this checks whether the player is allowed to move
                    # and if not updates the blocked flag to prevent movement.
                    if isinstance(self.room, Bank) and isinstance(new_room, ElectronicsStore):
                        blocked = True
                        self.room.block_event(self, backpack)
                        if self.is_member:
                            blocked = False
                    elif isinstance(self.room, FoodCourt) and isinstance(new_room, Lobby):
                        blocked = self.room.block_event(turn_counter)
                    elif isinstance(self.room, ElectronicsStore) and isinstance(new_room, Lobby):
                        blocked = True
                        self.room.block_event(self, backpack)
                        if self.given_scarf:
                            blocked = False
                    if not blocked:
                        self.current_coordinates = new_coordinates
                        self.room = new_room
                        self.game_map.set_player_coordinates(self)
                        self.game_map.update_tilemap(current_row, current_col)
                        print(f"You moved {direction}.")
                        print(f"You have arrived in the {new_room.name}.")
                        print(f"{new_room.description}")
                    else:
                        print("It looks like you can't proceed through here at the moment.\n")
                else:
                    print("Invalid direction. Try again.\n")
        else:
            print("Invalid direction. Try again.\n")
