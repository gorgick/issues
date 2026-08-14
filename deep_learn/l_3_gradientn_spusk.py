"""ГРАДИЕНТНЫЙ СПУСК"""

weight = 0.5
input_ = 0.5
goal_pred = 0.8

for i in range(20):
    pred = input_ * weight
    error_ = (pred - goal_pred) ** 2
    direction_and_amount = (pred - goal_pred) * input_
    weight = weight - direction_and_amount
    print("Error: " + str(error_) + " Prediction " + str(pred))

# (pred - goal_pred) - Чистая ошибка. Определит направление и величину промаха
# (Если + - то прогноз велик, и наоборот. Если число большое - сильный промах)

# Умножая (pred - goal_pred) на input_ - Остановка.
# Если инпут равен нулю то мы стоим, от величины и знака инпута зависит куда пойдет смещение

