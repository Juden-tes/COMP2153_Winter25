import random
def number_guessing_game():
    targetNumber = random.randint(1, 100)

    play = input("Do you want to play number guessing game? (yes/no)").strip().lower()

    attemps = 0
    max_attemps = 10

    while attemps < max_attemps:
        try:
            return True
        except:
            print("")
    play = input()
    return True