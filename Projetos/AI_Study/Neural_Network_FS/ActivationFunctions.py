import numpy as np

class ActivationFunctions():
    def ReLU(self, inputs):
        self.output = np.maximum(0, inputs)

    def Softmax(self, inputs):
        intermediate_value = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        self.output = intermediate_value/np.sum(intermediate_value, axis=1, keepdims=True)
