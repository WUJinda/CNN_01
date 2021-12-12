"""
 Eg3.0.0 : torch.nn.Module
 """
from torch import nn


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()  # Annotate it will give an error.
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=(1, 1))
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        return x

if __name__ == '__main__':

    model = SimpleModel()
    print("model: {}".format(model))
    for name, param in model.named_parameters():
        print(name, param)