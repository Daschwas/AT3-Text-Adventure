import random


class Item:
    """
    This class represents the items that can be held by the player and characters.
    """

    def __init__(self, name, description):
        """
        Parameters:
            Owner - The person or player that currently owns the item.
            Name - The name of the object.
            Description - A description of the item.
        """
        self.name = name
        self.description = description
        self.can_get = False

    def get_item(self, backpack):
        """
        Function that determines whether an object is fixed or not (ie; can be picked up or not).
        :param backpack: The player's backpack.
        """
        if self.can_get:
            backpack.add(self.name)
            print(f"You add {self.name} to your backpack")
        else:
            print("This will not fit inside your backpack!")

    def check_item(self):
        """
        Allows player to interact with a given item, which gives the description of the item.
        """
        print(f"You examine the {self.name}")
        print(f"{self.description}")

    def use_item(self, backpack):
        """
        A default use item method that can be used with different objects to interact with them.
        :param backpack: The player's backpack.
        """
        print(self.use)


class VendingMachine(Item):
    """
    A vending machine class that represents an in-game object that can be interacted with and offer water.

    Attributes:
        name - The name of the vending machine.
        description - Description of the vending machine.
        can_get - Determines if the vending machine can be added to the backpack or not.
    """
    def __init__(self, name):
        """
        Initializes a VendingMachine instance.
        :param name: Name of the vending machine.
        """
        super().__init__(name, description="A vending machine that offers a variety of refreshing drinks.")

    def check(self, backpack):
        """
        Allows the player to interact with the vending machine where they can check surroundings and buy drinks.
        :param backpack: The player's backpack.
        """
        print("You approach the vending machine.")
        print("The soft hum of the machine fills the air, and colorful buttons invite you to make a choice.")
        print("A digital display showcases a selection of beverages, each promising a burst of flavor.")
        print("You can almost taste the fizzy anticipation in the air.")
        choice = input("What would you like to do? ").lower().strip()
        if choice.startswith("get vending machine") and "drink" not in choice:
            self.get_item(backpack)
        elif choice.startswith("get") or choice.startswith("buy") or choice.startswith("purchase"):
            self.get_drink(backpack)
        elif choice.startswith("check") or choice.startswith("look"):
            direction = input("Where would you like to look? (left/right/behind): ").lower().strip()
            self.look(direction, backpack)
        print("You return to the entrance of the food court.")

    def get_drink(self, backpack):
        """
        Method to obtain drinks water from the vending machine.
        :param backpack: The player's backpack.
        """
        bottled_water = BottledWater("Bottled Water")
        print("You insert coins into the vending machine and purchase a bottle of water. It's refreshing!")
        bottled_water.get_item(backpack)

    def look(self, direction, backpack):
        """
        Allows the player to inspect different directions around the vending machine for events.
        :param direction: The direction to look (left/right/behind).
        :param backpack: The player's backpack.
        """
        scarf = Scarf("Dusty Scarf")
        has_scarf = backpack.in_backpack("Dusty Scarf") != -1
        # If player looks left of the vending machine.
        if direction == "left":
            print("You glance to the left of the vending machine and notice a small maintenance hatch.")
            print("It seems to be securely locked, preventing any unauthorized access.")
            print("Curiosity piques your interest, but there's no way to open it.\n")
        # If player looks right of the vending machine.
        elif direction == "right":
            print("Turning your attention to the right, you find a discarded soda can and a crumpled receipt.")
            print("It appears that the vending machine's visitors occasionally leave behind a trace of their presence.")
            # Random chance set to 1/30 for the player to find money.
            if random.randint(1, 30) == 1:
                print("While looking around, you see a coin on the ground.")
                print("Hey, it's $2. Lucky find! You add the money to your backpack\n")
                backpack.add_money(2)
            else:
                print("Nothing particularly useful catches your eye.\n")
        # If player looks behind vending machine.
        elif direction == "behind":
            # Ensures player can't find multiple copies of the same scarf.
            if has_scarf:
                print("The bag still sits there but nothing new of note is there since you last checked.")
                print("People are beginning to give you odd looks as your rifle behind the vending machine yet again.")
                # Event that allows the player to find an alternative scarf, so they don't need to buy it.
            else:
                print("Peeking behind the vending machine, you discover a dusty corner with a forgotten bag.")
                print("It looks like someone left this behind - you wonder what happened to them?")
                choice = input("Do you want to look inside the bag? Yes/No")
                if choice == "yes":
                    print("You look inside the bag - there appears to be a scarf. It must have sitting there for some "
                          "time as it is caked in a layer of dust")
                    second_choice = input("What would you like to do?")
                    if second_choice.startswith("get"):
                        print("The scarf. Why shouldn't you keep it?")
                        print("Perhaps it will come in handy some day.")
                        scarf.get_item(backpack)
                    else:
                        print("The only dust-based clothing you want to see is the outer cover of a book.")
                else:
                    print("Some things are better left undisturbed.")
                    print("You cannot see anything else of note and return to the front of the vending machine.")
                    print("Hopefully, the owner returns for this bag someday.\n")
        else:
            print("You look around but find nothing noteworthy.\n")


class BottledWater(Item):
    """
    Class that represents a bottled water object.

    Attributes:
        Name - The name of the water.
        Description - The description of the water.
        Can_get - Whether the water can be picked up or not.
    """
    def __init__(self, name):
        """
        Initializes an instance of the BottledWater.
        """
        super().__init__(name, description="A refreshing bottle of water!")
        self.can_get = True

    def use_item(self, backpack):
        """
        Allows the player to use the water - which then removes it from the backpack.
        :param backpack: The player's backpack.
        """
        print("You drink the bottle of water and feel refreshed!\n")
        backpack.remove(self)


class BlankCard(Item):
    """
    Class that represents a blank ID card to be used in a side-quest.

    Attributes:
        Name - The name of the card.
        Description - The description of the card.
        Can_get - Whether the card can be picked up or not.
    """
    def __init__(self, name):
        """
        Initializes an instance of the BlankCard.
        """
        super().__init__(name, description="A blank ID card that belongs to Josh. It's seen better days.\n")
        self.can_get = True

    def use_item(self, backpack):
        """
        Allows the player to use the item which then writes some flavour text.
        :param backpack: The player's backpack.
        """
        print("You're not sure what to use the Blank Card on. Maybe you could use something on it?\n")


class FakeCard(Item):
    """
    Class that represents the Fake Card which is made from the Blank ID card.

    Attributes:
        Name - The name of the card.
        Description - The description of the card.
        Can_get - Whether the card can be picked up.
    """
    def __init__(self, name):
        """
        Initializes an instance of the FakeCard.
        """
        super().__init__(name,
                         description="You've written your name on the card - it might pass for a Membership card.")
        self.can_get = True

    def use_item(self, backpack):
        """
        Allows the player to use the item which then writes some flavour text.
        :param backpack: The player's backpack.
        """
        print("You flash the fake membership card confidently, hoping it fools someone.?\n")


class MembershipCard(Item):
    """
    Class that represents the Membership Card object which can be purchased.
    """
    def __init__(self, name):
        """
        Initializes an instance of the MembershipCard object.
        """
        super().__init__(name,
                         description="A membership card that grants access to exclusive benefits. It belongs to the "
                                     "tech club.")
        self.can_get = True

    def use_item(self, backpack):
        """
        Allows the player to use the item which then writes some flavour text.
        :param backpack: The player's backpack.
        """
        print(
            "You proudly display the membership card to those around you, bragging about gaining access to exclusive "
            "areas.\n")


class Scarf(Item):
    """
    Class that represents the scarf object used in a side-quest - there are two types (Dusty and Warm).
    """
    def __init__(self, name):
        """
        Initializes an instance of the Scarf object.
        """
        super().__init__(name, description="A cozy and stylish scarf.")
        self.can_get = True

    def use_warm_item(self, backpack):
        """
        Allows the player to use the item which then writes some flavour text (changes depending on scarf type).
        :param backpack: The player's backpack.
        """
        print(f"You wrap the scarf around yourself, feeling warm and stylish.")
        print(f"Maybe a bit too warm. You take the scarf off.\n")

    def use_dusty_item(self, backpack):
        """
        Allows the player to use the item which then writes some flavour text (changes depending on scarf type).
        :param backpack: The player's backpack.
        """
        print(f"You wrap the scarf around yourself, and a cloud of dust emerges.")
        print(f"You take the scarf off, coughing all the while.\n")


class Watch(Item):
    """
    Class that represents the watch item which is a high value item that leads to a win scenario.
    """
    def __init__(self, name):
        """
        Initializes an instance of the Watch object.
        """
        super().__init__(name, description="A stylish and trendy watch.")
        self.can_get = True

    def use_item(self, backpack, turn_counter):
        """
        Allows the player to use the item which then shows the current time.
        :param backpack: The player's backpack.
        :param turn_counter: The current time in game.
        """
        print(f"You check the time on your stylish watch. It's 4.{turn_counter} pm.\n")


class Pen(Item):
    """
    Class that represents the pen item which is used in a side-quest.
    """
    def __init__(self, name):
        """
        Initializes an instance of the Pen object.
        """
        super().__init__(name, description="A basic ballpoint pen. It writes smoothly and is perfect for quick notes.")
        self.can_get = True

    def use_item(self, backpack):
        """
        Allows the player to use the pen on other items. Needed for a side-quest.
        :param backpack: The player's backpack.
        """
        print("You whip out the pen you stole from the bank teller.")
        choice = input("What would you like to use the pen on? ").lower().strip()
        if choice.startswith("blank") and backpack.in_backpack("Blank ID Card") != -1:
            print("You write your name on the Blank ID Card.")
            print("Could this maybe pass as a Membership Card?")
            backpack.remove("Blank ID Card")
            fake_card = FakeCard("Fake ID Card")
            backpack.add(fake_card.name)
        elif choice == "paperwork" and backpack.in_backpack("Bank Paperwork") != -1:
            print("You make some quick notes on the paperwork.")
        elif choice == "loan document" and backpack.in_backpack("Loan Document") != -1:
            print("You scribble on the loan document. Is this really a good idea?")
        elif (choice.endswith("bottle") or choice.endswith("water")) and backpack.in_backpack("Bottled Water") != -1:
            print("You write your name on the water bottle. Is there anything else you could write your name on?")
        else:
            print("That's not a valid option.\n")


class Paperwork(Item):
    """
    Class that represents the paperwork item which is a red herring.
    """
    def __init__(self, name):
        """
        Initializes an instance of the Paperwork object.
        """
        super().__init__(name, description="A set of paperwork. It appears to be official bank documents.")
        self.can_get = True

    def use_item(self, backpack):
        """
        Allows the player to use the item which then writes some flavour text.
        :param backpack: The player's backpack.
        """
        print("You browse through the paperwork, gaining some insights into the complex world of finance.\n")


class LoanDocument(Item):
    """
    Class that represents the Loan Document item.
    There are two types depending on if a fake name is used or not, which affects whether the player wins or not.
    """
    def __init__(self, name):
        """
        Initializes an instance of the LoanDocument object.

        Also has flag that determines if the loan document has a fake name on it or not.
        """
        super().__init__(name, description="A document outlining the terms of an interest-free loan. "
                                           "Read carefully; the fine print states it comes with a 'free' interest.")
        self.can_get = True
        self.fraudulent = False

    def get_description(self):
        """
        Custom description depending on whether a fake name has been used or not.
        """
        print("A seemingly innocuous document, but the fine print reveals it comes with a hefty 80% weekly "
              "interest rate.")
        if self.fraudulent:
            print("You, wisely, have signed it with a fake name.\n")

    def check_item(self):
        """
        Method to be used with get_description so different descriptions are used depending on the fraudulent flag.
        """
        print(f"You examine the {self.name}")
        print(self.get_description())

    def use_item(self, backpack):
        """
        Allows the player to use the item which then writes some flavour text.
        :param backpack: The player's backpack.
        """
        print("You carefully review the loan document, contemplating its terms and potential consequences.\n")


class Camera(Item):
    """
    Class that represents the Camera item. This is a high value item that allows the player to 'win' the game.
    """
    def __init__(self, name):
        """
        Initializes an instance of the Camera object.
        """
        super().__init__(name, description="A sleek and modern camera with advanced features at a great price. It "
                                           "promises to capture memories in vivid detail. This be a valuable addition "
                                           "to your collection.")
        self.can_get = True

    def use_item(self, backpack):
        """
        Allows the player to use the item which then writes some flavour text.
        :param backpack: The player's backpack.
        """
        print("You take out the camera and capture a memorable moment. The advanced features ensure a "
              "stunning photo.\n")
