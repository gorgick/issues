knob_weight = 0.5
input = 0.5
goal_pred = 0.8  # Значение которое мы хотели бы видеть

pred = input * knob_weight
error = (pred - goal_pred) ** 2  # Среднеквадратичная ошибка
print(error)

"""Метод холодно/горячо, способ уменьшения вероятности ошибки"""

weight = 0.1


def neural_network(input, weight):
    prediction = input * weight
    return prediction


number_of_toes = [8.5]
win_or_lose_binary = [1]  # Победа

input = number_of_toes[0]
true = win_or_lose_binary[0]
pred = neural_network(input, weight)
error = (pred - true) ** 2
print("error - ", error)

lr = 0.1
p_up = neural_network(input, weight) + lr  # Приращение
e_up = (p_up - true) ** 2
print("e_up - ", e_up)

lr = 0.01
p_dn = neural_network(input, weight) - lr  # Уменьшение
e_dn = (p_dn - true) ** 2
print("e_dn - ", e_dn)

print("weight", weight)

if (error > e_dn or error > e_up):
    if (e_dn < e_up):
        weight -= lr
    if (e_up < e_dn):
        weight += lr

print("weight", weight)
