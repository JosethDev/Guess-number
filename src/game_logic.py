import random
from player import get_player_guess


def get_random_number():
    return random.randint(1, 100)

def play_round(name, aleatorio_number):
    print(f"\n--- Round {name} ---")
    player_chosen = get_player_guess()
    if player_chosen < aleatorio_number:
        print("Too low, try again.")
        return False
    elif player_chosen > aleatorio_number:
        print("Too high, choose a number one more time.")
        return False
    else:
        print(f"You win, {name}! 🥳")
        return True
                   