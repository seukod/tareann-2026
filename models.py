import torch
import torch.nn as nn

class MultiLayerPerceptron(nn.Module):

    def __init__(self, input_dim, hidden_dim, output_dim): 
        super(type(self), self).__init__()  
        self.hidden = nn.Linear(input_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, output_dim)        
        self.activation = nn.Sigmoid()
        
    def forward(self, x):
        x = self.activation(self.hidden(x))
        return self.output(x)