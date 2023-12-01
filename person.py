class Person:
    """
    This class represents the NPCs that inhabit the world.
    """

    def __init__(self, name):
        """
        Parameters:
             Name - The name of the non player character.
             Items - A list that shows the current items held by the NPC.
             On_Shift - This is a state that shows whether the postman is currently working or not. It is switched off
             when the player runs out of 'turns' as the world then switches off.
        """
        self.name = name
        self.items = []
        self.on_shift = False
