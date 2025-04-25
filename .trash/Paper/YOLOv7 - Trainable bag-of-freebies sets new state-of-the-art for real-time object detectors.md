---
title: "YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors"
Authors: "Chien-Yao Wang, Alexey Bochkovskiy, Hong-Yuan Mark Liao"
date: '2022-07-06'
updated: "2025-02-10T15:03:39+09:00"
Link: "http://arxiv.org/abs/2207.02696"
tags:
  
 - Computer-Science---Computer-Vision-and-Pattern-Recognition
---
> [!Abstract]
>
> YOLOv7 surpasses all known object detectors in both speed and accuracy in the range from 5 FPS to 160 FPS and has the highest accuracy 56.8% AP among all known real-time object detectors with 30 FPS or higher on GPU V100. YOLOv7-E6 object detector (56 FPS V100, 55.9% AP) outperforms both transformer-based detector SWIN-L Cascade-Mask R-CNN (9.2 FPS A100, 53.9% AP) by 509% in speed and 2% in accuracy, and convolutional-based detector ConvNeXt-XL Cascade-Mask R-CNN (8.6 FPS A100, 55.2% AP) by 551% in speed and 0.7% AP in accuracy, as well as YOLOv7 outperforms: YOLOR, YOLOX, Scaled-YOLOv4, YOLOv5, DETR, Deformable DETR, DINO-5scale-R50, ViT-Adapter-B and many other object detectors in speed and accuracy. Moreover, we train YOLOv7 only on MS COCO dataset from scratch without using any other datasets or pre-trained weights. Source code is released in https://github.com/WongKinYiu/yolov7.
>\
## 1. Annotations  
> <mark style="background-color: #2ea8e5">Highlight</mark>  
> SWINL Cascade-Mask R-CNN  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=Y6Z8G7B7)  
> - SWINL Cascade-Mask R-CNN은 SWIN Transformer와 Cascade-Mask R-CNN을 결합하여 객체 탐지와 분할 성능을 향상시킨 모델입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> YOLOR  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=EJG2BNAD)  
> - YOLOR은 분류와 탐지를 동시에 수행하는 신경망 구조로, 다양한 객체 탐지 작업에 적합하게 설계된 모델입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> YOLOX  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=A9EJQA7A)  
> - YOLOX는 YOLO 시리즈의 향상된 모델로, Anchor-Free 기법과 추가적인 성능 최적화를 통해 고성능 객체 탐지를 수행합니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> Scaled-YOLOv4  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=5MBW4RUS)  
> - Scaled-YOLOv4는 다양한 크기의 모델을 제공하여 작은 모델부터 대규모 모델까지 범용적으로 사용할 수 있는 객체 탐지 모델입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> YOLOv5  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=G5LBXXVD)  
> - YOLOv5는 빠른 학습과 추론 속도, 높은 정확성을 제공하는 객체 탐지 모델로, PyTorch로 구현되었습니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> DETR  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=2FGS4S7A)  
> - DETR은 트랜스포머 아키텍처를 활용한 최초의 객체 탐지 모델로, 앵커 박스가 필요 없는 종단간 방식으로 작동합니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> Deformable DETR  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=5UC9I2AV)  
> - Deformable DETR은 DETR 모델의 개선된 버전으로, 변형 가능한 어텐션 메커니즘을 통해 학습 속도를 향상시킨 모델입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> DINO-5scale-R50  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=KKNH2N3R)  
> - DINO-5scale-R50은 고해상도 이미지에 대해 다양한 스케일에서 객체를 효과적으로 탐지하는 트랜스포머 기반 모델입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> ViT-Adapter-B  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=7F5GPP7Z)  
> - ViT-Adapter-B는 Vision Transformer의 성능을 확장하기 위한 추가적인 모듈을 제공하여 다양한 비전 작업에 적합한 성능을 발휘합니다.  


> <mark style="background-color: #ffd400">Highlight</mark>  
> In this paper, the real-time object detector we proposed mainly hopes that it can support both mobile GPU and GPU devices from the edge to the cloud.  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=CPA89WU4)  
> - 로컬 환경부터 클라우드 서버까지 다양한 플랫폼에서 실시간 처리가 가능하도록 지원하기를 희망한다  


> <mark style="background-color: #ffd400">Highlight</mark>  
> More recently, the development of real-time object detector has focused on the design of efficient architecture.  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=MC3BE335)

> <mark style="background-color: #e56eee">Highlight</mark>  
> our proposed methods will focus on the optimization of the training process.  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=K63F77TK)

> <mark style="background-color: #ffd400">Highlight</mark>  
> strengthen the training cost for improving the accuracy of object detection  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=SPKPUYM9)

> <mark style="background-color: #e56eee">Highlight</mark>  
> trainable bag-of-freebies  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=Z6PL84CQ)

> <mark style="background-color: #2ea8e5">Highlight</mark>  
> model re-parameterization  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=USIWPK4T)  
> - 모델 재매개변수화는 학습 과정 중 모델 구조를 변경하여 최적화 성능을 개선하고, 추론 시 더 단순한 모델로 변환시키는 방법입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> dynamic label assignment  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=LMNR8BB7)  
> - 동적 라벨 할당은 학습 중에 입력 데이터에 따라 라벨을 유동적으로 조정하여 모델의 적응성과 성능을 향상시키는 기법입니다.  


> <mark style="background-color: #ffd400">Highlight</mark>  
> In this paper, we will present some of the new issues we have discovered and devise effective methods to address them.  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=T8QLKC9X)

> <mark style="background-color: #ffd400">Highlight</mark>  
> model reparameterization  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=785IUB6R)

> <mark style="background-color: #ffd400">Highlight</mark>  
> “How to assign dynamic targets for the outputs of different branches?”  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=WP77X5F3)

> <mark style="background-color: #ffd400">Highlight</mark>  
> coarse-to-fine lead guided label assignment  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=3PJ8GT5F)  
> - 학습 초기에 거친 레벨의 라벨 할당을 시작하고, 점진적으로 더 세밀한 라벨로 전환하여 모델 학습 효율을 높이는 기법입니다.  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> knowledge distillation methods  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=2HWJA3CD)

> <mark style="background-color: #ffd400">Highlight</mark>  
> The model re-parameterization technique can be regarded as an ensemble technique  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=LMZSFYDK)

> <mark style="background-color: #2ea8e5">Highlight</mark>  
> module-level ensemble and model-level ensemble.  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=RIDAJKN2)  
> - 모듈과 모델의 차이가 무엇인가?  


> <mark style="background-color: #ffd400">Highlight</mark>  
> scaling factors  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=UIZ9A6XV)

> <mark style="background-color: #2ea8e5">Highlight</mark>  
> Network architecture search  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=XSBPH48W)  
> - 복잡한 규칙을 세우지 않고도 스케일링 팩터를 자동으로 찾는 기법  


> <mark style="background-color: #2ea8e5">Highlight</mark>  
> compound scaling category  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=ZMTWHAZV)

> <mark style="background-color: #ffd400">Highlight</mark>  
> The reason for this is because most popular NAS architectures deal with scaling factors that are not very correlated.  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=LBYPFY3L)

> <mark style="background-color: #2ea8e5">Highlight</mark>  
> cardinality  
> [page 3](zotero://open-pdf/library/items/LZ8Q479X?page=3&annotation=XCC7FSHT)

> <mark style="background-color: #2ea8e5">Highlight</mark>  
> cardinality manner  
> [page 3](zotero://open-pdf/library/items/LZ8Q479X?page=3&annotation=LNCSTA8H)

