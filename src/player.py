def welcome_player():
    print("Guess number game 🤯 \nWhat's your name?")
    while True:
        name = input()
        if name.strip():  # se asegura de que no esté vacío
            print(f"\nWelcome {name} 🤗\nGuess the secret number, this number is between 1 to 100")
            return name
        else:
            print("Please enter a valid name to start the game.")


def get_player_guess():
    while True:
        try:
            player_chosen = int(input("Choose a number: "))
            if 1 <= player_chosen <= 100:
                return player_chosen
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer number.")
