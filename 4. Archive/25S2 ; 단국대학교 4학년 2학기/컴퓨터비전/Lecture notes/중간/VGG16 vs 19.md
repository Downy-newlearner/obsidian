---
created: 2025-09-16
Question: VGG16, 19 차이 알려줘
---
좋은 질문이에요 👍

  

**VGG16**과 **VGG19**는 둘 다 옥스퍼드 Visual Geometry Group이 제안한 **VGGNet** 아키텍처의 변형입니다.

차이는 **층(layer)의 개수**에 있어요.

---

### **1. 공통점**

- 둘 다 **3×3 Convolution 필터**만 사용
    
- stride=1, padding=1을 유지해서 feature map 크기를 보존
    
- **Max Pooling(2×2, stride=2)** 로 크기 줄이기
    
- 마지막에 **3개의 Fully Connected layer (4096, 4096, 1000 classes)**
    
- Activation은 **ReLU**, Regularization은 **Dropout**
    

---

### **2. 차이점**

- **VGG16**: 총 **16개의 weight layer** (13 conv + 3 FC)
    
- **VGG19**: 총 **19개의 weight layer** (16 conv + 3 FC)
    
- 즉, VGG19는 **중간에 conv layer가 3개 더 많음** → 더 깊은 네트워크
    

---

### **3. 성능 차이**

- VGG19가 더 깊어서 **표현력은 약간 더 높지만**,
    
- 파라미터 수도 더 많아지고, **연산량이 훨씬 커서 속도는 느림**.
    
- 실제로 ImageNet에서 성능 차이는 크지 않아, 많은 연구에서는 **VGG16**을 더 자주 사용.
    

---

👉 요약

- **VGG16 = 13 conv + 3 FC = 16 layers**
    
- **VGG19 = 16 conv + 3 FC = 19 layers**
    
- VGG19가 더 깊지만, 계산량이 크고 성능 차이는 미미해서 VGG16이 실무에서 더 널리 쓰임.
    

  

혹시 원하시면, 제가 **VGG16 vs VGG19 레이어 구조를 한눈에 보는 표**로 정리해드릴까요?