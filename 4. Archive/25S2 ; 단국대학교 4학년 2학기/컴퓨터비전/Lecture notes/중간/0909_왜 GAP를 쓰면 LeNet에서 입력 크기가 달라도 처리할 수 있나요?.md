---
created: 2025-09-09
Question: LeNet에서 FC대신 GAP를 사용해서 input size가 달리도 handle할 수 있게 됐다고 하는데 이유가 뭐야? 채널별로 평균내서 계산하니까 input size와 무관하게 계산이 가능해서 그런가?
---
맞아요! 질문을 다시 정리하면:

“LeNet 같은 CNN에서 Fully Connected(FC) layer 대신 Global Average Pooling(GAP)을 쓰면 input size가 달라도 처리할 수 있다는데, 이유가 뭔가? 채널별 평균 때문인가?”

---

### **1. FC layer의 한계**

- FC layer는 입력 크기가 **고정**되어 있어야 합니다.
    
- 예를 들어 convolution 결과가 7×7×256이라면, 이를 펼쳐서 12544차원의 벡터로 만들고 FC weight와 곱해야 합니다.
    
- 만약 입력 이미지 크기가 변하면 → feature map 크기 H×W도 변함 → FC 입력 차원도 달라져서 weight shape가 맞지 않음 → 학습 불가.
    

---

### **2. GAP의 장점**

- GAP은 **각 채널의 모든 공간 위치(H×W)를 평균내어 단 하나의 값**으로 압축합니다.
    
- 따라서 feature map이
    
    - 7×7×256이든,
        
    - 14×14×256이든,
        
    - 28×28×256이든
        
        상관없이, 결과는 항상 **1×1×256**이 됩니다.
        
    
- 이렇게 하면 input image 크기가 변해도, 마지막 분류 layer (예: softmax, 256→클래스 수) 구조는 바뀌지 않습니다.
    

---

### **3. 직관적으로 말하면**

  

네, 말씀하신 것처럼 **채널별 평균을 내므로 공간적 크기(H, W)에 구애받지 않고, 채널 수(C)만 맞으면 동일한 출력 차원**을 얻을 수 있기 때문에 input size가 달라도 handle 가능해지는 겁니다.

