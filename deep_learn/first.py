def w_sum(a, b):
    assert (len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output


def neural_network(input, weight):
    prediction = w_sum(input, weight)
    return prediction



