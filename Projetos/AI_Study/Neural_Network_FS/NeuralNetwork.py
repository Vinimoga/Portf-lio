import numpy as np
from ActivationFunctions import *

class NeuralNetwork:

    def __init__(self):
        self.network = []
        self.layers = 0
        self.activation_function_list = []
        self.activation_function = ActivationFunctions()
        self.func_list = ["softmax", "relu"] 

    def add_input_layer(self, inputs):
        self.inputs = inputs

    def add_layer(self, n_inputs, n_neurons):
        Layer = NetworkLayer(n_inputs, n_neurons)
        self.network.append(Layer)
        self.activation_function_list.append('')
        self.layers += 1
        
    def solve(self, inputs):
        for i in len(self.network):
            inputs = self.network[i].forward(inputs)

    def load(self, layer, weights, biases):
        self.network[layer].load_weights(weights)
        self.network[layer].load_biases(biases)

    def save(self, path):
        pass

    def add_activation_function(self, func_name, layer = 0):
        if layer < 0 or layer > len(self.network):
            raise Exception("layer doesn't exist") 

        if func_name.lower() not in self.func_list:
            raise Exception("function doesn't exist") 
        
        self.activation_function_list[layer - 1] =  func_name

    def solve(self, inputs):
        pass

    def __repr__(self):
        return f'Neural_Network with {self.layers} layers'



class NetworkLayer():
    '''
    In the init function we need to create a set o weights and a set of biases, for the weights we know 
    (because of the dot product) that it need to be number imput (or else it doesn't match) by the number 
    of neurons in the layer, and for the biases it need to be 1 by the number of imputs (each imput with
    one bias).
    '''
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    '''
    for the forward method we need simply to do the calculations and give the result in a way that can be 
    used somewhere else in the code for new layers to use, so we simple give a variable name or we return
    it.
    '''
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases
    
    
    def load_weights(self, weights):
        pass

    def load_biases(self, biases):
        pass

    def __repr__(self):
        return f"Layer with {self.weights.shape[0]} inputs and {self.weights.shape[1]} neurons"

        
        
       