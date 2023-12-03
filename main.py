from commands import *
from player import Player
from backpack import BackPack


def start_game():
    """
        Initialize the game by creating instances of rooms and NPCs, and creating the player character.

        Returns:
            tuple: A tuple containing instances of player, rooms, backpack, and NPCs for the game.
    """
    food_court = FoodCourt()
    lobby = Lobby()
    bank = Bank()
    clothing_boutique = ClothingBoutique()
    electronics_store = ElectronicsStore()
    player = create_player(food_court)
    # sets opening money value of player to $40
    backpack = BackPack([], 40)
    josh = Josh()
    mary = Mary()
    mark = Mark()
    olivia = Olivia()
    katie = Katie()
    kento = Kento()
    return player, food_court, lobby, bank, clothing_boutique, electronics_store, backpack, josh, mary, mark, olivia, \
        katie, kento,


def create_player(starting_room):
    """
    Creates a player character by allowing the user to input the player.name field and initializing a Player instance.
    :param starting_room: The room where the player starts their adventure.
    :return: new_player: The player character for the game.
    """
    player_name = input("Enter your name: ")
    new_player = Player(player_name, starting_room)
    return new_player


def main():
    """
    This is the main loop of the game ("Code Black (Friday)").

    It initializes the game and handles the player input. It also allows the user to replay the game once finished.
    """
    while True:
        player, food_court, lobby, bank, clothing_boutique, electronics_store, backpack, josh, mary, olivia, mark, \
            katie, kento = start_game()
        turn_counter = 0
        show_introduction()

        # handles the different command choices
        while not player.game_over and turn_counter <= 60:
            print(f"You are currently in the {player.room.name}.")
            print(f"What would you like to do? \n")
            choice_input = input("Please choose: ").lower().strip()

            # Move command
            if choice_input.startswith('move'):
                move_command(player, backpack, turn_counter)
                turn_counter += 1
            # Check command
            elif choice_input.startswith('check'):
                turn_counter += 1
                check_command(player, backpack, turn_counter)
            # Talk command
            elif choice_input.startswith('talk'):
                talk_command(player, backpack, [josh, mary, olivia, katie, mark, kento])
                turn_counter += 1
            # Look command
            elif choice_input.startswith('look'):
                look_command(player, backpack)
                turn_counter += 1
            # Get command
            elif choice_input.startswith('get'):
                get_command(player, backpack)
                turn_counter += 1
            # Use command
            elif choice_input.startswith('use'):
                use_item(backpack, turn_counter)
                turn_counter += 1
            # Help command
            elif choice_input.startswith('help'):
                help_command()
            # Wait command
            elif choice_input.startswith('wait'):
                print("You're just hanging around.")
                turn_counter += 2
            # Invalid command
            else:
                print("That is not a valid option")

        # lose scenario if player runs out of time
        if turn_counter >= 60:
            print("As the clock strikes 5:00 PM, an unsettling quiet descends upon the now-deserted shops.")
            print("The once-bustling halls are now eerily silent, and the emptiness amplifies every creak and groan.")
            print("You attempt to open the exit, but the heavy doors refuse to budge.")
            print("The only sound is the echo of your footsteps, hauntingly loud in the empty space.")
            print("It dawns on you that you're trapped, alone, until someone comes to free you on Monday.")
            print("The solitude stretches ahead, and the abandoned shops seem to watch silently.")
            print("Looks like you're in for a long, uneasy weekend...\n")
            print("Game over!")

        # play again option
        play_again = input("Do you want to play again? (yes/no): \n").lower()
        if play_again != 'yes':
            break


if __name__ == "__main__":
    main()
