"""
Eg1.2.0 : MNIST
"""
from torchvision.datasets.mnist import MNIST
import matplotlib.pyplot as plt

train_dataset = MNIST(root="./mnist_data",
                      train=True,
                      transform=None,
                      download=False)
# first time you run this py, you can modify the parameter download to True,
# so that you can download those MNIST dataset, then set it False.

# this dataset in our project is an instance, dataset do not mean those files where saved lots of data.

print("type(train_dataset): {}".format(type(train_dataset)))  # <class 'torchvision.datasets.mnist.MNIST'>
index = 0
print("train_dataset[{}]: {}".format(index, train_dataset[index]))  # (PIL.Image.Image, 5)
print("len(train_dataset): {}".format(len(train_dataset)))

plt.imshow(train_dataset[index][0], cmap='gray')
plt.show()
