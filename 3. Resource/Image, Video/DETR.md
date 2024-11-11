---
created: 2024-11-04 00:57
tags:
  - Object_Detection
  - DETR
aliases:
  - DEtection TRansformer
---
이 블로그 게시물은 DETR (DEtection TRansformer)에 대해 설명한다. DETR은 기존 객체 탐지 파이프라인에서 필요로 하는 수작업 컴포넌트인 [[Non-Maximum Suppression|NMS]](Non-Maximum Suppression)와 [[앵커]](anchor) 생성 과정을 제거하고, [[엔드-투-엔드 방식]]의 트랜스포머 구조를 사용해 객체 탐지를 set prediction 문제로 접근한다. 주요 특징으로는 encoder-decoder 구조의 트랜스포머를 통해 중복된 예측을 제거하며, COCO 데이터셋에서 Faster R-CNN과 유사한 성능을 보인다. Large object에 강점을 보이나, small object에 대한 성능은 낮아 FPN 적용을 계획 중이다.



![[Pasted image 20241111135713.png]]
**기존 디텍션**
이미지에 잔뜩 앵커박스를 치고, Ground truth와 비교했을 떄 가장 신뢰도가 높은 앵커박스만 NMS 방식을 사용해서 남긴다.

![[Pasted image 20241111135825.png]]
**DETR**
오로지 DETR만을 사용하여 디텍션을 진행한다.

## Loss: Bounding Box Loss
![[Pasted image 20241111140252.png]]
- 일반적인 detector에서의 bounding box loss는 예측과 ground truth 간의 _상대적인 좌표 및 크기_ 를 이용하여 정의한다.
	- Anchor에서 정의된 box를 얼마나 움직이고, 얼마나 키워야 ground truth에 가까워지는지를 확인한다.
- 반면 DETR의 경우 절대적인 bounding box의 좌표 및 크기를 direct 하게 예측하므로 loss를 계산 시 일반적인 L1 loss 외에 scale 보정이 필요함 -> [[GIoU]] 사용