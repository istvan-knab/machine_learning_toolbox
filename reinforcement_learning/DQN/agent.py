from torch import nn
import torch.nn.functional as F

class DQNAgent(nn.Module):
    def __init__(self,input_layer: int, hidden_layers: list, output_layer: int):
        super(DQNAgent, self).__init__()
        layers = [input_layer]
        for i in range (len(hidden_layers)):
            layers.append(hidden_layers[i])
        layers.append(output_layer)
        self.linear1 = nn.Linear(layers[0], layers[1])
        self.linear2 = nn.Linear(layers[1], layers[2])
        self.linear3 = nn.Linear(layers[2], layers[3])

    def forward(self, x):
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        return self.linear3(x)




