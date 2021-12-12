"""
Eg3.2 : (B, C, H ,W)
"""
from torch import nn


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=(1, 1))
        self.conv2 = nn.Conv2d(in_channels=3, out_channels=5, kernel_size=(1, 1))
        self.relu = nn.ReLU(inplace=True)
        self.flatten = nn.Flatten(start_dim=1, end_dim=-1)
        self.linear = nn.Linear(in_features=5 * 28 * 28, out_features=10, bias=False)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.relu(x)
        print("[before flatten] x.shape: {}".format(x.shape))  # torch.Size([1, 5, 28, 28])
        x = self.flatten(x)
        print("[after flatten] x.shape: {}".format(x.shape))  # torch.Size([1, 3920])
        x = self.linear(x)
        x = self.relu(x)
        return x

if __name__ == '__main__':
    from torch.utils.data import Dataset, DataLoader, dataset
    from torchvision import models, transforms
    from torchvision.datasets.mnist import MNIST

    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Normalize(mean=(0.5,), std=(0.5,))
        ]
    )

    train_dataset = MNIST(root="../mnist_data",
                          train=True,
                          transform=transform,
                          target_transform=None,
                          download=False)
    train_loader = DataLoader(dataset=train_dataset,
                              batch_size=10000,
                              shuffle=True)
    model = SimpleModel()
    x = train_dataset[0][0]  # torch.Size([1, 28, 28])
    x = x[None, ...]  # torch.Size([1, 1, 28, 28])
    model(x)