---
created: 2024-11-24
tags: 
aliases:
  - layer.resizing
reference:
---
```python
keras_cv.layers.Resizing(
    640, 640, pad_to_aspect_ratio=True, bounding_box_format="xywh"
)
```

이 코드는 Keras-CV에서 제공하는 `Resizing` 레이어를 생성하는 부분으로, **입력 이미지를 크기 조정**하고, 필요하면 **비율을 유지하면서 패딩(padding)**을 추가합니다. 이를 통해 이미지의 크기를 모델 입력에 맞게 전처리합니다.

---

### **매개변수 설명**

1. **`640, 640`**:
    
    - 출력 이미지의 **목표 크기(height, width)** 를 지정합니다.
    - 여기서는 출력 이미지를 `(640, 640)` 크기로 변환합니다.
2. **`pad_to_aspect_ratio=True`**:
    
    - 입력 이미지의 **종횡비(aspect ratio)** 를 유지하기 위해 **패딩(padding)** 을 추가합니다.
    - 패딩이 적용되면 이미지가 왜곡되지 않고, 설정한 `(640, 640)` 크기로 맞춰집니다.
    - 이 옵션이 `False`일 경우, 이미지는 강제로 크기 조정되며 종횡비가 유지되지 않을 수 있습니다.
3. **`bounding_box_format="xywh"`**:
    
    - 바운딩 박스의 좌표 형식을 지정합니다.
    - `"xywh"`는 바운딩 박스의 형식을 **(x 중심 좌표, y 중심 좌표, 너비, 높이)** 로 나타냅니다.
    - 이 설정은 바운딩 박스가 이미지 크기 조정 후에도 올바르게 조정되도록 사용됩니다.

---

### **기능**

- **이미지 크기 조정**:
    
    - 입력 이미지의 크기를 `(640, 640)`으로 변환합니다.
    - 종횡비를 유지하면서 필요할 경우 패딩을 추가합니다.
- **바운딩 박스 크기 조정**:
    
    - 이미지와 함께 바운딩 박스 좌표도 적절히 조정됩니다.
    - 예: 바운딩 박스가 종횡비 조정에 맞게 자동 변환.

---

### **예제 사용**

```python
import keras_cv
import numpy as np

# 임의의 입력 이미지 (3채널 RGB)
image = np.random.rand(300, 500, 3)  # 입력 이미지 크기: (300, 500)
bounding_box = np.array([[100, 50, 200, 150]])  # 임의의 바운딩 박스: xywh 형식

# Resizing 레이어 정의
resize_layer = keras_cv.layers.Resizing(
    640, 640, pad_to_aspect_ratio=True, bounding_box_format="xywh"
)

# 이미지 및 바운딩 박스 크기 조정
resized_image, resized_bounding_box = resize_layer([image, bounding_box])

print("Resized Image Shape:", resized_image.shape)
print("Resized Bounding Box:", resized_bounding_box)
```

---

### **결론**

`keras_cv.layers.Resizing`은 입력 이미지와 바운딩 박스를 크기 조정하고, **종횡비를 유지하며 패딩을 추가**해 모델 입력에 적합한 형태로 변환합니다. 특히 바운딩 박스 좌표가 이미지 크기 조정에 맞게 자동 조정되므로, **객체 탐지 모델**에 유용합니다.