---
created: 2025-09-15
Question: AlexNet에서 사용된 Local Response Normalization(LRN)에 대해 설명해줘.
---
좋은 질문이에요 👍 AlexNet에서 **Local Response Normalization(LRN)** 은 2012년 당시 새로운 정규화 기법으로 도입된 것으로, 신경망이 **생물학적 신경 세포의 lateral inhibition(측방 억제)** 현상을 흉내 내기 위해 사용되었어요.

---

### **설명**

1. **아이디어**
    
    - 사람의 시각 피질에서는 한 뉴런이 강하게 반응하면 주변 뉴런의 반응을 억제해서 특정 특징을 더 선명하게 인식하게 돼요.
        
    - AlexNet은 이를 모방해, 특정 위치에서 한 채널의 뉴런이 강하게 활성화되면 인접 채널의 활성화를 줄여 상대적인 대조를 강화했어요.
        
    
2. **계산 방식**
    
    LRN은 한 뉴런의 출력을 **주변 채널들의 활성값 제곱합**으로 나누어 정규화합니다.
    
    수식으로 쓰면:
    

```
b_{x,y}^i = a_{x,y}^i / (k + α * Σ_{j=max(0,i-n/2)}^{min(N-1,i+n/2)} (a_{x,y}^j)^2 )^β
```

2. - a_{x,y}^i : (x,y) 위치, i번째 채널의 활성화 값
        
    - n : 정규화에 포함되는 채널 개수 (보통 5)
        
    - k, α, β : 하이퍼파라미터 (AlexNet에서는 k=2, α=10^-4, β=0.75)
        
    - b_{x,y}^i : 정규화된 출력
        
    
    즉, 특정 채널의 값이 크면 주변 채널들의 값이 억제돼서 상대적으로 더 두드러지게 만들어요.
    
3. **효과**
    
    - 일반화(regularization) 효과가 있어 과적합을 줄였고,
        
    - 특징 맵 간의 경쟁을 유도해 **희소 표현(sparse representation)** 을 얻는 데 도움을 줬습니다.
        
    

---

### **현재 관점**

- 당시에는 ReLU와 함께 AlexNet의 성능 향상에 기여했지만,
    
- 이후 [[Batch Normalization(BN)]]이 등장하면서 LRN은 사실상 쓰이지 않게 됐습니다.
    
- 이유는 BN이 학습 안정화와 성능 향상에 훨씬 효과적이기 때문이에요.
    

---

한 줄 요약:

**LRN은 강하게 활성화된 뉴런 주변의 다른 뉴런들을 억제해 대비를 강화하고 일반화를 돕는 정규화 기법이지만, 지금은 BatchNorm 같은 더 강력한 기법에 의해 대체되었다.**

  

혹시 원하시면 제가 **AlexNet에서 LRN이 적용된 위치(예: 첫 번째, 두 번째 ReLU 뒤)** 를 그림으로 정리해드릴까요?



좋습니다! AlexNet에서 **LRN(Local Response Normalization)** 이 적용된 위치를 정리해드릴게요.

---

### **AlexNet 구조에서의 LRN 위치**

1. **Conv1 → ReLU → LRN → MaxPooling**
    
    - 첫 번째 합성곱(Conv1, 11×11 필터, stride 4, 96개 채널) 후에 ReLU를 거치고, 그 결과에 LRN을 적용한 다음 MaxPooling을 수행합니다.
        
    
2. **Conv2 → ReLU → LRN → MaxPooling**
    
    - 두 번째 합성곱(Conv2, 5×5 필터, 256개 채널) 후에도 ReLU → LRN → MaxPooling 순으로 진행됩니다.
        
    
3. **그 이후의 Conv3, Conv4, Conv5**
    
    - ReLU만 사용되고, LRN은 적용되지 않습니다.
        
    

---

### **그림으로 정리 (텍스트 다이어그램)**

```
Input (224x224 RGB)
 ↓
Conv1 (11x11, stride 4, 96 filters)
 ↓
ReLU
 ↓
LRN   ◀── 첫 번째 적용
 ↓
MaxPooling
 ↓
Conv2 (5x5, 256 filters)
 ↓
ReLU
 ↓
LRN   ◀── 두 번째 적용
 ↓
MaxPooling
 ↓
Conv3 (3x3, 384 filters)
 ↓
ReLU
 ↓
Conv4 (3x3, 384 filters)
 ↓
ReLU
 ↓
Conv5 (3x3, 256 filters)
 ↓
ReLU
 ↓
MaxPooling
 ↓
FC6 → ReLU → Dropout
 ↓
FC7 → ReLU → Dropout
 ↓
FC8 → Softmax
```

---

즉, **AlexNet에서는 LRN이 처음 두 개의 합성곱 블록 뒤에만 적용** 되었어요.

이게 당시 ImageNet 대규모 학습에서 성능 향상에 꽤 기여했지만, 이후 연구들에서 **BN 도입 이후에는 성능 이득이 거의 없어져서 빠지게 된 것**입니다.

  

혹시 제가 이 구조를 **컬러 블록 다이어그램**으로 그려드리면 더 보기 쉽게 정리해드릴까요?


![[AlexNet Architecture with LRN Highlighted.png]]

위 다이어그램은 AlexNet의 전체 아키텍처 흐름을 블록으로 표현한 것이고, LRN(Local Response Normalization)이 적용된 위치를 강조했습니다.

- Conv1 → ReLU → LRN → Pool
    
- Conv2 → ReLU → LRN → Pool
    
- Conv3 → ReLU
    
- Conv4 → ReLU
    
- Conv5 → ReLU → Pool
    
- FC6 → ReLU
    
- FC7 → ReLU
    
- FC8 → Softmax
    

  

즉, LRN은 초반부 **Conv1과 Conv2 이후**에만 적용되었고, 이후 레이어에서는 사용되지 않았습니다.

  

혹시 제가 이 블록도를 논문 원문 그림처럼 더 “병렬 구조(두 개 GPU 분할)”로 그려드릴까요, 아니면 지금처럼 단순화된 직렬 구조가 이해하기에 편하신가요?