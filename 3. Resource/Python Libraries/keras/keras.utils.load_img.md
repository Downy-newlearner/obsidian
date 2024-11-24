---
created: 2024-11-24
tags: 
aliases:
  - load_img
reference:
---
`keras.utils.load_img(filepath)` 메서드는 Keras에서 이미지를 로드하기 위해 사용됩니다. 

---

### **기능**

- 주어진 파일 경로(`filepath`)에서 이미지를 로드하여 Keras에서 사용할 수 있는 **[[PIL 이미지 객체]]**로 반환합니다.
- 로드된 이미지를 추가로 전처리하거나, 딥러닝 모델에 입력하기 전에 배열로 변환할 수 있습니다.

---

### **매개변수**

- **`filepath`**:
    
    - 로드할 이미지 파일의 경로입니다.
    - 로컬 디렉토리나 URL을 지원합니다.
- **`color_mode`** _(선택사항)_:
    
    - 이미지를 로드할 색상 모드. 기본값은 `"rgb"`입니다.
        - `"grayscale"`: 흑백 이미지로 로드.
        - `"rgb"`: 3채널(RGB) 컬러 이미지로 로드.
        - `"rgba"`: 4채널(RGBA) 컬러 이미지로 로드.
- **`target_size`** _(선택사항)_:
    
    - 로드된 이미지를 `(height, width)` 크기로 조정합니다. 지정하지 않으면 원본 크기로 로드됩니다.
- **`interpolation`** _(선택사항)_:
    
    - 이미지 크기를 조정할 때 사용할 보간 방법. 기본값은 `"nearest"`입니다.
        - `"nearest"`, `"bilinear"`, `"bicubic"`, `"lanczos"`, `"hamming"`, `"box"` 등이 있습니다.

---

### **반환값**

- **PIL.Image 객체**:
    - 이미지 데이터를 포함한 PIL 객체입니다.
    - 필요할 경우 `numpy.array()`로 변환해 사용할 수 있습니다.

---

### **사용 예시**

```python
from keras.utils import load_img, img_to_array

# 이미지 로드
image = load_img("path/to/image.jpg", target_size=(224, 224), color_mode="rgb")

# PIL 이미지 객체를 NumPy 배열로 변환
image_array = img_to_array(image)
```

---

### **요약**

`keras.utils.load_img()`는 이미지를 파일 경로에서 로드하고, 딥러닝 모델에서 사용할 수 있는 **PIL 이미지**로 반환하는 메서드입니다. 크기 조정 및 색상 모드 변환도 함께 지원합니다.