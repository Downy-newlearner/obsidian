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

**AP$_{50}$**:  
IoU 임계값을 **0.50**으로 고정한 상태에서의 **AP**로, 비교적 낮은 임계값에서 객체 탐지 성능을 평가한다.

**핵심 디테일**:  
AP$_{50}$은 더 넓은 탐지 범위를 허용하여 모델의 검출력(Recall)을 평가하는 데 중점을 둔다.

**요약**:  
IoU 임계값 0.50에서 모델의 검출 성능을 평가하는 지표이다.

---

**AP$_{75}$**:  
IoU 임계값을 **0.75**로 고정한 상태에서의 **AP**로, 더 높은 정밀도를 요구하는 지표이다.

**핵심 디테일**:  
AP$_{75}$는 높은 IoU 임계값에서 측정되므로, 예측 상자와 실제 상자가 정확히 맞아떨어지는 경우에만 높은 점수를 부여하여 모델의 정밀도(Precision)를 평가한다.

**요약**:  
IoU 임계값 0.75에서 모델의 정밀도를 평가하는 지표이다.

---

**AP$_S$ (AP for Small objects)**:  
작은 객체(small objects)에 대한 평균 정밀도를 나타내며, 소형 객체에서의 모델 성능을 평가한다.

**핵심 디테일**:  
객체 크기가 작은 경우 탐지가 어려워지므로, AP$_S$는 모델이 작은 객체를 얼마나 잘 탐지하는지를 보여준다.

**요약**:  
작은 객체에 대한 모델의 탐지 성능을 평가하는 지표이다.

---

**AP$_M$ (AP for Medium objects)**:  
중간 크기의 객체(medium objects)에 대한 평균 정밀도를 나타내며, 중형 객체에서의 모델 성능을 평가한다.

**핵심 디테일**:  
중간 크기의 객체에 대해 모델의 탐지 성능을 확인하여, 특정 크기에서의 성능을 구체적으로 파악한다.

**요약**:  
중간 크기의 객체에 대한 모델의 탐지 성능을 평가하는 지표이다.

---

**AP$_L$ (AP for Large objects)**:  
큰 객체(large objects)에 대한 평균 정밀도를 나타내며, 대형 객체에서의 모델 성능을 평가한다.

**핵심 디테일**:  
크기가 큰 객체에 대해 모델의 탐지 성능을 측정하여, 대형 객체에서의 성능 강점을 평가한다.

**요약**:  
큰 객체에 대한 모델의 탐지 성능을 평가하는 지표이다.