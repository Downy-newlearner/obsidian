---
created: 2025-09-15
Question: 그래서 normalization, regularization은 왜 필요한가?
---
좋은 질문이에요 👍

  

딥러닝에서 **Normalization(정규화)** 과 **Regularization(규제)** 는 비슷해 보이지만 목적과 초점이 다릅니다.

---

### **Normalization (정규화)**

- **목적**: 학습을 안정적으로 하고 빠르게 수렴시키는 것.
    
- **이유**:
    
    - 신경망의 입력 값이나 은닉층 출력을 일정한 범위(보통 평균 0, 분산 1)로 맞추면 **경사 소실/폭주(vanishing/exploding gradient)** 를 줄일 수 있음.
        
    - 각 층이 비슷한 분포를 가지게 되어 **학습 속도가 빨라지고** 학습이 더 안정적임.
        
    
- 예시: Batch Normalization, Layer Normalization, Instance Normalization 등.
    

---

### **Regularization (규제)**

- **목적**: 모델이 훈련 데이터에 과적합(overfitting)하지 않고 **일반화 성능**을 높이는 것.
    
- **이유**:
    
    - 신경망이 파라미터 수가 많아 복잡하면 학습 데이터에만 맞추고, 새로운 데이터에선 성능이 떨어질 수 있음.
        
    - 규제를 통해 가중치 크기를 제한하거나(dropout, weight decay), 데이터 다양성을 늘려(data augmentation) 더 **견고한 모델**을 만듦.
        
    
- 예시: Dropout, L1/L2 규제, Early Stopping, Data Augmentation.
    

---

### **한 줄 요약**

- **Normalization = 수학적 안정성, 빠른 학습**
    
- **Regularization = 일반화 성능, 과적합 방지**
    

---

혹시 이걸 **AlexNet 맥락**(LRN, Dropout 등)에서 연결해서 정리해드릴까요?




좋습니다 👍 AlexNet 맥락에서 **Normalization**과 **Regularization**을 연결해서 정리해드릴게요.

---

### **AlexNet에서의 Normalization**

- AlexNet은 **LRN (Local Response Normalization)** 을 사용했어요.
    
- 당시 목적은 **특정 뉴런이 강하게 활성화되면 주변 뉴런은 억제**하도록 해서, **더 뚜렷한 특징 대비(contrast)** 를 만드는 것.
    
- 이는 **Normalization**의 예시로, 학습을 안정화하고 좋은 일반화를 기대했지만, 지금은 **Batch Normalization(BN)** 같은 더 강력한 방법이 쓰이고 있어요.
    

---

### **AlexNet에서의 Regularization**

- AlexNet은 파라미터 수가 **60M 이상**으로 매우 크기 때문에 **과적합 위험**이 컸습니다.
    
- 이를 막기 위해 **Dropout**을 도입했는데, 이는 훈련 시 무작위로 일부 뉴런을 끊어버려서 네트워크가 **특정 뉴런에 의존하지 않게** 만들고, **일반화 성능을 크게 향상**시켰습니다.
    
- 또, Data Augmentation(이미지 회전, 이동, 색 변화 등)도 Regularization의 일환으로 사용됐습니다.
    

---

### **정리**

- **Normalization (LRN)** → 학습 안정성, 특징 대비 강조.
    
- **Regularization (Dropout + Data Augmentation)** → 과적합 방지, 일반화 성능 확보.
    

---

즉, AlexNet은 **Normalization으로 학습을 안정화**하고, **Regularization으로 일반화 성능을 확보**하여 당시 ImageNet 대회에서 큰 성공을 거둘 수 있었던 거예요 🚀.

  

👉 원한다면, AlexNet에 쓰인 **LRN, Dropout, Data Augmentation 각각의 메커니즘을 한 장짜리 표**로 요약해드릴까요?