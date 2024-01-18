import numpy as np
from ActivationFunctions import *
from LossFunctions import *

class NeuralNetwork:

    def __init__(self, lr = 0.01):
        self.network = []
        self.layers = 0
        self.activation_function_list = []
        self.usable_func_list = ["Softmax", "ReLU"] 
        self.lerning_rate = lr

        
        self.activation_function = ActivationFunctions()
        self.loss_function = CategoricalCrossEntropy_Loss()

    def add_input_layer(self, inputs, correct_category):
        self.inputs = inputs
        self.category = correct_category

    def add_layer(self, n_inputs, n_neurons):
        Layer = NetworkLayer(n_inputs, n_neurons)
        self.network.append(Layer)
        self.activation_function_list.append('')
        self.layers += 1
        
    def solve(self):
        data = self.inputs
        for i in range(len(self.network)):
            #print(i)
            self.network[i].forward(data)
            data = self.network[i].output
            #print('workeddata:',data)
            self.use_activation_function(func_name=self.activation_function_list[i], inputs= data)
            data = self.activation_function.output
        self.solution = data
        self.find_loss(data, self.category)
        self.find_accuracy(data, self.category)

    def load(self, layer, weights, biases):
        self.network[layer].load_weights(weights)
        self.network[layer].load_biases(biases)

    def save(self, path):
        pass

    def use_activation_function(self, func_name, inputs):
        method = getattr(self.activation_function, func_name, None)
        return method(inputs)
    
    def add_activation_function(self, func_name,layer = 0):
        if func_name not in self.usable_func_list:
            raise Exception('Invalid activation function name')
        else:
            self.activation_function_list[layer - 1] = func_name
        
    def find_loss(self, softmax_output, intended_target_value):
        self.loss = self.loss_function.calculate(softmax_output, intended_target_value)
    
    def find_accuracy(self, softmax_output, intended_target_value):
        self.accuracy = self.loss_function.calculate_accuracy(softmax_output,intended_target_value)

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
        self.inputs = inputs
        self.output = np.dot(inputs, self.weights) + self.biases
    
    
    def load_weights(self, weights):
        pass

    def load_biases(self, biases):
        pass

    def __repr__(self):
        return f"Layer with {self.weights.shape[0]} inputs and {self.weights.shape[1]} neurons"