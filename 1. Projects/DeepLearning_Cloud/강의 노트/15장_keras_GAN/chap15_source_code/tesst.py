import numpy as np

arr = np.array([1, 2, 3])
print("Original", arr)  # [1 2 3]
print("Original Shape:", arr.shape)  # (3,)

# 차원을 추가
arr_expanded = np.expand_dims(arr, axis=1)
print("Expanded", arr_expanded)  # [[1 2 3]]
print("Expanded Shape:", arr_expanded.shape)  # (1, 3)