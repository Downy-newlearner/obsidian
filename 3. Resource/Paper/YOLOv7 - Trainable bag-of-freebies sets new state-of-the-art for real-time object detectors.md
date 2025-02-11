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
> <mark style="background-color: #ffd400">Highlight</mark>  
> strengthen the training cost for improving the accuracy of object detection  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=SPKPUYM9)

> <mark style="background-color: #ffd400">Highlight</mark>  
> trainable bag-of-freebies  
> [page 1](zotero://open-pdf/library/items/LZ8Q479X?page=1&annotation=Z6PL84CQ)

> <mark style="background-color: #2ea8e5">Highlight</mark>  
> model re-parameterization  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=USIWPK4T)

> <mark style="background-color: #2ea8e5">Highlight</mark>  
> dynamic label assignment  
> [page 2](zotero://open-pdf/library/items/LZ8Q479X?page=2&annotation=LMNR8BB7)

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

