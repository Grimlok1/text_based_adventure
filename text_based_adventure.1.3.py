from story import story

def main():
    main_menu()

def game_loop():
    inventory = []
    flags = set()
    current = "footsteps"
    while True:
        scene = story[current]
        print(scene.text)
        
        if scene.reward:
            for reward in scene.reward:
                print(f"You recived a {reward}")
                inventory.append(reward)
                
        if scene.set_flags:
            flags.update(scene.set_flags)
                
        if scene.options:
            current = ask_choice(scene.options, flags)
            
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
            
def ask_choice(options, flags):
    promt = ""
    print("What do you do?\n")
    
    for i, option in enumerate(options, start=1):
        promt += f"{i}.\t{option.label}\n"
        
    choice_index = verify_input(promt, ("1", f"{len(options)}"))
    targets = options[int(choice_index) - 1].targets
    choice = choose_option_scene(targets, flags)
    
    return choice
    
def choose_option_scene(targets, flags):
    # 1. First pass: check flagged targets
    for target in targets:
        if target.conditions and set(target.conditions).issubset(flags):
            return target.scene

    # 2. Second pass: choose the default target
    for target in targets:
        if not target.conditions:
            return target.scene

    return None  # or raise error if you expect a fallback always

def verify_input(promt, valid_options, fail_promt = "invalid input"):
    while True:
        user_choice = input(promt).strip().lower()
    
        if user_choice in valid_options:
            return user_choice
        else:
            print(fail_promt)
if __name__ == "__main__":
    main()
