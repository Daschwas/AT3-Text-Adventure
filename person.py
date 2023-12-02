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
            choice = input("Is there anything else you would like to do?").lower().strip()
            if "ID" or "card" in choice:
                self.give_blank_card(player, backpack)
            else:
                print(f"{self.name} Nothing else? Then bother me later.")
            print("You return to the entrance to the food court.")


        def give_blank_card(self, player, backpack):
            if BlankCard in [type(item) for item in self.items]:
                blank_card = next(item for item in self.items if isinstance(item, BlankCard))
                self.items.remove(blank_card)
                backpack.add(blank_card)
                print(f"{self.name}:  You want my employee card...? You know what, sure, I was looking for an excuse to quit "
                      "anyway.")
                print(f"{self.name}: That's part of the reason why I never wrote my name on this thing.")
                print(f"{self.name} gives you a Blank ID Card. Maybe you'll find a use for it!")
            else:
                print(f"{self.name}:What else do you want? Bother me later.")


class Mary(Person):
    def __init__(self):
        super().__init__("Mary", "A salesperson at the Clothing Boutique.")
        self.items.append(Scarf("Warm Scarf"))
        self.items.append(Watch("Stylish Watch"))

    def greet(self, player, backpack):
        print(f"{self.name}: Hello there! I'm {self.name}, and I work at the Clothing Boutique.")
        print(f"{self.name}: Would you like to have a look at our selection?")
        choice = input("Do you want to see the selection? (Yes/No): ").lower().strip()
        if choice == "yes":
            self.offer_items(player, backpack)
        else:
            print(f"{self.name}: No worries - see you around!")
        print("You return to the entrance of the boutique.")


    def offer_items(self, player, backpack):
        print(f"{self.name}: Welcome to the Clothing Boutique! Take a look at our selection:")
        for index, item in enumerate(self.items, start=1):
            print(f"{index}. {item.name}")
        choice = input("What would you like to buy?): ").lower().strip()
        self.sell_item(player, choice, backpack)

    def sell_item(self, player, item, backpack):
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
            print(f"{self.name}: I'm sorry, but we don't sell {item.name} right now.")


class Olivia(Person):
    def __init__(self):
        super().__init__("Olivia", "A person hanging by the exit to the electronics store - she seems to be impatiently"
                                   "waiting for someone.")
        self.items.append(None)

    def greet(self, player, backpack):
        print(f"{self.name}: I'm waiting for a friend. She should be here any minute...")
        if backpack.in_backpack("scarf"):
            self.give_scarf(backpack)
        print("You return to the entrance of the electronics store.")

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
        print(f"{self.name}: Oh, that's the scarf I wanted!")
        choice = input("Will you give her the scarf? (Yes/No):").lower().strip()
        if choice == "yes":
            backpack.remove(scarf)
            print(f"{self.name}: Thanks for the scarf! It's really warm.")
        else:
            print(f"{self.name}: No, of course - I understand...")
            print(f"{self.name}: I hope my friend arrives soon so I can go get one for myself.")

class Mark(Person):
    def __init__(self):
        super().__init__("Mark", "A stern-looking security guard at the entrance to the secret store.")
        self.items.append(MembershipCard("Membership Card"))

    def greet(self, player, backpack):
        has_id = backpack.in_backpack("fake card")
        has_card = backpack.in_backpack("membership card")

        if has_id or has_card:
            print(f"{self.name}: Always good to see one of our loyal clients.")
        else:
            print(f"{self.name}: Members only through here, mate. Or are you looking to purchase a membership?")
            choice = input("Do you want to buy a membership card? (Yes/No): ").lower().strip()
            if choice == "yes":
                self.sell_membership_card(player, backpack)
            else:
                print(f"{self.name}: Alright, then scram.")
        print("You return to the entrance of the bank.")

    def block_exit(self, backpack):
        print("You are prevented from moving ")
        membership_card = MembershipCard("Membership Card")
        fake_card = FakeCard("Fake ID Card")

        if backpack.in_backpack(fake_card):
            print(f"{self.name}: Oh, you are a member after all? You must be longtime client - I don't recognise"
                  f"that design!")
            print(f"{self.name}: Well, come on through.")
            return False
        elif backpack.in_backpack(membership_card):
            print(f"{self.name}: Ah, one of ")
            return False
        else:
            print(f"{self.name}: Sorry, mate - members only through here, I'm afraid.")
            print(f"{self.name}: I can sell you a pass, though. What do you say?")
            return True

    def sell_membership_card(self, backpack):
        membership_card = MembershipCard("Membership Card")
        if MembershipCard or FakeCard in [type(item) for item in backpack.items]:
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
        print("You return to the entrance of the bank.")

    def sell_interest_free_loan(self, player, backpack):
        loan_document= LoanDocument("Loan Document")
        if backpack.in_backpack(loan_document):
            print(f"{self.name}: I love the enthusiasm, but we need to be sure you can pay it back, sorry.")
        else:
            backpack.add(loan_document)
            print(f"{self.name}: Here you go, one interest free loan.")
            print(f"{self.name}:Oh? No, it's not free of interest - it comes with a 'free' loan!")
            print(f"{self.name}:That's 80% weekly interest you will need to pay back. Enjoy!")

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

class Kento(Person):
    def __init__(self):
        super().__init__("Kento", "The vendor at the Electronics Store.")

    def greet(self, player, backpack):
        scarf = Scarf("Warm Scarf")
        print(f"{self.name}: Welcome to the Electronics Store! If you need the latest gadgets, you're in the right place.")
        if backpack.in_backpack(scarf) != -1:
            print(f"{self.name}: Oh, that's a nice scarf you've got there! I heard a customer here talking about that"
                  f"very design - must be chilly outside since it's so popular!")
        print(f"{self.name}: We actually have a great deal on at the moment - our Canon EOS R5 model camera is 80% off!")
        choice = input("Would you like to buy? Yes/No:  ").lower().strip()
        if choice == "yes":
            self.sell_item(player, backpack)
        print("You return to the entrance to the food court.")

    def sell_item(self, player, backpack):
        camera = Camera("Camera")
        if backpack.in_backpack(camera):
            print(f"{self.name}: Wait, haven't you bought one already? One per customer, I'm afraid!")
        else:
            backpack.add(camera)
            print(f"{self.name}: Here you go, one Canon. Enjoy!")
