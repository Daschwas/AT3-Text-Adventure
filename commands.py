from room import *
import random


def end_game(player, backpack):
    """
    Display's different messages at the end of the game depending on what the player has achieved.
    Then sets the player's game over flag to true so the user can replay the game.

    :param player: The player.
    :param backpack: The player's backpack.
    """
    has_camera = backpack.in_backpack("Camera") != -1
    has_watch = backpack.in_backpack("Stylish Watch") != -1
    has_loan = backpack.in_backpack("Loan Document") != -1
    has_fraud = backpack.in_backpack("Loan Document with Fake Name") != -1

    print("As the clock strikes 5:00 PM, you find yourself at the exit of the bustling shopping mall.")

    # win scenario: escaping with a camera and no loan
    if has_camera and not has_loan:
        print("Congratulations! You successfully navigated the maze of shops, capturing vibrant and memorable moments "
              "with your new camera.")
        print("The snapshots of laughter, dazzling storefronts, and unexpected encounters will be cherished forever.")
        print("It's been a successful and enjoyable shopping adventure!")
    # win scenario: escaping with a watch and no loan
    elif has_watch and not has_loan:
        print("You glance at your new stylish watch and realize you spent the day strolling through the mall, "
              "enjoying its ambiance.")
        print("Not only did you get the item of your desire, the experience itself was also worth every moment.")
        print("You leave the mall with a sense of contentment.")
    # lose scenario: escaping with no valuable items
    else:
        print("Unfortunately, your shopping spree didn't go as planned and you leave largely empty-handed.")
        print("Better luck next time!")
        player.game_over = True

    # extra flavour text if player successfully fooled bank teller
    if has_fraud:
        print("You breathe a sigh of relief as you realise you narrowly escaped taking on a heavy loan by using a "
              "fake name.")
        print("It's a reminder to be cautious and honest in financial dealings. Dodging that bullet was a close call!")

    # lose scenario: has camera but also has loan
    if has_camera and has_loan:
        print("Despite the joy of capturing moments with your new camera, you can't shake the uneasy feeling of having "
              "a signed loan document in your backpack.")
        print("The terms look challenging, and the weight of potential debt lingers. It's a lesson learned about the "
              "importance of financial responsibility.")
        player.game_over = True
    # lose scenario: has watch but also has loan
    elif has_watch and has_loan:
        print("You weigh the pros and cons of your purchases. The camera brought joy, but the signed loan document "
              "brings a sense of responsibility.")
        print("The terms look challenging, and the weight of potential debt lingers. It's a lesson learned about the "
              "importance of financial responsibility.")
        player.game_over = True
    # lose scenario: has loan
    elif has_loan:
        print("You exit the mall with a signed loan document in your backpack. The terms look challenging.")
        print("Hopefully, you can manage the repayments. It's a reminder to be cautious about what you agree to.")
        player.game_over = True

    # checks if player "won"
    if not player.game_over:
        print("You win! Your shopping adventure was huge success!")
        player.game_over = True
    # extra flavour text if player loses
    else:
        print(
            "Game Over! Whether it was the maze-like layout or unexpected challenges, this shopping trip didn't go as "
            "planned.")
        print("Better luck next time! The mall is always open for new adventures.")


def use_item(backpack, turn_counter):
    """
    Allows the player to use an item currently in their backpack.

    :param backpack: The player's backpack.
    :param turn_counter: The turn counter representing the time.
    :return:
    """
    backpack.list()
    used_item_name = input("What would you like to use? ").strip()

    if backpack.in_backpack(used_item_name) != -1:
        item_instance = create_item_instance(used_item_name)

        if item_instance:
            if isinstance(item_instance, Scarf):
                if item_instance.name == "Dusty Scarf":
                    item_instance.use_dusty_item(backpack)
                elif item_instance.name == "Warm Scarf":
                    item_instance.use_warm_item(backpack)
                else:
                    print(f"You can't use the {item_instance.name} in this way.")
            elif isinstance(item_instance, Watch):
                item_instance.use_item(backpack, turn_counter)
            else:
                item_instance.use_item(backpack)
        else:
            print("You can't use that item.")
    else:
        print("You don't have that item in your backpack.")


def create_item_instance(item_name):
    """
    Creates an instance of an item depending on it's name which is then used in the use function.
    :param item_name: The name of the item.
    :return: An instance of the corresponding item class.
    """
    item_mapping = {
        "warm scarf": Scarf("Warm Scarf"),
        "stylish watch": Watch("Stylish Watch"),
        "bottled water": BottledWater("Bottled Water"),
        "blank card": BlankCard("Blank Card"),
        "fake card": FakeCard("Fake Card"),
        "membership card": MembershipCard("Membership Card"),
        "scarf": Scarf("Scarf"),
        "watch": Watch("Stylish Watch"),
        "bank pen": Pen("Bank Pen"),
        "paperwork": Paperwork("Bank Paperwork"),
        "loan document": LoanDocument("Loan Document", "Loan Document with Fake Name"),
        "camera": Camera("Camera")
    }

    return item_mapping.get(item_name)


def help_command():
    """
    Display help information about the game controls.
    """
    print("Game Controls:")
    print("- 'Move': Move to a different room.")
    print("- 'Talk': Interact with a person in the current room.")
    print("- 'Check': Interact with an object in the current room.")
    print("- 'Look': Examine your surroundings.")
    print("- 'Get': Pick up an item.")
    print("- 'Use': Use an item in your inventory.")
    print("- 'Help': Display this help message.")


def show_introduction():
    """
    Display the welcome message and instructions for the 'Code Black (Friday)' text-based adventure game.
    """
    print("Welcome to 'Code Black (Friday)'!")
    print("It's 4:00 PM on Friday, November 24, 2023.")
    print("Black Friday is in full swing, and you've been enjoying a long lunch in the food court.")
    print("As you check the time, you realize the crowds are growing, and you must navigate the shopping center "
          "strategically to survive and snag a great deal.")
    print("\nInstructions:")
    print(
        "- Use the following commands in combination with an object or person: 'Get', 'Use', 'Check', 'Talk', 'Leave', "
        "and 'Look'.")
    print("If you are ever stuck, type 'Help' for advice")
    print("- Use 'Move' in combination with 'North', 'East', 'South', and 'West' to explore the map.")
    print("- Your ultimate goal: Escape. Survive. Shop.")


def move_command(player, backpack, turn_counter):
    """
       Manage the player's movement between rooms based on user input.

       Parameters:
            player (Player): The player.
            backpack (Backpack): The player's backpack.
            turn_counter: The current turn counter representing the in game time.
    """
    current_room = player.room
    print(f"You are in the {current_room.name}")
    choice = input("Where would you like to move?").lower()
    print(choice)
    if choice in {'north', 'south', 'east', 'west'}:
        player.move_rooms(choice, backpack, turn_counter)
    else:
        print("Invalid choice. Try again.")


def talk_command(player, backpack, npcs):
    """
    Handles the player's attempt to talk to different instances of the person class (ie; NPCs) within the game.

    :param player: The player.
    :param backpack: The player's backpack.
    :param npcs: List of instances of the person class within the current room.
    """
    npc_name = input("Who would you like to talk to?").lower().strip()
    if (npc_name == "man" or npc_name == "employee") and isinstance(player.room, FoodCourt):
        npc_name = "josh"
    if (npc_name == "man" or npc_name == "guard") and isinstance(player.room, Bank):
        npc_name = "mark"
    if (npc_name == "woman" or npc_name == "employee" or npc_name.startswith("bank") or npc_name.endswith("teller")) \
            and isinstance(player.room, Bank):
        npc_name = "katie"
    if (npc_name == "woman" or npc_name == "employee" or npc_name.endswith("vendor")) and isinstance(player.room,
                                                                                                     ClothingBoutique):
        npc_name = "mary"
    if (npc_name == "woman") and isinstance(player.room, ElectronicsStore):
        npc_name = "olivia"
    if (npc_name == "man") or npc_name == "employee" or npc_name.endswith("vendor") and isinstance(player.room,
                                                                                                   ElectronicsStore):
        npc_name = "kento"
    selected_npc = next((npc for npc in npcs if npc.name.lower() == npc_name), None)

    if selected_npc:
        selected_npc.greet(player, backpack)
    else:
        print(f"There's no one around matching the description of {npc_name}.")


def get_command(player, backpack):
    """
    This function handles the user inputting the get command to try and obtain an item.
    It also provides some hints on what to do in the game depending on the keyword entered.

    :param player: The player.
    :param backpack: The player's backpack.
    """
    has_scarf = backpack.in_backpack("Warm Scarf") != -1
    choice = input("Who would you like to get?").lower().strip()
    if (choice.endswith("card") or choice.endswith("ID") or choice.endswith("hat")) and isinstance(player.room,
                                                                                                   FoodCourt):
        print("You'll have to approach the man first before you can take his items.")
    elif choice.endswith("deal") or choice.endswith("bargain"):
        print("You can't see any around at the moment - but you do really want a new watch or camera.")
    elif choice.endswith("scarf"):
        if has_scarf:
            print("You put the scarf on for a moment, before deciding it is not quite your style.")
        else:
            if isinstance(player.room, ClothingBoutique):
                print("You cannot see a scarf lying around - maybe try the Clothing Boutique?")
            else:
                print("You cannot see a scarf lying around but the clothing store salesperson may sell one.")
    else:
        print(f"You try to find {choice} but to no avail.")


def look_command(player, backpack):
    """
    Displays information about the current room and (at random) gives the player an opportunity to get more money.
    :param player: The player.
    :param backpack: The player's backpack.
    """
    player.room.look()
    # handles a random event that the player can find some money, preventing game over from running out of funds
    # This has been set to a 1/23 chance but these odds can be changed.
    if random.randint(1, 23) == 1:
        print("While looking around, you see a coin on the ground.")
        print("Hey, it's $1. Lucky find! You add the dollar to your backpack")
        backpack.add_money(1)


def check_command(player, backpack, turn_counter):
    """
    Handles the player's attempt to check different elements within the game when they use the check keyword.

    :param player: The player.
    :param backpack: The player's backpack.
    :param turn_counter: The current turn counter representing the time.
    """
    print(f"What would you like to check?")
    print(f"Type 'map' to check the map and 'backpack' to check your backpack.")
    print(f"Type 'room' if you want to check out your surroundings.")
    print(f"Type 'time' if you want to check the current time.")
    print(f"Otherwise type an object if you wish to check that out.")
    check_input = input("Please choose:").lower().strip()
    # Checks map
    if check_input.startswith('map'):
        player.game_map.display_map()
    # Checks backpack inventory
    elif check_input.startswith('backpack'):
        backpack.list()
    # Checks room
    elif check_input == "room":
        look_command(player, backpack)
    # Checks the current time based on the turn_counter
    elif check_input == "time":
        if turn_counter <= 9:
            print(f"It is 4.0{turn_counter} pm")
        else:
            print(f"It is 4.{turn_counter} pm")
    # Allows player to check vending machine.
    elif check_input.startswith("vending") and isinstance(player.room, FoodCourt):
        player.room.room_check(backpack)
    # Checks wallet.
    elif check_input == "wallet" or "money":
        print(f"You have ${backpack.money}.")
    else:
        print(f"You check {check_input} but it does not exist. Passerby's look at you oddly.")
