"""
Eg1.2.1 : transforms
"""
from torchvision.datasets.mnist import MNIST
from torchvision import transforms

transform = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Normalize(mean=(0.5,), std=(0.5,))
    ]
)
# In fact, the dataset that we gonna handle is the type of tensor rather than image.
# so this is the reason why transforms exists.
train_dataset = MNIST(root="./mnist_data",
                      train=True,
                      transform=transform,
                      target_transform=None,
                      download=False)

index = 0
print("type(train_dataset[{}]): {}".format(index, type(train_dataset[index])))  # <class 'tuple'>
print("type(train_dataset[{}][0]): {}".format(index, type(train_dataset[index][0])))  # <class 'torch.Tensor'>
print("train_dataset[{}][0].shape: {}".format(index, train_dataset[index][0].shape))  # torch.Size([1, 28, 28])
print("type(train_dataset[{}][1]): {}".format(index, type(train_dataset[index][1])))  # <class 'int'>