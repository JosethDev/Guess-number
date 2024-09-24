import numpy as np
from sklearn.linear_model import LinearRegression

def train_model(X_train, y_train):
    # X_train -> array de intentos
    # y_train -> array de [numero aleatorio - intento]
    X_train = np.array(X_train).reshape(-1, 1)  # Asegúrate de que sea un arreglo 2D (filas y columnas)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_next_guess(model, attempt):
    return int(model.predict(np.array([[attempt]])))

def play_pc_round_ml(model, aleatorio_number, attempts, low, high):
    print("\n--- Round PC 😏 ---")

    # Validar que 'low' y 'high' estén dentro del rango permitido
    low = max(low, 1)  # 'low' no puede ser menor que 1
    high = min(high, 100)  # 'high' no puede ser mayor que 100
    # Asegurar que 'low' siempre sea menor que 'high'
    if low >= high:
        pc_chosen = low  # Si el rango es inválido, la PC elige 'low' directamente
    else:
        if model is None or len(attempts) == 0:
            pc_chosen = np.random.randint(low, high + 1)  # Genera un número aleatorio dentro del rango válido
        else:
            pc_chosen = predict_next_guess(model, attempts[-1])  # Usar el modelo para predecir

    print(f"PC chooses: {pc_chosen}")

    if pc_chosen < aleatorio_number:
        print("Too low 🙁, the PC will choose again.")
        low = max(pc_chosen + 1, 1)  #Se asegura  de que 'low' no sea menor que 1
        return False, low, high, pc_chosen
    elif pc_chosen > aleatorio_number:
        print("Too high 😨, the PC will choose again.")
        high = min(pc_chosen - 1, 100)  # Se asegura de que 'high' no sea mayor que 100
        return False, low, high, pc_chosen
    else:
        print("The PC wins! Better luck next time! 🤖")
        return True, low, high, pc_chosen
