import numpy as np
from NeuralNetwork import *
from ActivationFunctions import *
from SpiralData import *
from LossFunctions import *
import matplotlib.pyplot as plt

X,t = spiral_data(100,3)
plt.scatter(X[:,0],X[:,1],c=t)

nnfs = NeuralNetwork(lr = 0.01)
nnfs.add_input_layer(X, t)
nnfs.add_layer(n_inputs=2,n_neurons=3)
nnfs.add_activation_function("ReLU")
nnfs.add_layer(n_inputs=3,n_neurons=3)
nnfs.add_activation_function('Softmax')

nnfs.solve()
print('solution:' )
print(nnfs.solution)
print('custo final',nnfs.loss)
print('acurácia', nnfs.accuracy)

primeiro = nnfs.loss

nnfs.loss_function.calculate_gradient(nnfs.solution,t)
print('gradiente da função de custo:')
print(nnfs.loss_function.gradient)
print('inputs do layer 2:')
print(nnfs.network[1].inputs)
weight_gradients = np.dot(nnfs.network[1].inputs.T,nnfs.loss_function.gradient) 
print('o gradiente do pesos então é:')
print(weight_gradients)
print('e portanto os novos pesos são')
new_weights = nnfs.network[1].weights - nnfs.lerning_rate * weight_gradients
print(new_weights)
print('os antigos eram:')
print(nnfs.network[1].weights)

print('and now, lets try again')
nnfs.network[1].weights = new_weights
nnfs.solve()
print('solution:' )
print(nnfs.solution)
print('custo final',nnfs.loss)
print('acurácia', nnfs.accuracy)

segundo = nnfs.loss
print(primeiro - segundo)
print('if it is positive, it means that he learned!!!!!!')
plt.show()