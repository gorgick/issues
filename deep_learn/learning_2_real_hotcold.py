weight = 0.5
input_ = 0.5
goal_prediction = 0.8
step_amount = 0.001  # Шаг изменения в каждой итерации

for iteration in range(1101):
    prediction = input_ * weight
    error_ = (prediction - goal_prediction) ** 2

    print("Error: " + str(error_) + " Prediction " + str(prediction))

    up_prediction = input_ * (weight + step_amount)  # Увеличиваем
    up_error = (goal_prediction - up_prediction) ** 2

    down_prediction = input_ * (weight - step_amount)  # Уменьшаем
    down_error = (goal_prediction - down_prediction) ** 2

    if down_error < up_error:
        weight = weight - step_amount

    if up_error < down_error:
        weight = weight + step_amount

print(weight)  # Тот вес, который нужен для лучшего результата
