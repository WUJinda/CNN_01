"""
 Eg3.1 : __call__  [magic methods]
 """
from torch import nn


class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=(1, 1))
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.conv1(x)
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
    print(model(x) == model.forward(x))  # call like fonction