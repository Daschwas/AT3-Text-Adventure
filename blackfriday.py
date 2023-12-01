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

current_room = 'Food Court'


rooms = {
    'Food Court': {'North': 'Lobby', 'East': 'Bank'},
    'Lobby': {'South': 'Food Court', 'East': 'Electronics Store'},
    'Bank': {'North': 'Electronics Store', 'West': 'Food Court', 'South': 'Clothing Boutique'},
    'Electronics Store': {'West': 'Lobby', 'South': 'Bank'},
    'Clothing Boutique': {'North': 'Bank'},
}
"""
Dictionary representing the layout of rooms in the shopping center.

Each room is a key in the dictionary, and its value is another dictionary describing the bordering rooms in each 
cardinal direction.
"""

directions = ['North', 'East', 'South', 'West']
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