"""
Eg2.3.0 : enumerate
"""
import torch
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST

train_dataset = MNIST(root="./mnist_data",
                      train=True,
                      transform=None,
                      target_transform=None,
                      download=False)

train_loader = DataLoader(dataset=train_dataset,
                          batch_size=10000,
                          shuffle=False)

for batch, (x, y) in enumerate(train_loader):
    print("batch: {}, type(x): {}, type(y): {}".format(batch, type(x), type(y)))
    # batch: 0, type(x): <class 'torch.Tensor'>, type(y): <class 'torch.Tensor'>
    print("batch: {}, x.shape: {}, y.shape: {}".format(batch, x.shape, y.shape))
    # batch: 0, x.shape: torch.Size([10000, 1, 28, 28]), y.shape: torch.Size([10000])
    break

"""
Eg2.3.1 : tqdm
"""
from torch.utils.data import DataLoader
from tqdm import tqdm

train_loader = DataLoader(dataset=train_dataset,
                          batch_size=10000,
                          shuffle=False)

with tqdm(train_loader, desc="TRAINING") as train_bar:
    for (x, y) in train_bar:
        pass

"""
Eg2.4 : collate_fn
"""


def collate_fn(batch):
    print("type(batch): {}, len(batch): {}".format(type(batch), len(batch)))  # <class 'list'>, 10000
    x = [i[0] for i in batch]
    y = [i[1] for i in batch]
    x = torch.cat(x)[:, None, ...]
    y = torch.Tensor(y)
    return {"x": x, "y": y}


# from torch.utils.data import DataLoader
# from tqdm import tqdm
train_loader = DataLoader(dataset=train_dataset,
                          batch_size=10000,
                          shuffle=False,
                          collate_fn=collate_fn)

for batch in train_loader:
    print("type(batch): {}".format(type(batch)))  # <class 'dict'>
    print("type(batch[\"x\"]): {}".format(type(batch["x"])))  # <class 'torch.Tensor'>
    print("type(batch[\"y\"]): {}".format(type(batch["y"])))  # <class 'torch.Tensor'>
    print("batch[\"x\"].shape: {}".format(batch["x"].shape))  # torch.Size([10000, 1, 28, 28])
    print("batch[\"y\"].shape: {}".format(batch["y"].shape))  # torch.Size([10000])
    break
