import numpy as np

X = np.array([1,2,3])
weights = np.array([0.1,-0.5, 0.9])
bias = np.array([0,0,0])
print(weights.T)
output = np.dot(X,weights.T)
print(output)



'''
class Layer():
    def __init__(self,):
        self.weights = np.random.randint()

    def forward(self, X):
        
'''