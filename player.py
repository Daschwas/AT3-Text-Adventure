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


player = Player("Person", "Food Court")
