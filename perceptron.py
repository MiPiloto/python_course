dataset = [
    [1,1,0,1],
    [1,0,1,0],
    [0,0,0,1],
    [1,0,0,1]]

weights = [0, 0, 0, 0]

# perceptron prediction
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

# function to training weights
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

# example of training weights
# learning rate, arbitrary value
l_rate = 0.1
# number of epochs(number of times to run through the training data while updating the weight)
n_epoch = 5
# calling train weights
weights = train_weights(dataset, l_rate, n_epoch)
print(weights)
