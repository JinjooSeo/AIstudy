import numpy as np

arr1 = np.array([[5, 7], [9, 11]], float)
arr2 = np.array([[2, 4], [5, 8]], float)

concat_1 = np.concatenate((arr1, arr2), axis = 0) #expend the dimension to vertical way
concat_2 = np.concatenate((arr1, arr2), axis = 1) #expend the dimension to horizontal way

print(arr1)
print(arr1)
print(f'concatenate to vertical way : \n {concat_1}')
print(f'concatenate to horizontal way : \n {concat_1}')