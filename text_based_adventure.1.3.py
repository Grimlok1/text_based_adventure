from story import game, start
from ui import error, success
import os



def main():
    error_message = ""
    while True:
        choice = main_menu(error_message)
        if choice == "1":
            game_loop()
            error_message = ""

        elif choice == "2":
            quit_game()

        else:
            error_message = "Invalid input!"

def game_loop():
    commands = dict(bag = open_inventory, b = open_inventory, quit = quit_game)
    new_game()

    while True:
        clear_screen()
        describe_event()
        display_options()

        if not game.current_event.options:
            print("Game over")
            break

        ask_input(commands)

def new_game():
    game.current_event = start
    game.flags = set()
    game.inventory = []
    for event in game.story:
        event.visited = False

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_options():
    if game.current_event.options:
        for key, option in game.current_event.get_options(game.flags).items():
            print(f"{key}. {option.description}\n")

def ask_input(commands):
    options = game.current_event.get_options(game.flags)
    while True:
        choice = input("> ")

        if choice in options.keys():
            game.current_event = options[choice].next_event
            return

        elif choice in commands:
            commands[choice]()
            return

        else:
            clear_screen()
            describe_event()
            display_options()
            error("Invalid input!\n")

def open_inventory():
    clear_screen()
    inventory = display_inventory()

    while True:
        choice = input("> ")

        if choice in inventory.keys():
            clear_screen()
            display_inventory()
            print(f"> {inventory[choice].name}: {inventory[choice].description}\n")

        elif choice == f"{len(inventory) + 1}":
            clear_screen()
            break

        else:
            clear_screen()
            display_inventory()
            error("Invalid input!\n")

def quit_game():
    quit()

def display_inventory():
    inventory = {str(key) : item for (key, item) in enumerate(game.inventory, start=1)}
    print("Backpack items:")

    for key, item in inventory.items():
        print(f"{key}. {item.name}")
    print(f"{len(inventory) + 1}. close bag")

    return inventory

def describe_event():
    event = game.current_event
    print(event.description)

    if event.flag:
        game.flags.add(event.flag)

    for treasure in event.treasure:
        success(f"{treasure.name} added to inventory\n")

    if not event.visited:
        game.inventory.extend(event.treasure)
        event.visited = True
      
def main_menu(error_message):
    clear_screen() 
    print("Welcome placeholder\n")
    print("1. Start game\n2. Quit game\n")
    error(error_message)

    return input("> ")

            
def verify_input(promt, valid_options, fail_promt = "invalid input"):
    while True:
        user_choice = input(promt).strip().lower()
    
        if user_choice in valid_options:
            return user_choice
        else:
            print(fail_promt)
if __name__ == "__main__":
    main()
