class Room:
    """
    The intention of this class would be to act as a container for the NPCs and objects that are
    located within the room as well as keep track of where the palyer is located.
    """

    def __init__(self, name, description, row, column):
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
        self.row = row
        self.column = column
        self.position = [self.row, self.column]

        # self.exits = {}

        def get_coordinates(self):
            return self.row, self.column


class FoodCourt(Room):
    def __init__(self):
        super().__init__("Food Court", "A food court filled with vendors and stores. The air is alive with "
                                       "the sweet melodies of various food aromas. ", 2, 1)

    def look(self):
        print(f"You looked around the {self.name}")
        print("Colorful banners hang overhead, advertising the delights that each vendor has to offer. Hungry "
              "patrons bustle around, deciding between savory bites and sweet treats. A vending machine ")
        print("Various vendors and stores line the perimeter, each offering a tempting array of culinary delights."
              "People are seated at tables, enjoying their meals and engaged in conversation.")
        print("A VENDING MACHINE sits in the corner of the room, with people frequently obtaining drinks from there.")
        print("A tired EMPLOYEE sits at one table with his hat and ID card discard sitting by him.")
        print("To the east, you can see the entrance to the Lobby, and to the south, a pathway leads to the Bank.")
        print("There appears to be a CROWD around the entrance to the lobby.")


class Lobby(Room):
    def __init__(self):
        super().__init__("Lobby", "A spacious lobby with various shops and entrances. People are bustling around.", 1,
                         1)

    def look(self):
        print(f"You looked around the {self.name}")
        print("The Lobby is a spacious area bustling with activity. Various shops surround the central space, "
              "and people move about with purpose.")
        print("The air is filled with a mix of scents from nearby stores. The atmosphere is vibrant, and the sound of "
              "shoppers and conversations creates a lively symphony. To the south, you can see the Food Court, and to "
              "the east, the Electronics Store beckons.")


class Bank(Room):
    def __init__(self):
        super().__init__("Bank", "A bank with counters and a waiting area. An eery quiet hangs over the room in"
                                 "comparison to the business of where you have been so far.", 2, 2)

    def look(self):
        print(f"You looked around the {self.name}")
        print("As you step inside, the scent of freshly printed money tickles your nose. The atmosphere is hushed, "
              "and the gentle hum of counting machines provides a soothing background noise. The sleek marble counters"
              " gleam under the soft glow of chandeliers.")
        print("A BANK TELLER is assisting people at the counter - she is efficiently processing transactions with a"
              "friendly smile")
        print("There are exits to the north, west and south - however a stern looking MAN blocks the north exit.")


class ElectronicsStore(Room):
    def __init__(self):
        super().__init__("Electronics Store", "A store filled with the latest gadgets and electronics.", 1, 2)

    def look(self):
        print(f"You looked around the {self.name}")
        print("You're surrounded by a dazzling display of cutting-edge gadgets and electronic marvels. Bright screens "
              "illuminate the space, showcasing the latest in technology.")
        print("Customers explore the aisles, mesmerized by the sleek devices on the shelves. The air is charged with "
              "the excitement of innovation. To the west, you can see the entrance to the Lobby, and to the south, "
              "a path leads to the Bank.")
        print('A WOMAN stands impatiently by the entrance to the Lobby, frequently checking her phone')


class ClothingBoutique(Room):
    def __init__(self):
        super().__init__("Clothing Boutique", "A fashionable boutique with racks of clothes and a fitting room.", 3, 2)

    def look(self):
        print(f"You looked around the {self.name}")
        print("Racks of stylish clothes adorn the walls, each garment vying for attention with its unique design and"
              " flair.")
        print("Soft lighting creates an inviting ambiance, and a fitting room in the corner beckons those eager to try "
              "on the latest trends. To the north, you can see the entrance to the Bank.")
        print("A friendly VENDOR stands by ready to assist you with your fashion choices")


