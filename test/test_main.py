import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Inserta la carpeta src en el sys.path antes de las importaciones
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Importaciones de los módulos
from game_logic import get_random_number
from player import get_player_guess
from pc import play_pc_round_ml, train_model
from main import play_game,play_again

class TestGame(unittest.TestCase):

    
    @patch('main.welcome_player', return_value="Test Player")  # Simula la entrada de nombre
    @patch('main.get_random_number', return_value=50)  # Simula el número aleatorio
    @patch('main.get_player_guess', side_effect=[50])  # Simula la adivinanza del jugador
    def test_play_game_wins(self, mock_get_player_guess, mock_get_random_number, mock_welcome_player):
        with patch('builtins.print') as mocked_print:
            play_game()  # Llama a la función
            mocked_print.assert_any_call("Congratulations Test Player! You guessed the correct number 🎉.")


    @patch('main.welcome_player', return_value="Test Player")  # Simula la entrada de nombre
    @patch('main.get_random_number', return_value=70)  # Simula el número aleatorio que la PC debe adivinar
    @patch('main.get_player_guess', side_effect=[30, 80, 60, 80])  # Simula los intentos del jugador
    @patch('main.play_pc_round_ml', return_value=(True, 1, 100, 70))  # Simula que la PC gana
    def test_play_game_pc_wins(self, mock_play_pc_round_ml, mock_get_player_guess, mock_get_random_number, mock_welcome_player):
        with patch('builtins.print') as mocked_print:
            play_game()  # Llama a la función
            mocked_print.assert_any_call("The PC wins! Better luck next time! 🤖")


if __name__ == '__main__':
    print("Running tests...")
    unittest.main()
