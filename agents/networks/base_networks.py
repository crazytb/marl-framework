# agents/networks/base_network.py
import torch.nn as nn

class BaseNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
    def forward(self, x):
        raise NotImplementedError