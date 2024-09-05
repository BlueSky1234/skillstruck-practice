words = {
    1 : "Horizon",
    2 : "Velocity",
    3 : "Fragment",
    4 : "Epoch",
    5 : "Quiver",
    6 : "Nexus",
    7 : "Zenith",
    8 : "Cascade",
    9 : "Euphoria",
    10 : "Solstice",
    11 : "Labyrinth"
    }
def hangman(number):
    turns = 12
    guessing = [x.lower() for x in words.get(number)]
    guessing_set = set(guessing)
    correct = set()

    while turns > 0:
        myletter = input().lower().strip()

        if myletter in guessing:
            correct.add(myletter)
            print(myletter)

        else:
            print("-")
        

        if correct == guessing_set and turns > 0:
            print(words[number])
            break
        turns -= 1
    
    if turns == 0:
        print(words[number])
    
    print(correct)
    print(guessing_set)
    
hangman(int(input().strip()))
