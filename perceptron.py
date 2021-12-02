# Dataset para teste
dataset = [
    [0,0,1,1],
    [1,0,1,1],
    [1,1,1,0],
    [0,0,0,1],
    [0,1,1,1],
    [1,0,1,1],
    [1,1,0,0]]

# pesos iniciais, com bias sendo w[0]
weights = [0, 0, 0, 0]

# funcão de predição do perceptron
def predict(row, weights):
    bias = weights[0]
    print(len(row))
    for i in range(len(row) - 1):
        activation = weights[i + 1] * row[i] + bias

    if activation >= 1:
        return 1.0
    else:
        return 0.0

for row in dataset:
    prediction = predict(row, weights)
    print("Expected: " + str({row[-1]}) + "Predicted: " + str({prediction}))

# função para treinar os pesos
def train_weights(train, l_rate, n_epoch):
	weights = [0.0 for i in range(len(train[0]))]
	for epoch in range(n_epoch):
		sum_error = 0.0
		for row in train:
			prediction = predict(row, weights)
			error = row[-1] - prediction
			sum_error += error**2
			weights[0] = weights[0] + l_rate * error
			for i in range(len(row)-1):
				weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
		print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
	return weights

# exemplo de treinamento
# taxa de aprendizado
l_rate = 0.1
# numero de epocas (vezes para rodar os dados de treinamento enquanto atualiza os pesos
n_epoch = 10
# chamada da função treinar pesos
weights = train_weights(dataset, l_rate, n_epoch)
print(weights)
