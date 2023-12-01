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
    turn_counter = 100;
    return player, turn_counter, food_court, lobby, bank, clothing_boutique, electronics_store


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

def get_command(item):
    print(f"You obtained {item}!")


def talk_command(person):
    print(f"You began talking to {person}")


##def leave_command:
    ##print(f"You left.")


def look_command(direction):
    print(f"You looked {direction}")

def end_game(self):
    """
    End the game by setting the game_over flag.
    """
    self.game_over = True


def main():
    player, food_court, lobby, bank, clothing_boutique, electronics_store, turn_counter = start_game()

    while True:
        show_instructions()

        if not player.game_over and turn_counter >= 0:
            print("What would you like to do?")
            choice_input = input("Please choose:").lower()

            if choice_input.startswith('move'):
                move_command(player)
                turn_counter -= 1
            elif choice_input.startswith('talk'):
                talk_command()
                turn_counter -= 1
            elif choice_input.startswith('look'):
                look_command()
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
            elif choice_input.startswith('wait'):
                print("You're just hanging around.")
                turn_counter -= 1
            else:
                print("That is not a valid option")
        elif turn_counter == 0:
                print("Game over!")
main()
