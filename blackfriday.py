from room import *
from player import *
from backpack import *
from item import *


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
    return player, food_court, lobby, bank, clothing_boutique, electronics_store


def create_player(starting_room):
    player_name = input("Enter your name: ")
    print(f"{starting_room.name}")
    new_player = Player(player_name, starting_room)
    print(f"{new_player.room.name}")
    print(f"{new_player.room.description}")
    return new_player


def show_instructions():
    """
    Display the welcome message and instructions for the 'Code Black (Friday)' text-based adventure game.
    """
    print("Welcome to 'Code Black (Friday)'!")
    print("It's 2:00 PM on Friday, November 24, 2023.")
    print("Black Friday is in full swing, and you've been enjoying a long lunch in the food court.")
    print("As you check the time, you realize the crowds are growing, and you must navigate the shopping center "
          "strategically to survive and snag a great deal.")
    print("\nInstructions:")
    print("- Use the following commands in combination with an object or person: 'Get', 'Check', 'Talk', 'Leave', "
          "and 'Look'.")
    print("- Use 'Move' in combination with 'North', 'East', 'South', and 'West' to explore the map.")
    print("- Your ultimate goal: Escape. Survive. Shop.")



def choice_manager(player):
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
        if choice in directions:
            player.move_rooms(choice)
            break
        else:
            print("Invalid choice. Try again.")

directions = ['north', 'east', 'south', 'west']
"""
List of cardinal directions for navigating around the game map.

This list includes the available cardinal directions that players can use to move between rooms.
"""

look_directions = ['Up', 'Down', 'Left', 'Right']


def move_command(direction):
    print(f"You moved {direction}.")

def get_command(item):
    print(f"You obtained {item}!")


def talk_command(person):
    print(f"You began talking to {person}")


##def leave_command:
    ##print(f"You left.")


def look_command(direction):
    print(f"You looked {direction}")

def main():
    player, food_court, lobby, bank, clothing_boutique, electronics_store = start_game()
    while True:
        show_instructions()
        choice_manager(player)

main()
