knob_weight = 0.5
input = 0.5
goal_pred = 0.8  # Значение которое мы хотели бы видеть

pred = input * knob_weight
error = (pred - goal_pred) ** 2  # Среднеквадратичная ошибка
print(error)
