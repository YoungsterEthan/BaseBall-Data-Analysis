import numpy as np
import random 
from scipy.signal import convolve2d

# matrices with 2 arrays that have 5 elements each
a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
b = np.array([[11,12,13,14,15], [16,17,18,19,20]])

#add each elements at same index of a and b
c = a + b
#multiply
d = a * b
#creates a gaussian equation thingy
e = np.eye(5)

#creates an array of 50 random integers ranging from 1-1000 
f = np.array(random.sample(range(1, 1000), 50))
#reshapes array f into a 3d tensor. It has 5 arrays that each contains 2 arrays that contains 5 elements each
g = f.reshape(5,2,5)

#creates an matrix with 10 arrays of 10 elements
h = np.arange(1, 101).reshape(10,10)

horizontal_kernel = np.array([[ 1, 1, 1, 1]])
vertical_kernel = np.transpose(horizontal_kernel)
diag1_kernel = np.eye(4, dtype=np.uint8)
diag2_kernel = np.fliplr(diag1_kernel)
detection_kernels = [horizontal_kernel, vertical_kernel, diag1_kernel, diag2_kernel]

board = np.ones((6,7), dtype= int)



# print(diag2_kernel)

# i = f.reshape(10,5)
# j = np.fliplr(i)
# print(i)
# print(' --------------------')
# print(j)

