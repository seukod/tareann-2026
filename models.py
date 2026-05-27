import torch
import torch.nn as nn
#Arquitecutra 1
class MultiLayerPerceptronSig(nn.Module):

    def __init__(self, input_dim, hidden_dim, output_dim): 
        super(type(self), self).__init__()  
        self.hidden = nn.Linear(input_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, output_dim)        
        self.activation = nn.Sigmoid()
        
    def forward(self, x):
        x = self.activation(self.hidden(x))
        return self.output(x)

#Arquitectura 2
class MultiLayerPerceptron2Cap(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim): 
        super().__init__()  
        self.hidden1 = nn.Linear(input_dim, hidden_dim)
        # Una segunda capa oculta que mantiene la misma dimensión
        self.hidden2 = nn.Linear(hidden_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, output_dim)        
        self.activation = nn.Sigmoid() # Puedes usar ReLU o Sigmoide aquí
        
    def forward(self, x):
        x = self.activation(self.hidden1(x))
        x = self.activation(self.hidden2(x))
        return self.output(x)
    
    #Arquitectura 3
class MultiLayerPerceptronRelu(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, dropout_p): 
        super(type(self), self).__init__()  
        self.hidden = nn.Linear(input_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, output_dim)        
        self.activation = nn.ReLU()
        self.dropout = nn.Dropout(p=dropout_p)  

    def forward(self, x):
        x = self.activation(self.hidden(x))
        x = self.dropout(x)  
        return self.output(x)