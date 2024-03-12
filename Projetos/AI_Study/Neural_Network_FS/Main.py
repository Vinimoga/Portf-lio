import numpy as np
from NeuralNetwork import *
from ActivationFunctions import *
from SpiralData import *
from LossFunctions import *
import matplotlib.pyplot as plt

X,t = spiral_data(1000,3)
plt.scatter(X[:,0],X[:,1],c=t)

nnfs = NeuralNetwork(lr = 0.01)
nnfs.add_input_layer(X, t)
nnfs.add_layer(n_inputs=2,n_neurons=3)
nnfs.add_activation_function("ReLU")
nnfs.add_layer(n_inputs=3,n_neurons=3)
nnfs.add_activation_function('Softmax')
nnfs.solve()
print(nnfs.solution)
'''
first = nnfs.loss
learn = nnfs.loss
for i in range(10):
    nnfs.solve()
    print(f'custo {i}', nnfs.loss)
    print('diferença',learn - nnfs.loss)
    learn = nnfs.loss
    nnfs.learn(2, t)
    print()

print('diferença total:', first - nnfs.loss)
#plt.show()
'''