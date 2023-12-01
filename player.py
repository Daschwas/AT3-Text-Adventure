class Player:
    """
    This class represents the user/player character.
    """

    def __init__(self, name):
        """
        Parameters:
             Name - The name of the non player character.
             Items - A list that shows the current items held by the player.
        """
        self.name = name
        self.items = []