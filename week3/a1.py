import numpy as np

arr1 = np.random.rand(5,3) #random value in m x n matrix
arr2 = np.random.rand(3,2)

dot = np.dot(arr1,arr2)
print(dot, dot.shape)