from room import *
from player import *
from backpack import *
from item import *
from person import *


def start_game():
    """
        Initialize the game by creating instances of rooms, defining their exits, and creating the player character.

        Returns:
            Player: The player character for the game.
    """
    food_court = FoodCourt()
    lobby = Lobby()
    bank = Bank()
    clothing_boutique = ClothingBoutique()
    electronics_store = ElectronicsStore()
    player = create_player(food_court)
    backpack = BackPack([])
    josh = Josh()
    mary = Mary()
    olivia = Olivia()
    katie = Katie()
    kento = Kento()
    return player, food_court, lobby, bank, clothing_boutique, electronics_store, backpack, josh, mary, olivia, katie, kento


def create_player(starting_room):
    player_name = input("Enter your name: ")
    print(f"{starting_room.name}")
    new_player = Player(player_name, starting_room)
    print(f"{new_player.room.name}")
    print(f"{new_player.room.description}")
    return new_player


def show_introduction():
    """
    Display the welcome message and instructions for the 'Code Black (Friday)' text-based adventure game.
    """
    print("Welcome to 'Code Black (Friday)'!")
    print("It's 2:00 PM on Friday, November 24, 2023.")
    print("Black Friday is in full swing, and you've been enjoying a long lunch in the food court.")
    print("As you check the time, you realize the crowds are growing, and you must navigate the shopping center "
          "strategically to survive and snag a great deal.")
    print("\nInstructions:")
    print("- Use the following commands in combination with an object or person: 'Get', 'Use', 'Check', 'Talk', 'Leave', "
          "and 'Look'.")
    print("If you are ever stuck, type 'Help' for advice")
    print("- Use 'Move' in combination with 'North', 'East', 'South', and 'West' to explore the map.")
    print("- Your ultimate goal: Escape. Survive. Shop.")



def move_command(player):
    """
       Manage the player's movement between rooms based on user input.

       Parameters:
            player (Player): The player.
    """
    current_room = player.room
    print(f"You are in the {current_room.name}")
    while True:
        choice = input("Where would you like to move?").lower()
        print(choice)
        if choice in {'north', 'south', 'east', 'west'}:
            player.move_rooms(choice)
            break
        else:
            print("Invalid choice. Try again.")

def talk_command(player, backpack, npcs):
    npc_name = input("Who would you like to talk to?").lower().strip()
    if (npc_name == "man" or npc_name == "employee") and isinstance(player.room, FoodCourt):
        npc_name = "josh"
    if (npc_name == "man" or npc_name == "guard") and isinstance(player.room, Bank):
        npc_name = "mark"
    if (npc_name == "woman" or npc_name == "employee" or npc_name.startswith("bank")) and isinstance(player.room, Bank):
        npc_name = "katie"
    if (npc_name == "woman" or npc_name == "employee" or npc_name.endswith("vendor")) and isinstance(player.room,
                                                                                                     ClothingBoutique):
        npc_name = "mary"
    if (npc_name == "woman") and isinstance(player.room, ElectronicsStore):
        npc_name = "olivia"
    selected_npc = next((npc for npc in npcs if npc.name.lower() == npc_name), None)

    if selected_npc:
        selected_npc.greet(player, backpack)
    else:
        print(f"There's no one around matching the description of {npc_name}.")


def get_command(item):
    print(f"You obtained {item}!")




##def leave_command:
    ##print(f"You left.")


def look_command(player):
    player.room.look()

def check_command(player, backpack):
    print(f"What would you like to check?")
    print(f"Type 'map' to check the map and 'backpack' to check your backpack.")
    print(f"Otherwise type an object if you wish to check that out.")
    check_input = input("Please choose:").lower().strip()
    if check_input.startswith('map'):
        player.game_map.display_map()
    elif check_input.startswith('backpack'):
        backpack.list()

def end_game(self):
    """
    End the game by setting the game_over flag.
    """
    self.game_over = True

def help_command():
    """
    Display help information about the game controls.
    """
    print("Game Controls:")
    print("- 'Move': Move to a different room.")
    print("- 'Talk': Interact with a person in the current room.")
    print("- 'Check': Interact with an object in the current room.")
    print("- 'Look': Examine your surroundings.")
    print("- 'Leave': Leave the current room/conversation.")
    print("- 'Get': Pick up an item.")
    print("- 'Use': Use an item in your inventory.")
    print("- 'Help': Display this help message.")


def main():
    player, food_court, lobby, bank, clothing_boutique, electronics_store, backpack, josh, mary, olivia, katie, kento = start_game()
    turn_counter = 100
    show_introduction()

    while True:

        if not player.game_over and turn_counter >= 0:
            print(f"You are currently in the {player.room.name}")
            print("What would you like to do?")
            choice_input = input("Please choose:").lower().strip()

            if choice_input.startswith('move'):
                move_command(player)
                turn_counter -= 1
            elif choice_input.startswith('check'):
                check_command(player, backpack)
                turn_counter -= 1
            elif choice_input.startswith('talk'):
                talk_command(player, backpack, [josh, mary, olivia])
                turn_counter -= 1
            elif choice_input.startswith('look'):
                look_command(player)
                turn_counter -= 1
            elif choice_input.startswith('leave'):
                #leave_command()
                turn_counter -= 1
            elif choice_input.startswith('get'):
                get_command()
                turn_counter -= 1
            elif choice_input.startswith('use'):
                #use_command()
                turn_counter -= 1
            elif choice_input.startswith('help'):
                help_command()
            elif choice_input.startswith('wait'):
                print("You're just hanging around.")
                turn_counter -= 1
            else:
                print("That is not a valid option")
        elif turn_counter == 0:
                print("Game over!")
main()