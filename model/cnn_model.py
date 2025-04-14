import torch.nn as nn

class TorchCNNModel(nn.Module):
    def __init__(self, input_size):
        super(TorchCNNModel, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=(3, 1)),
            nn.ReLU(),
            nn.Flatten()
        )
        self.fc = nn.Sequential(
            nn.Linear((input_size - 2) * 16, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        x = self.conv(x)
        return self.fc(x)
