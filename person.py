import time

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
             Description - A description of the NPC.
             On_Shift - This is a state that shows whether the postman is currently working or not. It is switched off
             when the player runs out of 'turns' as the world then switches off.
        """
        self.name = name
        self.items = []
        self.on_shift = False
        self.description = description


class Josh(Person):
    """
    Represents the NPC Josh, a friendly guy who works at the food court.
    """
    def __init__(self):
        super().__init__("Josh", "A friendly guy who works at the food court. He's seen better days.")
        # Item to give to player for use in the side-quest.
        self.items.append(BlankCard("Blank ID Card"))

    def greet(self, player, backpack):
        """
        Greets the player and offers a Blank ID Card if requested.
        """
        # Different dialogue trees depending on whether the player has the card or not.
        if backpack.in_backpack("Blank ID Card") != -1:
            print(f"{self.name} glances up as you approach.")
            print(f"{self.name}: Again? ")
        elif backpack.in_backpack("Fake ID Card") != -1:
            print(f"{self.name} glances up as you approach.")
            print(f"{self.name}: Did you write your name on my card? {player.name}, dude. Whatever.")
        else:
            print(f"You approach the tired looking man. His hat and employee card sit on the table next to him.")
            print(f"He glances up as you approach.")
            print(f"You notice his employee card is completely blank - I guess you'll need to ask for his name.")
            print(f"{self.name}: I'm {self.name}. Anyway,")

        print(f"{self.name}: I'm off shift at the moment - can you bother me later?")
        choice = input("Is there anything else you would like to do with Josh? ").lower().strip()
        if choice.endswith("id") or choice.endswith("card"):
            self.give_blank_card(player, backpack)
        elif choice.endswith("hat"):
            print(f"{self.name}: You want my hat? That's the last thing I would be willing to give away.")

        else:
            print(f"{self.name}: Nothing else? Then get out of my space, thanks.")
        print("You return to the entrance to the food court.")

    def give_blank_card(self, player, backpack):
        """
        Provides the user with the Blank ID Card for use in a side-quest.
        """
        # Determines if the NPC still has the Blank Card or not.
        if BlankCard in [type(item) for item in self.items]:
            blank_card = next(item for item in self.items if isinstance(item, BlankCard))
            self.items.remove(blank_card)
            backpack.add(blank_card.name)
            print(
                f"{self.name}: You want my employee card...? You know what, sure, I was looking for an excuse to quit "
                "anyway.")
            print(f"{self.name}: That's part of the reason why I never wrote my name on this thing.")
            print(f"{self.name} gives you a Blank ID Card. Maybe you'll find a use for it!")
        else:
            print(f"{self.name}: What else do you want? Bother me later.")


class Mary(Person):
    def __init__(self):
        """
        Represents the NPC Mary, a salesperson at the Clothing Boutique.
        """
        super().__init__("Mary", "A salesperson at the Clothing Boutique.")
        # Items to sell
        self.items.append(Scarf("Warm Scarf", 33))
        self.items.append(Watch("Stylish Watch", 26))

    def greet(self, player, backpack):
        """
        Greets the player and offers items for sale at the Clothing Boutique.
        """
        print(f"{self.name}: Hello there! I'm {self.name}, and I work at the Clothing Boutique.")
        # Determines if the NPC still has items to sell
        if Scarf or Watch in [type(item) for item in self.items]:
            print(f"{self.name}: Would you like to have a look at our selection?")
            choice = input("Do you want to see the selection? (Yes/No): ").lower().strip()
            if choice == "yes":
                self.offer_items(player, backpack)
            else:
                print(f"{self.name}: No worries - see you around!")
        else:
            print(f"{self.name}: We're plum out of items today, sorry!")
        print("You return to the entrance of the boutique.")

    def offer_items(self, player, backpack):
        """
        Displays the list of items for sale by Katie, depending on what the user has already bought.
        """
        # Flags for if the user has already purchased items.
        has_scarf = backpack.in_backpack("Warm Scarf") != -1
        has_watch = backpack.in_backpack("Stylish Watch") != -1
        if len(self.items) < 1:
            print(f"{self.name}: Sorry, I can't sell everything to you!")
        else:
            print(f"{self.name}: Welcome to the Clothing Boutique! Take a look at our selection:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item.name} (${item.cost})")
            choice = input("What would you like to buy?): ").lower().strip()
            # Different options depending on what has been purchased already.
            if choice == "1" and has_scarf:
                self.sell_item(player, f"Stylish Watch", backpack)
            elif choice == "1":
                self.sell_item(player, f"Warm Scarf", backpack)
            elif choice == "2" and has_watch:
                print(f"{self.name}: I didn't give that option...")
            elif choice == "2":
                self.sell_item(player, f"Stylish Watch", backpack)
            else:
                print(f"{self.name}: Please pick one of our items.")

    def sell_item(self, player, choice, backpack):
        """
        Sells specific items to the user which are then added to the backpack.
        """
        selected_item = None
        for item in self.items:
            if item.name == choice:
                selected_item = item
                break

        # Prevents player from buying multiple of the same item.
        if selected_item:
            if backpack.in_backpack(selected_item.name) != -1:
                (time.sleep(1))
                print(f"You already have a {selected_item.name}! You don't need another one.")
            elif selected_item.cost > backpack.money:
                print(f"{self.name}: I'm sorry, but you don't have the funds for our {selected_item.name}...")
            else:
                self.items.remove(selected_item)
                backpack.add(selected_item.name)
                print(f"{self.name} sells you a {selected_item.name}. Enjoy your purchase!")
                backpack.remove_money(selected_item.cost)
        else:
            print(f"{self.name}: I'm sorry, but we don't sell that item right now.")


class Olivia(Person):
    """
    Represents the NPC Olivia, who blocks the player's way at the Electronic Store unless given a scarf.
    """
    def __init__(self):
        """
        Initializes an instance of Olivia.
        """
        super().__init__("Olivia", "A person hanging by the exit to the electronics store - she seems to be impatiently"
                                   "waiting for someone.")
        self.items.append(None)

    def greet(self, player, backpack):
        """
        Greets player and calls the give scarf method if they have one.

        :param player: The player.
        :param backpack: The player's backpack.
        """
        has_scarf = backpack.in_backpack("Warm Scarf") != -1 or backpack.in_backpack("Dusty Scarf") != -1
        print(f"{self.name}: I'm waiting for a friend. She should be here any minute...")
        if has_scarf:
            self.give_scarf(player, backpack)
        print("You return to the entrance of the electronics store.")

    def block_exit(self, player, backpack):
        """
        Block event called by the Electronics Store object.
        Prevents the player from proceeding if they have not given Olivia a scard.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        # Flags that determine if the player has a scarf or not.
        has_scarf = backpack.in_backpack("Warm Scarf") != -1
        has_dusty = backpack.in_backpack("Dusty Scarf") != -1
        if not player.given_scarf:
            if has_scarf or has_dusty:
                self.give_scarf(player, backpack)
            else:
                print(f"{self.name}: How long is she going to take? I really hope they don't sell "
                      f"out of the scarf I want before I get there...")
        else:
            print(f"{self.name}: Thank you again!")

    def give_scarf(self, player, backpack):
        """
        Function that allows the player to give Olivia a scarf and proceed with the game.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        print(f"{self.name}: Oh, that's the scarf I wanted!")
        choice = input("Will you give her the scarf? (Yes/No): ").lower().strip()
        if choice == "yes":
            # Different events depending on which scarf the player has.
            if backpack.in_backpack("Warm Scarf") != -1:
                backpack.remove("Warm Scarf")
                print(f"{self.name}: Thanks for the scarf! It's really warm.")
                player.given_scarf = True
            else:
                backpack.remove("Dusty Scarf")
                print(f"{self.name}: Oh! Oh! Thank you! It's...not quite what I imagined.")
                player.given_scarf = True
        else:
            print(f"{self.name}: No, of course - I understand...")
            print(f"{self.name}: I hope my friend arrives soon so I can go get one for myself.")


class Mark(Person):
    """
    Represents the NPC Mark who blocks the player's way to the Electronics Store unless they have a membership.
    """
    def __init__(self):
        """
        Initializes an instance of the Mark object.
        """
        super().__init__("Mark", "A stern-looking security guard at the entrance to the secret store.")
        self.items.append(MembershipCard("Membership Card", 15))

    def greet(self, player, backpack):
        """
        Greets the player and gives them the option to purchase a membership card.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        has_membership = backpack.in_backpack("Membership Card") != -1
        has_id = backpack.in_backpack("Fake ID Card") != -1

        # Greeting is determined by membership status.
        if has_id or has_membership:
            print(f"{self.name}: Always good to see one of our loyal clients.")
        else:
            print(f"{self.name}: Members only through here, mate. Or are you looking to purchase a membership?")
            choice = input("Do you want to buy a membership card? (Yes/No): ").lower().strip()
            if choice == "yes":
                self.sell_membership_card(player, backpack)
            else:
                print(f"{self.name}: Alright, then scram.")
        print("You return to the entrance of the bank.")

    def block_exit(self, player, backpack):
        """
        Block event called by Bank that prevents the player from progressing unless they have a membership.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        print("You are prevented from moving")
        has_membership = backpack.in_backpack("Membership Card") != -1
        has_id = backpack.in_backpack("Fake ID Card") != -1
        # Whether the player can progress is determined by if they are a member or not.
        if not player.is_member:
            print(f"{self.name}: Sorry, mate - members only through here, I'm afraid.")
            if has_id:
                print(f"{self.name}: Oh, you are a member after all? You must be longtime client - I don't recognise"
                      f" that design...")
                print(f"{self.name}: Well, come on through.")
                player.is_member = True
            elif has_membership:
                print(f"{self.name}: Ah, one of our regulars - please come through.")
                player.is_member = True
            else:
                print(f"{self.name}: I can sell you a pass, though. What do you say?")
                choice = input("Do you want to buy a membership card? (Yes/No): ").lower().strip()
                if choice == "yes":
                    self.sell_membership_card(player, backpack)
        else:
            print(f"{self.name}: Ah, back again? Please, come through sir.")

    def sell_membership_card(self, player, backpack):
        """
        Allows the user to purchase a membership card and proceed with the game.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        # Different flags depending on whether the player has a card or fake card which prevents buying another.
        membership_card = MembershipCard("Membership Card", 15)
        has_membership = backpack.in_backpack("Membership Card") != -1
        has_id = backpack.in_backpack("Fake ID Card") != -1
        print(f"{self.name}: So, you want to buy a Membership, yeah? Only ${membership_card.cost}.")
        choice = input("Buy membership? (Yes/No): ").lower().strip()
        if choice == "yes":
            if has_id or has_membership:
                print(f"{self.name}: You can't become a member twice, mate.")
            elif membership_card.cost > backpack.money:
                print(f"{self.name}: You're broke? Don't wast my time, mate.")
            else:
                backpack.add(membership_card.name)
                print(f"{self.name}: Here you go, one Membership card.")
                backpack.remove_money(membership_card.cost)
                print(f"{self.name}: Come back and show me that and I'll let ya through.")
        else:
            print(f"{self.name}: Stop wasting my time, then.")


class Katie(Person):
    """
    Represents the NPC at the Bank who can offer the player more money - at a price.
    """
    # The amount of money she will loan to the player.
    loan_amount = 30
    def __init__(self):
        """
        Initalises an instance of the Katie object.
        """
        super().__init__("Katie", "The friendly bank teller at the counter.")
        # NPCs inventory.
        self.items.append(Pen("Bank Pen"))
        self.items.append(Paperwork("Bank Paperwork"))

    def greet(self, player, backpack):
        """
        Greets the player and allows them to take a pen/paperwork or sign up for a loan.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        has_paperwork = backpack.in_backpack("Bank Paperwork") != -1
        has_pen = backpack.in_backpack("Bank Pen") != -1

        # If the player thinks to use get, they can steal a pen or paperwork.
        # The pen can be used in a side-quest.
        # Different dialogue is used if the player has already taken the object.
        if has_paperwork or has_pen:
            print(f"{self.name}: Hello again. Are you here as a genuine client or just to stock up on more stationery?")
        else:
            print(f"{self.name}: Hello there! I'm {self.name}, the bank teller. How can I assist you today?")
            print(
                f"{self.name}: Oh, by the way, I can offer you an interest-free ${self.loan_amount} loan. Would you "
                f"like to buy one?")

        print(f"{self.name} gets your attention by gesturing to the pen and paperwork sitting in front of her")

        # Choice tree to allow the user to sign up for a loan.
        choice = input("Do you want to buy an interest-free loan? (Yes/No): ").lower().strip()
        if choice == "yes":
            self.sell_interest_free_loan(player, backpack)
        elif choice == "get":
            self.get_command(player, backpack)
        else:
            print(f"{self.name}: Alright, let me know if you change your mind. Have a great day!")
        print("You return to the entrance of the bank.")

    def sell_interest_free_loan(self, player, backpack):
        """
        Method that allows the user to sign up for a loan and get more money.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        loan_document = LoanDocument("Loan Document")
        fraud_document = LoanDocument("Loan Document with Fake Name")
        fraud_document.fraudulent = True

        # Prevents player from taking multiple loans
        if backpack.in_backpack("Loan Document") != -1 or backpack.in_backpack("Loan Document with Fake Name") != -1:
            (time.sleep(1))
            print(f"{self.name}: I love the enthusiasm, but we need to be sure you can pay it back, sorry.")
        else:
            print(f"{self.name}: I'll just get you to write your name here, if that's okay!")
            signed_name = input("Please write your name: \n")
            # If statement that determines if the player used a fake name or not when signing for the loan.
            # The name is matched against the name the player enters for the character at the start of the game.
            if signed_name == player.name:
                print(f"You quickly write {signed_name} at the bottom of the document.\n")
                backpack.add(loan_document.name)
            else:
                print(f"You scribble {signed_name} at the bottom of the document instead of your real name.\n")
                backpack.add(fraud_document.name)
            # Adds money to the player's account.
            print(f"{self.name}: Here you go, one interest free loan.")
            print(f"You gained ${self.loan_amount}.")
            backpack.add_money(self.loan_amount)
            print(f"{self.name}: Oh? No, it's not free of interest - it comes with a 'free' loan!")
            print(f"{self.name}: That's 80% weekly interest you will need to pay back. Enjoy!\n")
            (time.sleep(1))
            if signed_name == player.name:
                print("Welp.")
            else:
                print("Well, it's a good thing you used a fake name then...")

    def get_command(self, player, backpack):
        """
        Method that is called if 'get' keyword is used when greeting Katie.
        It allows the player to take either a pen or the paperwork.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        bank_pen = Pen("Bank Pen")
        paperwork = Paperwork("Bank Paperwork")
        choice = input("What would you like to take?").lower().strip()
        # If player takes paperwork.
        if choice == "paperwork":
            print("You stuff the paperwork into your backpack and quickly walk away from the table.")
            print(f"{self.name}: Hey! Wait! I need you to sign that here!")
            print(f"{self.name} shoots you a dirty look as you return to the entrance of the bank")
            backpack.add(paperwork.name)
        # If player takes pen.
        elif choice == "pen":
            print("You stuff the pen into your backpack and quickly walk away from the table.")
            print(f"{self.name}: Hey! Wait! I need you to sign that here!")
            print(f"{self.name} shoots you a dirty look as you return to the entrance of the bank")
            backpack.add(bank_pen.name)
        else:
            print("There's nothing to take of that description.")


class Kento(Person):
    """
    Represents the NPC that sells items at the Electronics store.
    """
    def __init__(self):
        """
        Initalises an instance of the Kento object.
        """
        super().__init__("Kento", "The vendor at the Electronics Store.")
        # Kento's list of items
        self.items.append(Camera("Camera", 25))

    def greet(self, player, backpack):
        """
        Greet method that plays when the player speaks to the NPC.
        :param player: The player.
        :param backpack: The player's backpack.
        """
        # NPC gives a hint if the player has a warm or dusty scarf.
        has_scarf = backpack.in_backpack("Warm Scarf") != -1 or backpack.in_backpack("Dusty Scarf") != -1
        print(
            f"{self.name}: Welcome to the Electronics Store! If you need the latest gadgets, you're in "
            f"the right place.")
        if has_scarf:
            print(f"{self.name}: Oh, that's a nice scarf you've got there! I heard a customer here talking about that"
                  f" very design - must be chilly outside since it's so popular!")
        print(
            f"{self.name}: We actually have a great deal on at the moment - our Canon EOS R5 model camera is 80% off!")
        choice = input("Would you like to buy? Yes/No:  ").lower().strip()
        # Allows the player to purchase items from the NPC.
        if choice == "yes":
            self.sell_item(player, backpack)
        print("You return to the entrance to the electronics store.")

    def sell_item(self, player, backpack):
        """
        Method that sells items to the player.
        :param player: The player.
        :param backpack: The backpack.
        """
        camera = Camera("Camera", 25)
        print(f"{self.name}: Alright, that'll be ${camera.cost}, please!")
        # Stops the player buying multiple cameras.
        if backpack.in_backpack("Camera") != -1:
            (time.sleep(1))
            print(f"{self.name}: Wait, haven't you bought one already? One per customer, I'm afraid!")
        elif camera.cost > backpack.money:
            print(f"{self.name}: Sorry, looks like you don't have enough money...")
            print(f"{self.name}: Feel free to come back later!")
        else:
            backpack.add(camera.name)
            backpack.remove_money(camera.cost)
            print(f"{self.name}: Here you go, one Canon. Enjoy!")
