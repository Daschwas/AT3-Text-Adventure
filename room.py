from person import*


class Room:
    """
    The intention of this class would be to act as a container for the NPCs and objects that are
    located within the room as well as keep track of where the player is located.

    Attributes:
        name (str) - The name of the room.
        items (list) - The list of items located in the room (not currently used).
        people (list) - The list of people in the room (not currently used).
        description (str) - A description of the room to guide the player.
        row (int) - The row coordinate of the room in the game map.
        column (int) - The column coordinate of the room in the game map.
        position (list) - A list representing the overall coordinate of the room.
    """

    def __init__(self, name, description, row, column):
        """
        Initialises the room object.
        :param name: Name of room.
        :param description: Description of room.
        :param row: Row coordinate of room.
        :param column: Column coordinate of room.
        """
        self.name = name
        self.items = []
        self.people = []
        self.description = description
        self.row = row
        self.column = column
        self.position = [self.row, self.column]


class FoodCourt(Room):
    """
    Class that represents the Food Court object.

    """
    def __init__(self):
        super().__init__("Food Court", "A food court filled with vendors and stores. The air is alive with "
                                       "the sweet melodies of various food aromas. ", 2, 1)

    def room_check(self, backpack):
        """
        Method that if the user is in the correct room, allows them to access the Vending Machine event.
        Similar methods could be implemented for other pages in future versions of the game.
        :param backpack: The player's backpack.
        """
        vending_machine = VendingMachine("Vending Machine")
        vending_machine.check(backpack)

    def block_event(self, turn_counter):
        """
        Handles the block event (crowd blocking way to lobby) when player tries to move.
        :param turn_counter: The current turn counter in the game which determines whether the event is still
        active or not.
        """
        # If turn counter is under 55 - can't move.
        if turn_counter < 55:
            print("You try to move, but a large crowd is blocking your way.")
            print("The food court is bustling with activity, and it seems difficult to navigate.")
            print("Perhaps waiting for a while or finding an alternative route may be the way to go.\n")
            return True
        # If turn counter is between 55 and 60 - can move.
        elif 55 <= turn_counter < 60:
            print("As the clock approaches 4:55 PM, you notice a change in the atmosphere.")
            print("The vendors start closing their stalls, and the once-bustling crowd begins to disperse.")
            print("People are finishing their meals and heading towards the exits.")
            print("You are now able to proceed to the exit.\n")
            return False
        # Game over event if time has expired.
        else:
            print("It's past 5:00 PM, and the shops have closed. The remaining patrons have left.")
            print("You are now alone in the deserted food court.")
            print("You can't proceed further, and the exits are locked.\n")
            return True

    def look(self):
        """
        Provides a description of the room to be used with the look command.
        """
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
    """
    The class that represents the Lobby room object - which is the exit of the game.
    """
    def __init__(self):
        super().__init__("Lobby", "A spacious lobby with various shops and entrances. People are bustling around.", 1,
                         1)

    def look(self):
        """
        Provides a description of the room to be used with the look command.
        """
        print(f"You looked around the {self.name}")
        print("The Lobby is a spacious area bustling with activity. Various shops surround the central space, "
              "and people move about with purpose.")
        print("The air is filled with a mix of scents from nearby stores. The atmosphere is vibrant, and the sound of "
              "shoppers and conversations creates a lively symphony. To the south, you can see the Food Court, and to "
              "the east, the Electronics Store beckons.")


class Bank(Room):
    """
    Class that represents the Bank room object in the game.
    """
    def __init__(self):
        super().__init__("Bank", "A bank with counters and a waiting area. An eerie quiet hangs over the room in"
                                 "comparison to the business of where you have been so far.", 2, 2)

    def block_event(self, player, backpack):
        """
        Handles the block event for the Bank room (the Membership card side-quest).
        :param player: The player object.
        :param backpack: The backpack object.
        """
        mark = Mark()
        mark.block_exit(player, backpack)

    def look(self):
        """
        Provides a description of the room to be used with the look command.
        """
        print(f"You looked around the {self.name}")
        print("As you step inside, the scent of freshly printed money tickles your nose. The atmosphere is hushed, "
              "and the gentle hum of counting machines provides a soothing background noise. The sleek marble counters"
              " gleam under the soft glow of chandeliers.")
        print("A BANK TELLER is assisting people at the counter - she is efficiently processing transactions with a"
              "friendly smile")
        print("There are exits to the north, west and south - however a stern looking MAN blocks the north exit.")


class ElectronicsStore(Room):
    """
    Class that represents the Electronics Store room object in the game.
    """
    def __init__(self):
        super().__init__("Electronics Store", "A store filled with the latest gadgets and electronics.", 1, 2)

    def block_event(self, player, backpack):
        """
        Handles the block event for the Electronics store (ie; the scarf side-quest).
        :param player: The player.
        :param backpack: The backpack.
        :return:
        """
        olivia = Olivia()
        olivia.block_exit(player, backpack)

    def look(self):
        """
        Provides a description of the room to be used with the look command.
        """
        print(f"You looked around the {self.name}")
        print("You're surrounded by a dazzling display of cutting-edge gadgets and electronic marvels. Bright screens "
              "illuminate the space, showcasing the latest in technology.")
        print("Customers explore the aisles, mesmerized by the sleek devices on the shelves. The air is charged with "
              "the excitement of innovation. To the west, you can see the entrance to the Lobby, and to the south, "
              "a path leads to the Bank.")
        print('A WOMAN stands impatiently by the entrance to the Lobby, frequently checking her phone')


class ClothingBoutique(Room):
    """
    Class that represents the Clothing Boutique room object in the game.
    """
    def __init__(self):
        super().__init__("Clothing Boutique", "A fashionable boutique with racks of clothes and a fitting room.", 3, 2)

    def look(self):
        """
        Provides a description of the room to be used with the look command.
        """
        print(f"You looked around the {self.name}")
        print("Racks of stylish clothes adorn the walls, each garment vying for attention with its unique design and"
              " flair.")
        print("Soft lighting creates an inviting ambiance, and a fitting room in the corner beckons those eager to try "
              "on the latest trends. To the north, you can see the entrance to the Bank.")
        print("A friendly VENDOR stands by ready to assist you with your fashion choices")
