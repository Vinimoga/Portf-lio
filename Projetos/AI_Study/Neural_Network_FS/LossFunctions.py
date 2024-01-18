import numpy as np

class Loss():
    def calculate(self, output, intended_target_value):
        sample_losses = self.forward(output, intended_target_value)
        data_loss = np.mean(sample_losses)
        return data_loss



class CategoricalCrossEntropy_Loss(Loss):
    def forward(self, y_prediction, y_true):
        samples = len(y_prediction)
        y_prediction_clipped = np.clip(y_prediction,1e-7,1-1e-7) #infinity error purpose
        
        #chosing the way we will read the category
        if len(y_true.shape) == 1:
            #have passed scalar class values
            self.probabilitys = y_prediction_clipped[range(samples), y_true]
        
        elif len(y_true.shape) == 2:
            #have passed classes entire prediction
            self.probabilitys = np.sum(y_prediction_clipped * y_true, axis= 1)

        return -np.log(self.probabilitys)
    
    def calculate_accuracy(self, softmax_output,intended_target_value):
        target_value = np.array(intended_target_value)

        #chosing the way we will read the category
        if len(target_value.shape) == 1:
            predictions = np.argmax(softmax_output, axis= 1)
            self.accuracy = np.mean(predictions == target_value) 
        
        elif len(target_value.shape) == 2:
            class_target = np.argmax(target_value, axis=1)
            predictions = np.argmax(softmax_output, axis= 1)
            self.accuracy = np.mean(predictions == class_target) 

        return self.accuracy
    
    def calculate_gradient(self, softmax_output, intended_target_value):
        # Determine the size of the matrix
        matrix_size = np.max(intended_target_value) + 1

        # Create the matrix
        result = np.zeros((len(intended_target_value), matrix_size))

        # Set the positions indicated by the vector to 1
        result[np.arange(len(intended_target_value)), intended_target_value] = 1

        self.gradient = softmax_output - result

