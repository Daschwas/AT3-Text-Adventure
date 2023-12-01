class Room:
    """
    The intention of this class would be to act as a container for the NPCs and objects that are
    located within the room as well as keep track of where the palyer is located.
    """
    def __init__(self, title, description):
        """
        Parameters:
            Title - The name of the room.
            Items/People - Lists that dictate which characters and objects are located in the room.
            Description -  An description of the room to guide the user in interacting/moving around the room.
            Exits - Dictates the exits available in each room and what room they lead to.
        """
        self.title = title
        self.items = []
        self.people = []
        self.description = description
        self.exits = {}


"""
Instances of all the rooms in the game.
"""
food_court = Room("Food Court", "A food court filled with vendors and stores. There is a vending machine dispensing "
                                "drinks in the corner and a man sitting at a bench. He seems to work here and has "
                                "discarded his staff uniform.")
food_court.exits = {'North': 'Lobby', 'East': 'Bank'}

lobby = Room("Lobby", "A spacious lobby with various shops and entrances. People are bustling around.")
lobby.exits = {'South': 'Food Court', 'East': 'Electronics Store'}

bank = Room("Bank", "A bank with counters and a waiting area. A security guard is standing at the entrance.")
bank_exits = {'North': 'Electronics Store', 'West': 'Food Court', 'South': 'Clothing Boutique'}

electronics_store = Room("Electronics Store", "A store filled with the latest gadgets and electronics.")
electronics_store_exits = {'West': 'Lobby', 'South': 'Bank'}

clothing_boutique = Room("Clothing Boutique", "A fashionable boutique with racks of clothes and a fitting room.")
clothing_boutique_exits = {'North': 'Bank'}

"""
print("Food Court:")
print(f"Title: {food_court.title}")
print(f"Description: {food_court.description}")
print(f"Exits: {food_court.exits}")
print()
"""