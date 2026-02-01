---
created: 2025-09-15
Question: CNN 맥락에서 topology가 무슨 뜻이야?
---
CNN 문맥에서 **topology**는 단순히 “레이어 구조”나 “네트워크 연결 방식”을 뜻해요.

  

조금 풀어서 말하면:

- 어떤 레이어가 어떤 레이어와 연결되는지 (예: Conv → Pooling → Conv → FC → Output)
    
- 각 레이어에서 맵 수, 커널 크기, 연결 형태(완전 연결 vs 부분 연결 등)
    
- 전체 네트워크의 **구성도와 배치 방식**
    

  

즉, topology는 CNN의 **아키텍처 구조도**를 지칭하는 말이에요.

  

예를 들어 LeNet-5의 topology는 “Conv(6맵) → Pool → Conv(16맵, 부분 연결) → Pool → Conv(120맵) → FC(84) → Output(RBF)” 이런 흐름을 가리키는 거죠.

  

👉 정리: CNN에서 topology는 **네트워크 층의 배열과 연결 형태를 기술하는 구조적 설계**라는 뜻이에요.

  

혹시 이걸 “architecture”랑 어떤 차이가 있는지도 정리해드릴까요?