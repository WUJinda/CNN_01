"""
 Eg1.4.0 : ImageFolder
 """
import os

from torchvision.datasets import ImageFolder
from torchvision import transforms

transform = transforms.Compose(
    [
        transforms.RandomResizedCrop(size=(224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
    ]
)
train_dataset = ImageFolder(root=os.path.join("./flower_data", "train"), transform=transform)

index = 0
print("type(train_dataset[{}]): {}".format(index, type(train_dataset[index])))  # <class 'tuple'>
print("type(train_dataset[{}][0]): {}".format(index, type(train_dataset[index][0])))  # <class 'torch.Tensor'>
print("train_dataset[{}][0].shape: {}".format(index, train_dataset[index][0].shape))  # torch.Size([3, 224, 224])
print("type(train_dataset[{}][1]): {}".format(index, type(train_dataset[index][1])))  # <class 'int'>

"""
Eg1.4.1 : classes, class_to_idx
"""

print("train_dataset.classes: {}".format(
    train_dataset.classes))  # ['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
print("train_dataset.class_to_idx: {}".format(
    train_dataset.class_to_idx))  # {'daisy': 0, 'dandelion': 1, 'roses': 2, 'sunflowers': 3, 'tulips': 4}
