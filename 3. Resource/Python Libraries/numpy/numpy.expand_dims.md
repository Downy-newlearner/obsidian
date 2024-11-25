---
created: 2024-11-24
tags: 
aliases:
  - expand_dims
reference:
---
`np.expand_dims`는 NumPy 배열의 차원을 확장하는 함수로, 지정한 위치에 새로운 차원을 추가합니다. 이를 통해 배열의 모양(shape)을 변경하여 특정 작업(예: 모델 입력)을 위한 요구 조건을 충족할 수 있습니다.

---

### **사용법**

```python
np.expand_dims(a, axis)
```

#### **매개변수**

1. **`a`**: 입력 배열 (NumPy 배열).
2. **`axis`**: 추가할 차원의 위치를 지정합니다.
    - 음수 값을 사용하면 배열의 끝에서부터 계산됩니다.
    - 예를 들어, `axis=0`은 가장 앞에 차원을 추가하고, `axis=-1`은 가장 뒤에 차원을 추가합니다.

#### **반환값**

- 지정한 위치에 차원이 추가된 새로운 배열을 반환합니다.

---

### **예제**

#### 1. 기본 사용

```python
import numpy as np


arr = np.array([1, 2, 3])

print("Original", arr)  # [1 2 3]

print("Original Shape:", arr.shape)  # (3,)

  

# 차원을 추가
arr_expanded = np.expand_dims(arr, axis=0)

print("Expanded", arr_expanded)  # [[1 2 3]]

print("Expanded Shape:", arr_expanded.shape)  # (1, 3)


# 차원을 추가
arr_expanded_2 = np.expand_dims(arr, axis=1)

print("Expanded", arr_expanded_2)

print("Expanded Shape:", arr_expanded_2.shape)
```
`Original [1 2 3]`
`Original Shape: (3,)`
`Expanded [[1 2 3]]`
`Expanded Shape: (1, 3)`
```
Expanded [[1]
 [2]
 [3]]
```
`Expanded Shape: (3, 1)`
#### 2. 여러 차원에서 사용

```python
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
```

Original Shape: (2, 3)
(1, 2, 3)
(2, 1, 3)
(2, 3, 1)

---

### **사용 사례**

1. **딥러닝 모델 입력 준비**:
    
    - 딥러닝 모델은 보통 특정 차원을 가진 데이터를 입력으로 요구합니다(예: 배치 차원).
    - `np.expand_dims`를 사용해 입력 데이터를 모델이 기대하는 모양으로 변환합니다.
        
        ```python
        image = np.array([[1, 2], [3, 4]])  # Shape: (2, 2)
        image_with_batch = np.expand_dims(image, axis=0)  # Shape: (1, 2, 2)
        ```
        
2. **방향성 유지**:
    
    - 1D 데이터에 추가 차원을 추가해 특정 연산에서 방향성을 유지합니다.
        
        ```python
        vector = np.array([1, 2, 3])  # Shape: (3,)
        column_vector = np.expand_dims(vector, axis=1)  # Shape: (3, 1)
        ```
        
3. **스칼라 확장**:
    
    - 스칼라 값을 배열처럼 다룰 수 있도록 확장합니다.
        
        ```python
        scalar = np.array(5)
        expanded = np.expand_dims(scalar, axis=0)  # Shape: (1,)
        ```
        

---

### **본문 코드에서의 사용**

```python
img_array_train = np.expand_dims(img_array_train, axis=0)
```

- **역할**: `img_array_train`은 원래 (28, 28) 모양의 2D 배열입니다.
- **추가된 차원**: `axis=0`을 사용해 맨 앞에 배치 차원을 추가하여 `(1, 28, 28)`로 변환.
- **목적**: 딥러닝 모델은 보통 배치 형태의 입력 데이터를 요구하므로, 배치 차원을 추가하여 모델 입력 형식에 맞춥니다.

---

### **요약**

- `np.expand_dims`는 배열에 **새로운 차원을 추가**합니다.
- 딥러닝에서 입력 데이터를 모델이 요구하는 형식으로 변환할 때 자주 사용됩니다.
- 본문에서는 `(28, 28)` 이미지를 `(1, 28, 28)`로 변환하여 배치 차원을 추가했습니다.