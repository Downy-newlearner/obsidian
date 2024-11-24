---
created: 2024-11-24
tags: 
aliases:
  - plot_bounding_box_gallery
  - plot_image_gallery
reference:
---
```
# Object dection example

# Requirements:

# pip install keras-cv

# pip install opencv-python

  

import os

  

os.environ["KERAS_BACKEND"] = "tensorflow"  # @param ["tensorflow", "jax", "torch"]

  

import keras

import keras_cv

import numpy as np

  

from keras_cv import visualization

import matplotlib.pyplot as plt

  

# Load a pretrained model

pretrained_model = keras_cv.models.YOLOV8Detector.from_preset(

    "yolo_v8_m_pascalvoc", bounding_box_format="xywh"

)

  

# Load an image from a URL or local path

filepath = "C:/Users/jdh25/Downloads/b&b.jpeg"

image = keras.utils.load_img(filepath)

image = np.array(image)

  

visualization.plot_image_gallery(

    np.array([image]),

    value_range=(0, 255),

    rows=1,

    cols=1,

    scale=5,

)

plt.show()

  
  
  

# resize image

inference_resizing = keras_cv.layers.Resizing(

    640, 640, pad_to_aspect_ratio=True, bounding_box_format="xywh"

)

  
  
  

image_batch = inference_resizing([image])

  

class_ids = [

    "Aeroplane",  "Bicycle", "Bird",  "Boat", "Bottle",

    "Bus",  "Car", "Cat", "Chair", "Cow", "Dining Table",

    "Dog", "Horse", "Motorbike", "Person", "Potted Plant",

    "Sheep", "Sofa", "Train", "Tvmonitor", "Total", ]

class_mapping = dict(zip(range(len(class_ids)), class_ids))

  

y_pred = pretrained_model.predict(image_batch)

# y_pred is a bounding box Tensor:

# {"classes": ..., boxes": ...}

print(y_pred['classes'][0][:4])

print(y_pred['confidence'][0][:4])

print(y_pred['boxes'][0][:4])

  
  

breakpoint()

  
  

visualization.plot_bounding_box_gallery(

    image_batch,

    value_range=(0, 255),

    rows=1,

    cols=1,

    y_pred=y_pred,

    scale=5,

    font_scale=0.7,

    bounding_box_format="xywh",

    class_mapping=class_mapping,

)

  

plt.show()
```
# 1. keras-cv.visualization._plot_image_gallery_

`visualization.plot_image_gallery`는 Keras-CV의 **`visualization`** 모듈에서 제공하는 함수로, 이미지 배열을 격자 형태로 시각화하여 쉽게 확인할 수 있도록 도와줍니다.

---

### **`visualization`란?**

- **`keras_cv.visualization`** 모듈은 Keras-CV에서 이미지와 예측 결과(예: 바운딩 박스, 클래스 정보)를 시각화하기 위한 도구를 제공합니다.
- 주요 기능:
    - 이미지 격자 표시 (`plot_image_gallery`)
    - 바운딩 박스 격자 표시 (`plot_bounding_box_gallery`)

---

### **`plot_image_gallery` 함수 설명**

이 함수는 **이미지 배열을 격자 형태로 출력**하여 여러 이미지를 한눈에 볼 수 있도록 시각화합니다.

#### **매개변수 설명**:

1. **`np.array([image])`**:
    
    - 입력 이미지를 배열 형태로 전달합니다. `[image]`는 입력이 단일 이미지라도 배열 형태로 만들어 전달해야 합니다.
    - 예: 하나의 이미지를 전달하려면 `np.array([image])`처럼 배열 형태로 묶습니다.
2. **`value_range=(0, 255)`**:
    
    - 이미지를 시각화할 때 사용할 픽셀 값의 범위를 지정합니다.
    - `0~255`는 일반적인 8비트 이미지를 표현하며, 픽셀 값이 이 범위를 넘어가는 경우 시각화에 이상이 있을 수 있습니다.
3. **`rows=1`**:
    
    - 격자의 행(Row) 수를 지정합니다.
    - 여기서는 이미지를 한 줄로 표시하도록 지정합니다.
4. **`cols=1`**:
    
    - 격자의 열(Column) 수를 지정합니다.
    - 여기서는 이미지를 한 열로 표시하도록 지정합니다.
5. **`scale=5`**:
    
    - 이미지를 표시할 때 스케일을 조정합니다.
    - 값이 클수록 이미지가 더 커집니다.

---

### **전체 코드의 역할**

```python
visualization.plot_image_gallery(
    np.array([image]),  # 이미지 배열 입력
    value_range=(0, 255),  # 픽셀 값 범위 설정
    rows=1,  # 격자 행 수
    cols=1,  # 격자 열 수
    scale=5,  # 출력 이미지 크기 배율
)
```

- 입력된 이미지를 격자(여기선 1행 1열)로 화면에 출력합니다.
- **출력 결과**:
    - 단일 이미지를 큰 크기로 화면에 표시.

---

### **`visualization`의 장점**

- **빠른 시각화**:
    - 데이터를 직관적으로 확인할 수 있도록 지원합니다.
- **모델 예측과 통합**:
    - `plot_bounding_box_gallery`처럼 바운딩 박스 및 클래스 결과와 함께 이미지를 시각화할 수 있습니다.


# 2. keras-cv.visualization._plot_bounding_box_gallery_

이 코드는 **객체 탐지 모델의 예측 결과를 처리하고 시각화**하는 부분입니다. 주요 작업은 모델 예측을 수행한 후, 바운딩 박스를 포함한 결과를 출력하고 시각적으로 확인하는 것입니다.

---

### **코드 상세 설명**

#### **1. 예측 수행**

```python
y_pred = pretrained_model.predict(image_batch)
```

- **`pretrained_model`**: YOLOv8 객체 탐지 모델 (사전에 학습된 모델).
- **`image_batch`**: 크기가 조정된 이미지 데이터 배치 (입력 데이터).
- **`predict`**:
    - 모델이 입력 이미지를 처리하여 객체 탐지 결과를 반환.
    - 반환값 **`y_pred`**는 딕셔너리 형태로, 다음의 정보를 포함:
        - **`classes`**: 탐지된 객체의 클래스 ID.
        - **`confidence`**: 탐지된 객체의 신뢰도.
        - **`boxes`**: 바운딩 박스 좌표.

---

#### **2. 예측 결과 일부 출력**

```python
print(y_pred['classes'][0][:4])
print(y_pred['confidence'][0][:4])
print(y_pred['boxes'][0][:4])
```

- 예측된 결과를 확인하기 위해 `y_pred`의 일부를 출력합니다.
    - **`y_pred['classes'][0][:4]`**: 첫 번째 이미지에서 예측된 상위 4개 클래스 ID를 출력.
    - **`y_pred['confidence'][0][:4]`**: 첫 번째 이미지에서 예측된 상위 4개 클래스의 신뢰도 출력.
    - **`y_pred['boxes'][0][:4]`**: 첫 번째 이미지에서 예측된 상위 4개 바운딩 박스 좌표 출력.
- 결과 예시:
    
    ```python
    [2, 7, 14, 1]       # 탐지된 클래스 ID
    [0.85, 0.76, 0.65, 0.60]  # 클래스 신뢰도
    [[100, 200, 50, 60], ...]  # 바운딩 박스 좌표
    ```
    

---

#### **3. 디버깅**

```python
breakpoint()
```

- 디버거를 활성화하여 `y_pred`의 구조와 값을 탐색할 수 있습니다.
- 디버깅 시 `p y_pred` 등을 사용하여 데이터를 확인할 수 있습니다.

---

#### **4. 바운딩 박스 시각화**

```python
visualization.plot_bounding_box_gallery(
    image_batch,
    value_range=(0, 255),
    rows=1,
    cols=1,
    y_pred=y_pred,
    scale=5,
    font_scale=0.7,
    bounding_box_format="xywh",
    class_mapping=class_mapping,
)
```

- **`visualization.plot_bounding_box_gallery`**:
    - 입력 이미지 위에 바운딩 박스와 클래스 정보를 그려 시각화합니다.
- **매개변수 설명**:
    - **`image_batch`**:
        - 입력 이미지 데이터 배치.
    - **`value_range=(0, 255)`**:
        - 이미지 픽셀 값의 범위를 설정.
        - 일반적으로 RGB 이미지에서 사용되는 값.
    - **`rows=1, cols=1`**:
        - 출력 이미지 격자(grid)의 행과 열 개수. 여기서는 단일 이미지만 표시.
    - **`y_pred`**:
        - 모델 예측 결과. 바운딩 박스 및 클래스 정보를 포함.
    - **`scale=5`**:
        - 출력 이미지 크기 배율.
    - **`font_scale=0.7`**:
        - 바운딩 박스에 표시되는 텍스트(클래스 이름)의 글꼴 크기.
    - **`bounding_box_format="xywh"`**:
        - 바운딩 박스의 좌표 형식 (중심 좌표 `x, y` 및 너비와 높이 `w, h`).
    - **`class_mapping=class_mapping`**:
        - 클래스 ID를 클래스 이름으로 변환하기 위한 매핑.

---

#### **5. 시각화 결과 출력**

```python
plt.show()
```

- Matplotlib을 사용하여 생성된 시각화를 화면에 출력합니다.

---

### **결과**

1. 모델이 탐지한 객체의 클래스 ID, 신뢰도, 바운딩 박스 좌표가 출력됩니다.
2. 바운딩 박스와 클래스 이름이 이미지에 시각적으로 표시됩니다.

---

### **요약**

- **모델 예측**: `pretrained_model.predict(image_batch)`로 객체 탐지 수행.
- **결과 확인**: 클래스 ID, 신뢰도, 바운딩 박스를 출력.
- **시각화**: 바운딩 박스와 클래스 정보를 이미지 위에 그려 확인.