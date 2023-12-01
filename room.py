class Room:
    """
    The intention of this class would be to act as a container for the NPCs and objects that are
    located within the room as well as keep track of where the palyer is located.
    """
    def __init__(self, name, description):
        """
        Parameters:
            Name - The name of the room.
            Items/People - Lists that dictate which characters and objects are located in the room.
            Description -  An description of the room to guide the user in interacting/moving around the room.
            Exits - Dictates the exits available in each room and what room they lead to.
        """
        self.name = name
        self.items = []
        self.people = []
        self.description = description
        self.exits = {}


class FoodCourt(Room):
    def __init__(self):
        super().__init__("Food Court", "A food court filled with vendors and stores. There is a vending machine "
                                       "dispensing drinks in the corner and a man sitting at a bench. He seems to work"
                                       "here and has discarded his staff uniform.")
        self.exits = {'north': Lobby(), 'east': Bank()}


class Lobby(Room):
    def __init__(self):
        super().__init__("Lobby", "A spacious lobby with various shops and entrances. People are bustling around.")
        self.exits = {'south': FoodCourt(), 'east': ElectronicsStore()}


class Bank(Room):
    def __init__(self):
        super().__init__("Bank", "A bank with counters and a waiting area. A security guard is standing at the "
                                 "entrance.")
        self.exits = {'north': ElectronicsStore(), 'west': FoodCourt(), 'south': ClothingBoutique()}


class ElectronicsStore(Room):
    def __init__(self):
        super().__init__("Electronics Store", "A store filled with the latest gadgets and electronics.")
        self.exits = {'west': Lobby(), 'south': Bank()}


class ClothingBoutique(Room):
    def __init__(self):
        super().__init__("Clothing Boutique", "A fashionable boutique with racks of clothes and a fitting room.")
        self.exits = {'north': Bank()}

"""
Instances of all the rooms in the game.
Also establishes a  dictionary for each representing the layout of rooms in the shopping center.

Each room is a key in the dictionary, and its value is another dictionary describing the bordering rooms in each 
cardinal direction.
"""

"""
print("Food Court:")
print(f"Title: {food_court.title}")
print(f"Description: {food_court.description}")
print(f"Exits: {food_court.exits}")
print()
"""