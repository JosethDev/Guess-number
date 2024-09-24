import unittest
from unittest.mock import patch
import sys
import os
import numpy as np
from sklearn.linear_model import LinearRegression
# Agregar el directorio SRC al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from pc import train_model, predict_next_guess, play_pc_round_ml  # Cambia 'your_module' por el nombre de tu archivo

class TestGameFunctions(unittest.TestCase):

    def test_train_model(self):
        X_train = [1, 2, 3, 4, 5]
        y_train = [2, 3, 4, 5, 6]
        model = train_model(X_train, y_train)

        # Comprobamos que el modelo se entrene correctamente
        self.assertIsInstance(model, LinearRegression)

    def test_predict_next_guess(self):
        X_train = [1, 2, 3, 4, 5]
        y_train = [2, 3, 4, 5, 6]
        model = train_model(X_train, y_train)

        next_guess = predict_next_guess(model, 3)
        # Esperamos que la predicción para 3 sea aproximadamente 4
        self.assertEqual(next_guess, 4)


    @patch('pc.predict_next_guess')
    def test_play_pc_round_ml_win(self,mock_predict):
        mock_predict.return_value = 50  # Simulamos que el modelo predice 50
        result, low, high, pc_chosen = play_pc_round_ml(LinearRegression, 50, [10, 20, 30], 1, 100)
        # Comprobamos que el PC ganó
        self.assertTrue(result)
        self.assertEqual(low, 1)  # Rango no cambia si gana
        self.assertEqual(high, 100)


if __name__ == '__main__':
    unittest.main()
