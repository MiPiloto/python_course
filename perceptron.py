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

# funcão de ativação do perceptron
def predict(row, weights):
    bias = weights[0]
    for i in range(len(row) - 1):
        activation = weights[i + 1] * row[i] + bias

    if activation >= 1:
        return 1.0
    else:
        return 0.0

for row in dataset:
    prediction = predict(row, weights)
    print("Esperado: " + str({row[-1]}) + "Predição: " + str({prediction}))

# Resultado: a IA erra 5 dos 7 resultados
    
# Esperado: {1}Predição: {0.0}
# Esperado: {1}Predição: {0.0}
# Esperado: {0}Predição: {0.0}
# Esperado: {1}Predição: {0.0}
# Esperado: {1}Predição: {0.0}
# Esperado: {1}Predição: {0.0}
# Esperado: {0}Predição: {0.0}

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


# após rodar as funções com 10 épocas, os pesos corrigidos foram:
# [0.9999999999999999, -0.7999999999999999, -0.4, 0.10000000000000003]

# rodando novamente com os novos pesos

new_weights = [0.9999999999999999, -0.7999999999999999, -0.4, 0.10000000000000003]

for row in dataset:
    prediction = predict(row, new_weights)
    print("Esperado: " + str({row[-1]}) + "Predição: " + str({prediction}))

# Mesmo com os pesos corrigidos a predição ainda não acerta todas, mas melhora os resultados, errando apenas duas vezes
    
# Esperado: {1}Predição: {1.0}
# Esperado: {1}Predição: {1.0}
# Esperado: {0}Predição: {1.0}
# Esperado: {1}Predição: {0.0}
# Esperado: {1}Predição: {1.0}
# Esperado: {1}Predição: {1.0}
# Esperado: {0}Predição: {0.0}
