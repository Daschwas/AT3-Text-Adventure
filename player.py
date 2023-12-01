class Player:
    """
    This class represents the user/player character.
    """

    def __init__(self, name, room):
        """
        Parameters:
             Name - The name of the non player character.
             Items - A list that shows the current items held by the player.
             Room - Keeps track of what room the player is currently in.
        """
        self.name = name
        self.items = []
        self.room = room

    def move_rooms(self, direction):
        """
        Move the player to a new room based on the specified direction.

        Parameters:
            Direction -  The direction in which the player wants to move.
        """
        if direction in self.room.exits:
            new_room = self.room.exits[direction]
            print(f"You moved {direction}.")
            self.room = new_room
            print(f"You have arrived in the {self.room.name}.")
        else:
            print("Invalid direction. Try again.")