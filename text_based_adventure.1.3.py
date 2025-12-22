from story import game

def main():
    main_menu()

def game_loop():
    while True:
        event = game.current_event

        describe_event()
        if event.options:
            game.current_event = ask_input()
        else:
            print("Game over")
            break

            
def ask_input():
    while True:
        options = game.current_event.get_options(game.flags)
        
        for key, option in options.items():
            print(f"{key}. {option.description}\n")
        choice = input("> ")
        if choice in options.keys():
            return options[choice].next_event
        else:
            print("invalid input")

def describe_event():
    event = game.current_event
    print(event.description)

    if event.flag:
        game.flags.add(event.flag)

    for treasure in event.treasure:
        print(f"{treasure.name} added to inventory\n")
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
