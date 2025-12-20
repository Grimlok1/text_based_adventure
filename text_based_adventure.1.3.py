from story import start, game

def main():
    main_menu()

def game_loop():
    event = start
    while True:
        event.event_description()
        
        if event.options:
            event = ask_choice(event)
            
        #automatic transition    
        else:
            event = event.next_event
    
def ask_choice(event):
    options = event.get_options(game.flags)
    
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
