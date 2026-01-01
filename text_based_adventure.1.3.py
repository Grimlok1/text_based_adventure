from story import game, start
from ui import error, success
import os



def main():
    error_message = ""
    while True:
        choice = main_menu(error_message)
        if choice == "1":
            run_game()
            error_message = ""

        elif choice == "2":
            quit_game()

        else:
            error_message = "Invalid input!"

def run_game():
    commands = dict(bag = inventory_menu, b = inventory_menu, quit = quit_game)
    new_game()
    error_message = "" #reset after display

    while True:
        render_scene(error_message)
        error_message = "" #reset after display

        if not game.current_event.options:
            game_over()
            return

        action, value = ask_input(commands)

        if action == "event":
            game.current_event = value.get_next_event(game.flags)

        elif action == "command":
            value()

        elif action == "error":
            error_message = value

def render_scene(error_message=""):
    clear_screen()
    render_event()
    render_options()
    error(error_message)
    
def game_over():
    while True:
        clear_screen()
        print(game.current_event.description)
        error("Game over!")
        print("1. return to main menu")
        i = input("> ")
        if i == "1":
            return

def new_game():
    game.current_event = start
    game.flags = set()
    game.inventory = []
    for event in game.story:
        event.visited = False

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def render_options():
    if game.current_event.options:
        for key, option in game.current_event.get_options(game.flags).items():
            print(f"{key}. {option.description}\n")

def ask_input(commands):
    options = game.current_event.get_options(game.flags)
    choice = input("> ")

    if choice in options.keys():
        return ("event", options[choice])

    elif choice in commands:
        return ("command", commands[choice])

    else:
        return ("error", "Invalid input!")

def inventory_menu():
    message = ""
    while True:
        clear_screen()
        inventory = display_inventory(message)
        choice = input("> ")

        if choice in inventory.keys():
            message = f"{inventory[choice].name}: {inventory[choice].description}"

        elif choice == f"{len(inventory) + 1}":
            return

        else:
            message = "Invalid input!"

def quit_game():
    quit()

def display_inventory(message):
    inventory = {str(key) : item for (key, item) in enumerate(game.inventory, start=1)}
    print("Backpack items:")

    for key, item in inventory.items():
        print(f"{key}. {item.name}")
    print(f"{len(inventory) + 1}. close bag")
    print(f"\n{message}")

    return inventory

def render_event():
    event = game.current_event
    print(event.description)
    event.resolve(game)
      
def main_menu(error_message):
    clear_screen() 
    print("Welcome placeholder\n")
    print("1. Start game\n2. Quit game\n")
    error(error_message)

    return input("> ")

if __name__ == "__main__":
    main()
