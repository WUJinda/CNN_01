from torchvision import transforms
from torchvision.datasets.mnist import MNIST
from torch.utils.data import DataLoader

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

"""
Eg2.1 : __iter__
"""


train_loader = DataLoader(dataset=train_dataset,
                          batch_size=10000,
                          shuffle=False)

print("type(train_loader): {}".format(type(train_loader)))  # <class 'torch.utils.data.dataloader.DataLoader'>
for batch in train_loader:
    print("type(batch): {}".format(type(batch)))  # <class 'list'>
    print("len(batch): {}".format(len(batch)))  # 2
    print("type(batch[0]): {}".format(type(batch[0])))  # <class 'torch.Tensor'>
    print("type(batch[1]): {}".format(type(batch[0])))  # <class 'torch.Tensor'>
    print("batch[0].shape: {}".format(batch[0].shape))  # torch.Size([10000, 1, 28, 28])
    print("batch[1].shape: {}".format(batch[1].shape))  # torch.Size([10000])
    break

"""
Eg2.2 : __len__
"""
print("len(train_loader): {}".format(len(train_loader)))  # 6
print("len(train_loader.dataset): {}".format(len(train_loader.dataset)))  # 60000
