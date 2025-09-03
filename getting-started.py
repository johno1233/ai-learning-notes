import torch
import numpy as np

# Initializing a tensor
data = [[1, 2], [3, 4]]

# Direct creation
x_data = torch.tensor(data)

# Created by numpy arrays - works both ways numpy -> tensor -> numpy
np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# From another trensor
x_ones = torch.ones_like(x_data)
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")


