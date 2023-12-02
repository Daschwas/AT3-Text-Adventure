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

        def greet(self, player, backpack):
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


class Olivia(Person):
    def __init__(self):
        super().__init__("Olivia", "A person hanging by the exit to the electronics store - she seems to be impatiently"
                                   "waiting for someone.")
        self.items.append(None)

    def greet(self):
        print(f"{self.name}: I'm waiting for a friend. She should be here any minute...")

    def block_exit(self, backpack):
        scarf = Scarf("Warm Scarf")
        if scarf in backpack.items:
            print(f"{self.name}: Oh! Oh! Thank you so much - how did you know I was looking for this?")
            return False
        else:
            print(f"{self.name}: How long is she going to take? I really hope they don't sell "
                  f"out of the scarf I want before I get there...")
            return True

    def give_scarf(self, backpack):
        scarf = Scarf("Warm Scarf")
        self.items[0] = scarf
        backpack.remove(scarf)
        print(f"{self.name}: Thanks for the scarf! It's really warm.")


class Mark(Person):
    def __init__(self):
        super().__init__("Mark", "A stern-looking security guard at the entrance to the secret store.")
        #self.items.append(MembershipCard("Membership Card"))

    def greet(self):
        print(f"{self.name}: Members only through here, mate. Or are you looking to purchase a membership?")

    def block_exit(self, backpack):
        print("You are prevented from moving ")
        #membership_card = MembershipCard("Membership Card")
        blank_card = BlankCard("Blank ID Card")

        if blank_card in backpack.items:
            print(f"{self.name}: Oh, you are a member after all? You must be longtime client - I don't recognise"
                  f"that design!")
            print(f"{self.name}: Well, come on through.")
            return False
        #elif membership_card in backpack.items:
            #print(f"{self.name}: Ah, one of ")
            #return False
        else:
            print(f"{self.name}: Sorry, mate - members only through here, I'm afraid.")
            print(f"{self.name}: I can sell you a pass, though. What do you say?")
            return True

    def sell_membership_card(self, backpack):
        membership_card = MembershipCard("Membership Card")
        if MembershipCard in [type(item) for item in backpack.items]:
            print(f"{self.name}: You can't become a member twice, mate.")
        else:
            backpack.add(membership_card)
            print(f"{self.name}: Here you go, one Membership card.")

class Katie(Person):
    def __init__(self):
        super().__init__("Katie", "The friendly bank teller at the counter.")
        self.items.append(Pen("Bank Pen"))
        self.items.append(Paperwork("Bank Paperwork"))
    def greet(self, player, backpack):
        has_paperwork = backpack.in_backpack("paperwork")
        has_pen = backpack.in_backpack("pen")

        if has_paperwork or has_pen:
                print(f"{self.name}: Hello again. Are you here as a genuine client or just to stock up on more stationery?")
        else:
            print(f"{self.name}: Hello there! I'm {self.name}, the bank teller. How can I assist you today?")
            print(f"{self.name}: Oh, by the way, I can offer you an interest-free loan. It's only 50 credits. Would you like "
              f"to buy one?")

        print(f"{self.name} gestures to the pen and paperwork sitting in front of her")

        choice = input("Do you want to buy an interest-free loan? (Yes/No): ").lower().strip()
        if choice == "yes":
            self.sell_interest_free_loan(player, backpack)
        elif choice == "get":
            self.get_command(player, backpack)
        else:
            print(f"{self.name}: Alright, let me know if you change your mind. Have a great day!")

    def sell_interest_free_loan(self, player, backpack):
        pass

    def get_command(self, player, backpack):
        choice = input("What would you like to take?").lower().strip()
        if choice == "paperwork":
            print("You stuff the paperwork into your backpack and quickly walk away from the table.")
            print(f"{self.name}: Hey! Wait! I need you to sign that here!")
            print(f"{self.name} shoots you a dirty look as you return to the entrance of the bank")
            backpack.add(Paperwork("Bank Paperwork"))
        elif choice == "pen":
            print("You stuff the pen into your backpack and quickly walk away from the table.")
            print(f"{self.name}: Hey! Wait! I need you to sign that here!")
            print(f"{self.name} shoots you a dirty look as you return to the entrance of the bank")
            backpack.add(Pen("Bank Pen"))
        else:
            print("There's nothing to take of that description.")
