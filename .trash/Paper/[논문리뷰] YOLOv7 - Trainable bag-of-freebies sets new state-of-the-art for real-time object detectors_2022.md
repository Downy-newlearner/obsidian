---
title: "[논문리뷰] YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors_2022"
Authors: ""
date: 'Error: `format` can only be applied to dates. Tried for format object'
updated: "2025-02-10T15:14:03+09:00"
Link: "https://velog.io/@yyk9612/논문리뷰-YOLOv7-Trainable-bag-of-freebies-sets-new-state-of-the-art-for-real-time-object-detectors2022"
tags:
  
---
> [!Abstract]
>
> 가장 빠른 객체 검출 알고리즘 모델 중 하나파이썬, 텐서플로 기반 프레임워크가 아닌 C++로 구현된 코드 기준 GPU사용 시, 초당 170 프레임 (170 FPS. frames per second)Single Network 하나만을 사용하여 속도가 매우 빠름Less f
>\
## 1. Annotations  
> <mark style="background-color: #2ea8e5">Highlight</mark>  
> Non-max suppresion  
> [page 1]()  
> - 객체 검출에서 여러 겹치는 [[Bounding box]] 중 가장 중요한 것을 선택하기 위한 기법입니다. 일반적으로 신뢰도가 가장 높은 박스만 남기고 나머지는 제거합니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> IoU  
> [page 1]()  
> - 두 개의 Bounding box가 겹치는 정도를 측정하는 지표로, 겹치는 영역의 크기를 두 box의 전체 영역 크기로 나누어 계산합니다.  


> <mark style="background-color: #ffd400">Highlight</mark>  
> E-ELAN  
> [page 1]()  
> - YOLO v7을 개선하기 위한 구조로, 효율성과 계산 비용을 줄이기 위해 설계된 네트워크 구조입니다.  


> <mark style="background-color: #ffd400">Highlight</mark>  
> Expand -> Shuffle -> Merge  
> [page 1]()  
> - 네트워크의 학습 능력을 향상시키기 위한 과정이며, 이로 인해 원래의 그라디언트 경로가 보존됩니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> original gradient path  
> [page 1]()  
> - 네트워크가 학습할 수 있도록 중요한 그라디언트 정보가 손실 없이 전달되는 경로입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> group conv g  
> [page 1]()  
> - convolution 연산에서 그룹화된 convolution 방법을 사용하는 파라미터로, 계산 효율성을 높입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> computational block의 채널수  
> [page 1]()

> <mark style="background-color: #2ea8e5">Highlight</mark>  
> Concatenation-based  
> [page 1]()  
> - 서로 다른 데이터나 특성을 하나로 결합하는 방식으로, 신경망에서 여러 레이어의 출력을 연결하기 위해 사용됩니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> Model Scaling  
> [page 1]()  
> - 모델의 구조를 조정해 크기, 깊이, 너비 등을 변화시켜 정확도와 속도를 최적화하는 기법입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> scale  
> [page 1]()  
> - 모델의 특정 속성(너비, 깊이, 해상도 등)을 조정하여 다양한 크기의 모델을 생성하는 것을 의미합니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> Transition Layer  
> [page 1]()  
> - 신경망의 구조에서 서로 다른 레이어 간의 연결을 담당하는 레이어로, 데이터의 크기나 채널 수를 변환합니다.  


> <mark style="background-color: #ffd400">Highlight</mark>  
> Compound model scaling method  
> [page 1]()  
> - YOLO v7에서 사용된 방법으로, 모델의 깊이, 너비, 해상도를 함께 조정하여 효율적으로 성능을 향상시키는 기법입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> depth scaling up  
> [page 1]()  
> - 모델의 깊이를 늘려 레이어 수를 증가시킴으로써 학습 능력을 강화하는 방법입니다.  


