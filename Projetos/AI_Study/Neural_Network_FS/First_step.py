import numpy as np

samples = 3
y_prediction_clipped = np.array([[0.7, 0.1, 0.2],
                                [0.1, 0.5, 0.4],
                                [0.02, 0.9, 0.08]])

y_true_position_value = np.array([[1, 0, 0],
                                  [0, 1, 0],
                                  [0, 1, 0]])


x = np.array(y_true_position_value)

'''
[blue,yellow,purple]
'''

if len(y_true_position_value.shape) == 2:
        class_target = np.argmax(y_true_position_value, axis= 1)
        print(class_target)