import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original Shape:", arr.shape)  # (2, 3)

# 앞에 차원 추가
arr_expanded_0 = np.expand_dims(arr, axis=0)
print(arr_expanded_0.shape)  # (1, 2, 3)

# 중간에 차원 추가
arr_expanded_1 = np.expand_dims(arr, axis=1)
print(arr_expanded_1.shape)  # (2, 1, 3)

# 뒤에 차원 추가
arr_expanded_2 = np.expand_dims(arr, axis=-1)
print(arr_expanded_2.shape)  # (2, 3, 1)