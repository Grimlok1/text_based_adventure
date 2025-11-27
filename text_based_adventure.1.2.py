from story import story

def main():
    main_menu()

def game_loop():
    inventory = []
    current = "footsteps"
    while True:
        scene = story[current]
        print(scene.text)
        if scene.options:
            options = list(scene.options.keys())
            promt = create_promt(options)
            choice_index = verify_input(promt, ("1", f"{len(options)}"))
            choice = options[int(choice_index) - 1]
            current = scene.options[choice]
        else:
            print("Game over")
            break
                            
def main_menu():
    print("Welcome placeholder\n")
    while True:
        choice = verify_input("1. Start game\n2. Quit game\n", ("1", "2"))
        if choice == "1":
            game_loop()
        elif choice == "2": #quit game
            break
            
def create_promt(options):
        temp_list = []
        print("What do you do?")
        for i, key in enumerate(options, start=1):
            temp_list.append(f"{i}.\t{key}")
        promt = "\n".join(temp_list)
        return "\n" + promt + "\n"
        
def verify_input(promt, valid_options, fail_promt = "invalid input"):
    while True:
        user_choice = input(promt).strip().lower()
    
        if user_choice in valid_options:
            return user_choice
        else:
            print(fail_promt)
if __name__ == "__main__":
    main()
