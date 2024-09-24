import unittest
from unittest.mock import patch
import sys
import os
# Agregar el directorio SRC al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from player import get_player_guess, welcome_player

# Tests
class TestPlayerFunctions(unittest.TestCase):

    ### welcome_player
    
    @patch('builtins.input', side_effect=["John"])
    def test_welcome_player_valid(self, mock_input):
        name = welcome_player()
        self.assertEqual(name, "John")
        print("\n✅ test_welcome_player_valid completado con éxito.")

    @patch('builtins.input', side_effect=["", "Alice"])
    def test_welcome_player_invalid_then_valid(self, mock_input):
        name = welcome_player()
        self.assertEqual(name, "Alice")
        print("\n✅ test_welcome_player_invalid_then_valid completado con éxito.")


    ### get_player_guess

    @patch('builtins.input', side_effect=["50"])
    def test_get_player_guess_valid(self, mock_input):
        guess = get_player_guess()
        self.assertEqual(guess, 50)
        print("\n✅ test_get_player_guess_valid completado con éxito.")


    @patch('builtins.input', side_effect=["200", "75",])
    def test_get_player_guess_out_of_range_then_valid(self, mock_input):
        guess = get_player_guess()
        self.assertEqual(guess, 75)
        print("\n✅ test_get_player_guess_out_of_range_then_valid completado con éxito.")


    @patch('builtins.input', side_effect=["abc","24.332323","50"])
    def test_get_player_guess_invalid_input_then_valid(self, mock_input):
        guess = get_player_guess()
        self.assertEqual(guess, 50)
        print("\n✅ test_get_player_guess_invalid_input_then_valid completado con éxito.")

if __name__ == '__main__':
    unittest.main()