from story import start
from scene import Game

def main():
    main_menu()

def game_loop():
    game = Game(start) #onko mahdollista importoida suoraan game object jolloin ei tarvitse antaa sitä functioille.
    
    while True:
        handle_event(game)
        
        if event.options:
            game.current_event = ask_choice(event)
        else:
            game.current_event = event.next_event
        
    
def ask_choice(game):
    options = game.current_event.get_options(game.flags)
    
    for i, option in enumerate(options, start=1):
        print(f"\n{i}. {option.description}\n")
        
    while True:    
        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(options):
                return options[choice].next_event
            else:
                print("invalid input")
        except ValueError:
            print("invalid value type")

def handle_event(game):
    game.current_event = event
    print(event.description)
    game.flags.update(event.flags)
    for treasure in event.treasure:
        print(f"{treasure.name} added to inventory")
        game.inventory.append(treasure)
        
def main_menu():
    print("Welcome placeholder\n")
    while True:
        choice = verify_input("1. Start game\n2. Quit game\n", ("1", "2"))
        if choice == "1":
            game_loop()
        elif choice == "2": #quit game
            break
            
    
def verify_input(promt, valid_options, fail_promt = "invalid input"):
    while True:
        user_choice = input(promt).strip().lower()
    
        if user_choice in valid_options:
            return user_choice
        else:
            print(fail_promt)
if __name__ == "__main__":
    main()
