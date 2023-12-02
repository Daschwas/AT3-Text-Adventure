from item import *


class Person:
    """
    This class represents the NPCs that inhabit the world.
    """

    def __init__(self, name, description):
        """
        Parameters:
             Name - The name of the non player character.
             Items - A list that shows the current items held by the NPC.
             Description -
             On_Shift - This is a state that shows whether the postman is currently working or not. It is switched off
             when the player runs out of 'turns' as the world then switches off.
        """
        self.name = name
        self.items = []
        self.on_shift = False
        self.description = description


class Josh(Person):
        def __init__(self):
            super().__init__("Josh", "A friendly guy who works at the food court. He's seen better days.")
            self.items.append(BlankCard("Blank ID Card"))

        def greet(self):
            print(f"{self.name}:  Hey, I'm {self.name}. I'm off shift at the moment - can you bother me later?")

        def give_blank_card(self, backpack):
            if BlankCard in [type(item) for item in self.items]:
                blank_card = next(item for item in self.items if isinstance(item, BlankCard))
                self.items.remove(blank_card)
                backpack.add(blank_card)
                print(f"{self.name}:  You want my employee card...? You know what, sure, I was looking for an excuse to quit "
                      "anyway.")
                print(f"{self.name}: That's part of the reason why I never wrote my name on this thing.")
                print(f"{self.name} gives you a Blank ID Card. Maybe you'll find a use for it!")
            else:
                print("What else do you want? Bother me later.")


class Mary(Person):
    def __init__(self):
        super().__init__("Mary", "A salesperson at the Clothing Boutique.")
        self.items.append(Scarf("Warm Scarf"))
        self.items.append(Watch("Stylish Watch"))

    def greet(self):
        print(f"{self.name}: Hello there! I'm {self.name}, and I work at the Clothing Boutique.")

    def offer_items(self):
        print(f"{self.name}: Welcome to the Clothing Boutique! Take a look at our selection:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.name}")

    def sell_item(self, item, backpack):
        if self.items <=1:
            print(f"{self.name}: Sorry, I can't sell everything to you!")
        elif item in self.items:
            if backpack.in_backpack(item) != -1:
                print(f"You already have a {item.name}! You don't need another one.")
            else:
                self.items.remove(item)
                backpack.add(item)
                print(f"{self.name} sells you a {item.name}. Enjoy your purchase!")
        else:
            print(f"{self.name}: I'm sorry, but I don't have {item.name} in stock right now.")