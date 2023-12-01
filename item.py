class Item:

    """
    This class represents the items that can be held by the player and characters.
    """
    def __init__(self, owner, title):
        """
        Parameters:
            Owner - The person or player that currently owns the item.
            Title - The name of the object.
        """
        self.owner = owner
        self.title = title