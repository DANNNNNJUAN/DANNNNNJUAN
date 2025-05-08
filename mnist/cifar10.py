import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import Dataloader

cifar_train = datasets.CIFAR10('cifar', train = True, download = True, transform = transforms.Compose(
    transforms.Resize((32, 32)),
    transforms.RandomHorizontalFilp(),
    transforms.RandomRotation(15),
    transforms.RandomVerticalFilp(),
    transforms.ToTensor()
))
cifar_train, cifar_val = torch.utils.data.random_split(cifar_train, (0.8*len(cifar_train), 0.2*len(cifar_train)))

cifar_train = datasets.CIFAR10('cifar', train = False, download = True, transform = transforms.Compose(
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
))

cifar_train = Dataloader(cifar_train, shuffle=True)