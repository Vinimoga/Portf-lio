import numpy as np
from NeuralNetwork import *
from ActivationFunctions import *
from SpiralData import *
from LossFunctions import *

X,t = spiral_data(100,3)

first_layer = NetworkLayer(2,3)
second_layer = NetworkLayer(3,3)

activation = ActivationFunctions()

first_layer.forward(X)
activation.ReLU(first_layer.output)


second_layer.forward(activation.output)
activation.Softmax(second_layer.output)

loss = CategoricalCrossEntropy_Loss()

mean_loss = loss.calculate(activation.output, t)

print('output:',activation.output[:5])
print('loss:', mean_loss)

print('accuracy:', loss.calculate_accuracy(activation.output,t))