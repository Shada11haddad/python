
def adventure_game():
    print("Welcome to the Kingdom of Eldoria!")
    name = input("What is your name, adventurer? ")
    print(f"Greetings, {name}. Your journey begins now.")

    print("\nYou stand at the edge of the Whispering Woods. There are three paths ahead:")
    print("1. The Overgrown Path")
    print("2. The River Route")
    print("3. The Shadowed Pass")

    choice = input("Which path will you take? (Type 'overgrown', 'river', or 'shadowed'): ").lower()

    if choice == "overgrown":
        print("\nYou brave the Overgrown Path, where shadows whisper your name.")
        print("Halfway through, you meet Lady Evanna, a sorceress cloaked in violet.")
        trust_evanna = input("Will you trust her guidance? (yes or no): ").lower()

        if trust_evanna == "yes":
            print("Evanna leads you through the treacherous maze, shielding you from harm.")
            print("You emerge safely on the other side, her magic saving your life.")
        else:
            print("Ignoring her warning, you face the spectral guardian alone.")
            print("The battle is fierce, and though you survive, you are badly injured.")

    elif choice == "river":
        print("\nYou take the River Route, where the water sparkles deceptively.")
        print("A thief named Thrain appears, offering his guidance for a price.")
        trust_thrain = input("Do you accept his help? (yes or no): ").lower()

        if trust_thrain == "yes":
            print("Thrain guides you past hidden dangers but steals a trinket from your bag.")
        else:
            print("Without Thrain’s help, you are ambushed by bandits and lose valuable supplies.")

    elif choice == "shadowed":
        print("\nYou climb the Shadowed Pass, the cliffs steep and dangerous.")
        print("Sir Cedric, a valiant knight, offers his assistance.")
        accept_cedric = input("Do you accept his help? (yes or no): ").lower()

        if accept_cedric == "yes":
            print("Cedric’s strength saves you from a deadly fall, and his tales bolster your courage.")
        else:
            print("You climb alone, narrowly escaping disaster. The journey leaves you shaken.")

    else:
        print("\nConfused by indecision, you wander aimlessly until the dangers of the woods claim you.")
        return

    print("\nAfter surviving the path, you arrive at Malakar’s fortress.")
    print("The fortress looms before you, its towers piercing the sky.")
    print("You must decide how to proceed:")
    print("1. Sneak through the sewers.")
    print("2. Storm the gates.")
    print("3. Scale the walls.")

    fortress_choice = input("How will you enter? (sewer, gates, or walls): ").lower()

    if fortress_choice == "sewer":
        print("\nYou endure the filth and traps of the sewers, emerging unseen within the fortress.")
    elif fortress_choice == "gates":
        print("\nYou and your allies distract the guards and storm the gates. The battle is fierce but successful.")
    elif fortress_choice == "walls":
        print("\nUnder the cover of night, you scale the walls. A slip nearly costs your life, but you recover and proceed undetected.")
    else:
        print("\nIndecision causes you to falter. You are discovered and captured by Malakar’s guards.")
        return

    print("\nAt last, you stand before Lord Malakar himself.")
    print("His voice booms through the throne room: 'Join me, and together we will rule, or face your doom.'")

    final_choice = input("Will you join Malakar or fight him? (join or fight): ").lower()

    if final_choice == "join":
        print("\nYou betray your allies and join Malakar. Eldoria falls into darkness under your rule.")
    elif final_choice == "fight":
        print("\nYou engage in a fierce battle with Malakar. Summoning all your strength, you deliver the final blow.")
        print("The Orb of Eternity is reclaimed, and peace returns to Eldoria. You are hailed as a hero!")
    else:
        print("\nYour hesitation costs you dearly. Malakar strikes you down, and Eldoria is lost.")

    print("\nThank you for playing, brave adventurer!")

# Start the game
adventure_game()