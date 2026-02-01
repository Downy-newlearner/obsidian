---
created: 2024-11-04 00:57
tags:
  - ResNet
  - LSTM
  - 지능정보특론
aliases:
---
![[4. Archive/Source/32202841유석 지능정보특론 발표자료.pdf]]

## Architecture
![[Pasted image 20241104141905.png]]

- Coventional Block은 네트워크 깊이는 낮추고 채널은 높이고, 크기는 낮춘다.
- Identify Block은 $32*4$ 깊이를 유지하며 정보를 다음 블록으로 넘기는 역할이다. 