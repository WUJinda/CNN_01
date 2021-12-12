import os
import torch

from torch.utils.data import Dataset
from torch.utils.data import Sampler


class SimpleDataset(Dataset):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __getitem__(self, index):
        return {"x": self.x[index], "y": self.y[index]}

    def __len__(self):
        return len(self.x)


if __name__ == '__main__':
    """
      Eg1.1 : __getitem__, __len__
    """
    x = torch.linspace(-1, 1, 10)
    y = x ** 2

    simpledataset = SimpleDataset(x, y)
    index = 0
    # __getitem__
    print("simpledataset.__getitem__({}): {}".format(index, simpledataset.__getitem__(index)))
    print("simpledataset[{}]: {}".format(index, simpledataset[index]))
    # __len__
    print("simpledataset.__len__(): {}".format(simpledataset.__len__()))
    print("len(simpledataset): {}".format(len(simpledataset)))
