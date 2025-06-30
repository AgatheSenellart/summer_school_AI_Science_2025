import torch
import numpy as np

m0 = torch.load('./data/MMNIST/train/m0.pt')
m1 = torch.load('./data/MMNIST/train/m1.pt')
m2 = torch.load('./data/MMNIST/train/m2.pt')
m3 = torch.load('./data/MMNIST/train/m3.pt')
m4 = torch.load('./data/MMNIST/train/m4.pt')
labels = torch.load('./data/MMNIST/train/labels.pt')


indices = np.random.choice(len(m0),1000,replace=False)

torch.save(m0[indices], './data/MMNIST/train/m0_.pt')
torch.save(m1[indices], './data/MMNIST/train/m1_.pt')
torch.save(m2[indices], './data/MMNIST/train/m2_.pt')
torch.save(m3[indices], './data/MMNIST/train/m3_.pt')
torch.save(m4[indices], './data/MMNIST/train/m4_.pt')
torch.save(labels[indices], './data/MMNIST/train/labels.pt')





print(indices)

