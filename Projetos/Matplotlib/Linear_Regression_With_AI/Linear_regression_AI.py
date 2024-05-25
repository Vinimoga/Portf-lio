import torch
from torch import nn # nn contains all of PyTorch's building blocks for neural networks
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pathlib import Path

Weight = 0.7
Bias = 0.3

X = torch.arange(0,1,0.02).unsqueeze(dim=1)  #Defining the features
Y = X*Weight + Bias                          #Defining the label

ratio = 0.8    #Defining the division of the dataset
split = int(ratio * len(X))

X_train, X_test = X[:split],X[split:]
Y_train, Y_test = Y[:split],Y[split:]

class LinearRegressionModel(nn.Module):
  def __init__(self):
    super().__init__()
    self.weights = nn.Parameter(torch.randn(1, dtype=torch.float32, requires_grad=True))

    self.bias = nn.Parameter(torch.randn(1, dtype=torch.float32, requires_grad=True))

  def forward(self, x: torch.Tensor) -> torch.Tensor :
    return x*self.weights + self.bias
  
fig, ax = plt.subplots()#initializin plot

torch.manual_seed(42)
Model_1 = LinearRegressionModel()
loss_Func1 = nn.L1Loss()
optmizer1 = torch.optim.SGD(params=Model_1.parameters(),lr=0.01)
print(Model_1.state_dict())

def update_plot(i):
  #Training Loop
  Model_1.train() #Puts the model in training Mode
  Y_pred = Model_1(X_train) #Do the forward pass
  loss = loss_Func1(Y_train,Y_pred) #Calculate the loss
  optmizer1.zero_grad() #reestart (disable accumulation)
  loss.backward() #Do backpropagation
  optmizer1.step() #Do a step forward to glory
  print(f'epoch:{i}; Dict:{Model_1.state_dict()}')

  #Testing Loop
  Model_1.eval() #Puts the model in testing Mode
  with torch.inference_mode():
    test_pred = Model_1(X_test)
    ax.scatter(X_test,test_pred,c='m',s=2)

def init_f():
    ax.set(xlabel='X', ylabel='Y', title='About as simple as it gets, folks')
    ax.clear()

    with torch.inference_mode():
      Y_pred = Model_1(X_test)

    ax.scatter(X_test,Y_pred,c='green',s=2)
    ax.scatter(X_test,Y_test,c='red',s=2)
    ax.scatter(X_train,Y_train,c='blue',s=2)

anim = FuncAnimation(fig=fig,
                     func=update_plot,
                     frames=torch.arange(0, 150),
                     init_func = init_f,
                     interval=100)

print(Model_1.state_dict())
anim.save('Projetos/Matplotlib/Linear_Regression_With_AI/Linear_Regression.mp4',
          dpi=150,
          fps=5,
          writer='ffmpeg')
#Creating a directory
Model_dir = Path("Linear_regression_template")
Model_dir.mkdir(parents=True, exist_ok=True)

#Model path
Model_name = "Model_1.pth"
Model_Save_path = Model_dir / Model_name

#saving
print(f'saving model `{Model_1.state_dict()} in path {Model_Save_path}')
torch.save(obj=Model_1.state_dict(),f=Model_Save_path)

