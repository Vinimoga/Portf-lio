import numpy as np


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
       