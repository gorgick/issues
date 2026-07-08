import numpy as np

# weights = np.array([0.1, 0.2, 0])

d = np.zeros((2, 5))  # Матрица 2x5, заполненная нулями
w = np.random.rand(2, 4)  # Матрица 2x4, заполненная случайными числами от 0 до 1



# def neural_network(input, weight):
#     pred = input.dot(weight)
#     return pred


toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

# игр % побед болельщиков .T - меняет местами столбцы и строки
ih_wgt = np.array([[0.1, 0.2, -0.1],  # hid[0]
                   [-0.1, 0.1, 0.9],  # hid[1]
                   [0.1, 0.4, 0.1]]).T  # hid[2]

# hid[0] hid[1] hid[2]
hp_wgt = np.array([[0.3, 1.1, -0.3],  # травмы?
                   [0.1, 0.2, 0.0],  # победы?
                   [0.0, 1.3, 0.1]]).T  # печаль?

weights = [ih_wgt, hp_wgt]


def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred


input = np.array([toes[0], wlrec[0], nfans[0]])
pred = neural_network(input, weights)

print(weights[0])

print(pred)
