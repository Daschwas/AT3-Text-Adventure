from game_map import GameMap

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
        self.current_coordinates = (2, 1)

    def move_rooms(self, direction):
        """
        Move the player to a new room based on the specified direction.

        Parameters:
            Direction -  The direction in which the player wants to move.
        """

        current_row, current_col = self.current_coordinates
        new_row, new_col = current_row, current_col

        if direction == 'north':
            new_row -= 1
        elif direction == 'south':
            new_row += 1
        elif direction == 'east':
            new_col += 1
        elif direction == 'west':
            new_col -= 1

        new_coordinates = (new_row, new_col)
        new_room = self.game_map.get_room_at(*new_coordinates)

        if new_room:
            self.current_coordinates = new_coordinates
            self.room = new_room
            print(f"You moved {direction}.")
            print(f"You have arrived in the {new_room.name}.")
        else:
            print("Invalid direction. Try again.")
