import numpy as np
from NeuralNetwork import *
from ActivationFunctions import *
from SpiralData import *
from LossFunctions import *
import matplotlib.pyplot as plt

X,t = spiral_data(5,3)

#plt.scatter(X[:,0],X[:,1],c=t)

#New code starts here

nnfs = NeuralNetwork()
print('current network:', nnfs.network)

nnfs.add_input_layer(X)
print('inputs:')
print(nnfs.inputs)

nnfs.add_layer(n_inputs=2,n_neurons=3)
#nnfs.add_layer(n_inputs=3,n_neurons=3)
print('current network:', nnfs.network)

nnfs.add_activation_function("ReLU")

nnfs.solve()

print(nnfs.solution)
      




'''
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
'''

#plt.show()