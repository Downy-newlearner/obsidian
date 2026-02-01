
# Segmentation, Detection Introduction
## 공간 정보와 지역성을 보존하는 방법

### CNN의 공간 정보/지역성 관련 문제점
- Pooling & Stride in CNN -> downsampling -> 지역 해상도 저하
- CNN은 Translation invariance가 존재
	- Segmentation, Detection에서는 "무엇인지"뿐 아니라 "어디 있는지"가 반드시 필요한 정보인데 위치 정보에 둔감해지는 CNN의 특징인 TI는 "어디 있는지"에 대한 정보를 완전히 뭉개버린다.
		- Pooling -> 위치 정보 일부 삭제
		- Deep layer -> global, abstract features
		- fully connected layer -> 공간 정보 완전 제거
	- TI는 Classification에는 좋지만, Segmentation, detection에서는 최악임.
	- Detection은 Translation Variance가 필요하다.

Spatial information과 locality를 보존하기 위해 FCN과 U-Net처럼 **Encoder-Decoder** 구조와 **Skip connection**을 사용한다.

### 공간 정보와 지역성
![[Pasted image 20251210202324.png|400]]
![[Pasted image 20251210202334.png|400]]
- 공간 정보: 이미지에서 features의 절대적 위치
- 지역성: 지역에서의 특징의 상대적 arrangement

### 해결책 1: Encoder-Decoder Structure
p. 16
- Encoder
	- Convolutions + pooling으로 high-level semantic 특징 추출
	- Spatial dimensions 줄임 ($W*H -> w * h$)

- Decoder
	- upsampling을 사용해서 피처맵을 원본 사이즈로 복원($w * h -> W*H$)
	- segmentation map 생성

- Problem in Simple Encoder-Decoder
	- encoder로부터 발생한 high-level 특징은 low-level 디테일이 부족하다.
	- upsampling만으로는 정확한 바운더리 재구조화가 힘들다.

### 해결책 2: Skip Connection

- 인코더 레이어와 그에 상응하는 디코더 레이어를 직접 연결한다.
- low-level 공간 디테일과 high-level semantics를 merge한다.

- 장점
	- low-level 디테일 유지
	- spatial resolution 보존
	- 정확한 segmentation을 위해 locality와 semantic context 결합


---

p.18
## Fully **Convolutional** Networks for Sementic Segmentation
### 목표
- 이미지의 모든 픽셀에 class label을 할당
- end-to-end learning
- semantic meaning과 spatial precision간의 균형 유지

### Key idea
- 공간 정보를 보존하기 위해 FC(Fully Connected) layers -> fully convolution layers 대체

### Key Insights


### Core Steps
1. Convolutionalization
2. Upsampling
	- Coarse(global) feature map -> dense, high-resolution predictions
3. Skip Architecture
	- 정확한 바운더리를 위해 깊고, 글로벌하고, semantic한 features를 얕고, fine하고, appearance features와 융합한다.

## 왜 Segmentation에서 Fully Connected Layers는 대체되었을까?
### 문제점 with Fully **Connected** Layers
#### 1.  공간 정보를 잃는다.
- FC layers는 feature maps를 flatten하므로 픽셀의 location data를 버린다.
- 중요한 공간 정보 대응(무엇이 어디에 있는지)을 잃는다.

#### 2. FC layers는 고정된 입력 사이즈 제한이 있다.
- 고정된 입력 사이즈 제한으로 인해 이미지 사이즈의 다양성과 유연성에 한계가 생긴다.

#### 3. Coarse Outputs for Dense Prediction
- 아웃풋이 ==하나의 이미지에 대해 하나의 클래스==이다.
	- Single class for whole image, not per-pixel

#### 요약: Fully Connected layers가 Segmentation에 문제가 되는 이유
- Semantic segmentation은 밀도있고, pixel-to-pixel 예측이 필요하다.
- Semantic segmentation은 ==semantic meaning과 location information== 둘 다 필요하다.
- FC Layers는 공간 정보를 파괴한다.

### FC -> Conv 변환(Convolutionalization)
- FC layers를 동등한 convolutional layers로 대체한다.

- 장점
	- 임의의 입력 사이즈를 허용한다.
	- 공간 정보를 담고있는 공간적 output maps를 제공한다.
	- end-to-end pixel-level learning이 가능해진다.

#### Example: FC -> Conv 대체



## Segmentation에서 Upsampling이 필수인 이유
### 1. Downsampling in CNNs
- 공간 해상도를 점진적으로 감소시킨다.
- 원본 이미지의 모든 픽셀들의 공간 정보는 보존된다.

### 2. The Problem for Segmentation
- 각 픽셀들의 공간 정보를 보존하긴 하지만, 여전히 해상도가 너무 coarse하다.

## Coarse to Dense: Deconvolution Layers
p. 27
### 1. Upsampling Methods


### 2. Backwards Convolution Concept

==이게 뭐지???==

지금까지 배운(뭘 배웠나? - 분류?) 내용과 Segmentation의 다른 점 -> Standard CNN 아키텍처는 왜 Segmentation에 실패했나? - 

33-47페이지 U-Net











# FCN

[[Week7 - FCN 대비 문제]]


# U-Net

[[Week7 - U-Net 대비 문제]]

## 용어 정리
### Valid convolution

#### 1. valid conv = 패딩 없는 conv와 "완전 동일한 의미"
valid conv는 padding= 0 이고 kernel 크기만큼 feature map 크기가 줄어드는 일반 conv이다.

#### 2. 그럼 왜 U-Net은 Valid conv를 사용했을까?

1. 더 정확한 특징 추출
2. 원본보다 작은 영역만 예측하게 만들어 정확도 향상

-> 성능을 위해 Valid conv를 사용했음

#### 3. valid conv -> crop 필요가 생기는 이유
![[Pasted image 20251211185550.png]]

### Overlap-Tile

Overlap-tile strategy는 다음 문제를 해결하는 전략이다.
- valid conv를 사용하면 출력이 입력보다 항상 작아진다.
- 큰 이미지를 타일로 나눠서 처리할 때 타일 경계 부분의 context(주변 정보)가 사라지는 문제가 발생한다.

그래서,
타일을 겹치게해서 잘라 입력 -> 출력은 중심 부분만 사용으로 경계 정보 부족을 해결한다.


### Mirroring Extrapolation
![[Pasted image 20251211200903.png|400]]
![[Pasted image 20251211200647.png]]

#### Zero-padding 대신 Mirroring Extrapolation을 하는 이유.
- zero-padding을 하면 원본 이미지에 존재하지 않는 검은 테두리가 생긴다.
- 네트워크는 이걸 진짜 패턴으로 학습해버림
- 특히 U-Net처럼 픽셀 단위 예측이 중요한 segmentation에서는 경계 예측이 망가짐

- 하지만 Mirroring을 하면 자연스러운 경계가 만들어짐
- 모델이 진짜 이미지와 유사한 문맥을 입력받음
- 경계 영역에서 feature map이 안정적으로 계산됨
- segmentation mask 경계가 훨씬 부드럽고 정확해짐

### Weighted Loss



