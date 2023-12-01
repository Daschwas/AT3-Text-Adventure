from backpack import *

class Item:

    """
    This class represents the items that can be held by the player and characters.
    """
    def __init__(self, name, description):
        """
        Parameters:
            Owner - The person or player that currently owns the item.
            Name - The name of the object.
            Description - A description of the itemn.
        """
        self.name = name
        self.description = description
        self.can_get = False
    def get_item(self, backpack):
        if self.can_get == True:
            backpack.add(self.name)
        else:
            print("This will not fit inside your backpack!")

class VendingMachine(Item):
    def __init__(self, name):
        super().__init__(name, description="A vending machine that offers a variety of refreshing drinks.")

    def get_drink(self, backpack):
        bottled_water = BottledWater("Bottled Water")
        print("You insert coins into the vending machine and purchase a bottle of water. It's refreshing!")
        backpack.add(bottled_water)

class BottledWater(Item):
    def __init__(self, name):
        super().__init__(name, description="A refreshing bottle of water!")
        self.can_get = True

    def use_drink(self, backpack):
        print("You drink the bottle of water and feel refreshed!")
        backpack.remove(self)


class BlankCard(Item):
    def __init__(self, name):
        super().__init__(name, description="A blank ID card that belongs to Josh. It's seen better days.")
        self.can_get = True

class Scarf(Item):
    def __init__(self, name):
        super().__init__(name, "A cozy and stylish scarf.")
        self.can_get = True

