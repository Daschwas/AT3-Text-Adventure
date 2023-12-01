class Room:
    """
    The intention of this class would be to act as a container for the NPCs and objects that are
    located within the room.
    """
    def __init__(self, title):
        """
        Parameters:
            Title - The name of the room.
            Objects/People - Lists that dictate which characters and objects are located in the room.
        """
        self.title = title
        self.objects = []
        self.people = []
