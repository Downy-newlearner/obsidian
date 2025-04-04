---
created: 2024-11-11
tags:
  - Object_Detection
  - DETR
aliases:
  - Generalized Intersection over Union
---
**GIoU (Generalized Intersection over Union)**:  
[[IoU]]의 한계를 보완한 지표로, 예측 상자와 *실제 상자가 겹치지 않을 때에도 상자의 위치와 크기를 고려한 차이를 계산*하여 정확도를 평가한다.

**핵심 디테일**:  
GIoU는 IoU에 추가적으로 두 상자를 포함하는 최소 외접 상자의 크기를 고려하여, 예측 상자가 실제 상자와 멀리 떨어져 있을 때도 차이를 측정한다. 이를 통해, 겹치지 않는 경우에도 벌점을 부여하여 학습 과정에서 더 나은 상자 위치를 학습하도록 유도한다.

**IoU의 개선점**:  
IoU는 예측 상자와 실제 상자가 겹치지 않는 경우 $0$으로 계산되어 상자 간 위치 차이를 반영하지 못하는 단점이 있다. GIoU는 이러한 상황에서 두 상자 간의 위치 차이를 고려한 추가적인 벌점을 부여하여, 겹치지 않는 경우에도 더 나은 위치 예측을 유도한다.

**요약**:  
GIoU는 IoU의 단점인 겹치지 않는 상자 간의 차이를 반영하여 더 정확한 위치 평가를 가능하게 한다.