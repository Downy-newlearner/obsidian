---
created: 2024-11-04 00:57
tags:
  - Object_Detection
  - DETR
aliases:
  - DEtection TRansformer
reference: https://www.youtube.com/watch?v=hCWUTvVrG7E
---
데이터만 잘 주어진다면 end to end 방식으로 Detection을 하도록 해주는 것이 DETR의 가장 큰 contribution이다.
 





 

DETR(DEtection TRansformer)은 기존 객체 탐지 파이프라인에서 필요로 하는 수작업 컴포넌트인 [[Non-Maximum Suppression|NMS]](Non-Maximum Suppression)와 [[앵커]](anchor) 생성 과정을 제거하고, [[엔드-투-엔드 방식]]의 트랜스포머 구조를 사용해 객체 탐지를 set prediction 문제로 접근한다. 
	*이분 매칭(bipartite matching) 방식*을 사용하여 이를 가능하게 만들었다.

주요 특징으로는 encoder-decoder 구조의 트랜스포머를 통해 중복된 예측을 제거하며, COCO 데이터셋에서 Faster R-CNN과 유사한 성능을 보인다. Large object에 강점을 보이나, small object에 대한 성능은 낮아 FPN 적용을 계획 중이다.


![[Pasted image 20241111135713.png]]
**기존 디텍션**
이미지에 잔뜩 앵커박스를 치고, Ground truth와 비교했을 떄 가장 신뢰도가 높은 앵커박스만 NMS 방식을 사용해서 남긴다.

![[Pasted image 20241111135825.png]]
**DETR**
오로지 DETR만을 사용하여 디텍션을 진행한다.

## Loss: Bounding Box Loss
![[Pasted image 20241111141923.png]]
### 1. 클래스 예측: $\hat{p}_{\sigma(i)}(c_i)$
### 2. 박스 좌표 예측 $L_{box}$
![[Pasted image 20241111140252.png]]
- 일반적인 detector에서의 bounding box loss는 예측과 ground truth 간의 _상대적인 좌표 및 크기_ 를 이용하여 정의한다.
	- Anchor에서 정의된 box를 얼마나 움직이고, 얼마나 키워야 ground truth에 가까워지는지를 확인한다.
- 반면 DETR의 경우 절대적인 bounding box의 좌표 및 크기를 direct 하게 예측하므로 loss를 계산 시 일반적인 L1 loss 외에 scale 보정이 필요함 -> [[GIoU]] 사용

## Model Architecture


## Training Process

이분 매칭


## Experiment
![[Pasted image 20241111143443.png]]
**[[AP]] (Average Precision)**:  
객체 탐지 모델의 정확도를 평가하는 지표로, 다양한 임계값에서의 **Precision-Recall 곡선** 아래의 면적을 계산하여 평균을 낸 값이다.  

**핵심 디테일**:  
AP는 IoU 임계값을 여러 개 설정하여 모든 객체의 탐지 성능을 종합적으로 평가한다. 주로 COCO 데이터셋에서 평가 시 다양한 IoU 임계값 (예: 0.50에서 0.95까지)을 기준으로 AP를 구한다.

**요약**:  
모든 IoU 임계값에서의 평균 Precision-Recall 곡선 아래 면적으로 객체 탐지 모델의 정확도를 평가한다.

---



**DETR(Detection Transformer)의 문제점:**

1. 느린 학습 속도와 낮은 수렴 속도:
    - DETR은 기존 객체 탐지 모델에 비해 학습 시간이 훨씬 오래 걸립니다.
    - 수렴 문제가 발생하여 합리적인 시간 내에 최적의 성능을 달성하기 어려운 경우가 있습니다.
    
2. 희소한 긍정 신호(sparse positive signal):
    - 학습 데이터에서 긍정적인(관련된) 신호의 분포가 희소하여 효과적으로 학습하기 어렵습니다.
    - 이로 인해 중요한 특징이나 객체를 식별하는 데 비효율성이 발생할 수 있습니다.