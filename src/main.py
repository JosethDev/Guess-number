#importacion de la funciones
from player import get_player_guess, welcome_player
from pc import play_pc_round_ml, train_model
from game_logic import get_random_number

def play_game():
    #variables
    name = welcome_player() #bienvenida al juego 
    aleatorio_number = get_random_number() #numero secreto aleatorio
    low, high = 1, 100 # Rango inicial para la búsqueda
    attempts = [] #Intentos de la pc
    responses = [] # Diferencia entre los intentos y el número aleatorio
    player_attempts = []  # registro los intentos del usuario
    pc_attempts = []  # registro los intentos de la PC

    while True:
        # Turno del jugador
        print(f"\n--- {name}'s Round 🎮 ---")
        player_attempt = get_player_guess() #Obtiene el intento del jugador 
        player_attempts.append(player_attempt) #registra los intentos

        # Agregar respuesta correspondiente al intento del jugador
        responses.append(aleatorio_number - player_attempt) 

        #verifica si el jugador acertó
        if player_attempt == aleatorio_number:
            print(f"Congratulations {name}! You guessed the correct number 🎉.")
            print(f"Your guesses: {player_attempts}") #muestra los intentos del jugador
            break
        elif player_attempt < aleatorio_number:
            print(f"Too low, {name}! Try again.")
            low = max(player_attempt + 1, low)
        else:
            print(f"Too high, {name}! Try again.")
            high = min(player_attempt - 1, high)

        # Intento de la PC
        if len(attempts) > 1:
            #combina los intentos del jugador y de la computadora.
            combined_attempts = attempts + player_attempts        
            # Asegurarse de que las listas tengan la misma longitud
            if len(combined_attempts) == len(responses):
                model = train_model(combined_attempts, responses)
                pc_wins, low, high, attempt = play_pc_round_ml(model, aleatorio_number, attempts, low, high)
            else:
                print("Error: Inconsistent number of attempts and responses!")
                break  # Salir del juego si hay un error de consistencia
        else:
            pc_wins, low, high, attempt = play_pc_round_ml(None, aleatorio_number, attempts, low, high)

        # Agregar el intento de la PC y su respuesta correspondiente
        attempts.append(attempt)
        responses.append(aleatorio_number - attempt)
        pc_attempts.append(attempt)

        if pc_wins:
            print("The PC wins! Better luck next time! 🤖")
            print(f"PC's guesses: {pc_attempts}")
            break

# Opción para jugar de nuevo
def play_again():
    while True:
        play_game()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_again()
