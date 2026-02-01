## CNN 효율성 향상의 3가지 방법
### 1. Depth
- 의미: 네트워크의 레이어 수를 늘리는 것
- 연산 영향: 선형 증가
- 특징: 모델의 표현력을 높일 수 있지만, 깊어질수록 gradient vanishing/exploding 문제 발생 가능

### 2. Width
- 의미: 각 레이어의 채널 수를 늘리는 것
- 연산 영향: 이차 증가
- 특징: 특징 표현의 다양성이 증가하지만, 연산량이 빠르게 커짐

### 3. Resolution
- 의미: 입력 이미지의 크기를 키우는 것
- 연산 영향: 이차 증가
- 특징: 더 많은 공간 정보를 보존하지만 메모리 및 연산량 증가


- 단순히 하나의 축만 확장하면 연산량이 기하급수적으로 늘게 됨.
- 따라서 세 축을 균형있게 조절하는 것이 효율적인 모델 설계의 핵심

## FLOP이 무엇인가?
### 1. FLOP의 정의
- Floating Point Operation: 부동소수점 연산을 의미함
- 딥러닝에서 FLOP은 주로 모델의 계산 복잡도(연산량)를 정량적으로 평가하는 지표로 사용됨
- 곱셉이나 덧셈 각각 하나당 1FLOP으로 계산됨

## MobileNet 소개
### 1. MobileNet 개요
- 2017년 Google이 제안한 경량화 CNN 아키텍처
- 모바일 및 임베디드 비전 시스템에 최적화됨

### 2. 핵심 아이디어
- Depthwise Separable Convolution 사용
	- Depthwise Convolution: 각 채널에 대해 별도로 필터 적용(채널 독립적 연산)
	- Pointwise Convolution: 1x1 convolution으로 depthwise 결과를 결합
- 결과적으로 표준 컨볼루션 대비 약 8~9배 연산량 감소

### 3. 특징 및 활용
- MACs(연산량) 대비 높은 정확도(효율성)가 특징
- 실제 응용 예시: 얼굴 인식, 객체 탐지, 지리적 위치 추정 등


## FLOPs 비교: Standard vs Depthwise Separable
### 1. FLOPs 계산 요소
- $D_K$: 커널 크기 (예: 3 for 3x3)
- $M$: 입력 채널 수
- $N$: 출력 채널 수
- $D_F$: 입력 피처맵 공간 해상도
- $D_G$: 출력 피처맵 공간 해상도 (보통 $D_G ≈ D_F$)

### 2. Standard Convolution 연산량(FLOPs)
- 각 출력 채널은 모든 입력 채널을 동시에 보고, ==하나의 3D필터가 공간 + 채널 정보==를 통합해서 처리한다.


- 하나의 필터가 한 위치에서 수행하는 연산: 
	 $D_K^2 \times M$
    
- 전체 위치에서의 연산 (assuming $D_G = D_F$):
    $D_G^2 \times D_K^2 \times M$
    
- 전체 출력 채널 수 N만큼 반복:
    $\boxed{FLOPs_{standard} = D_G^2 \times D_K^2 \times M \times N}$

### 3. Depthwise Separable Convolution 연산량
#### Step 1: Depthwise Convolution
- 각 입력 채널에 하나의 필터만 적용 -> 총 M개의 필터
- 하나의 채널에 대한 연산:
	$$D_F^2 \times D_K^2$$
    
- 총 M개 채널에 대해:
    $$D_F^2 \times D_K^2 \times M$$

#### Step 2: Pointwise Convolution (1x1 conv)
- 각 $D_F \times D_F$ 위치마다 N개의 1x1 필터가 M채널에 적용됨

$$M \times N \times D_F^2$$


#### **총 FLOPs:**

$$\boxed{ FLOPs_{depthwise} = D_F^2 \times D_K^2 \times M + M \times N \times D_F^2 }$$


### 4. 효율성 비교(비율)
$$\frac{FLOPs_{depthwise}}{FLOPs_{standard}} = \frac{D_F^2 \cdot D_K^2 \cdot M + D_F^2 \cdot M \cdot N}{D_F^2 \cdot D_K^2 \cdot M \cdot N} = \frac{1}{N} + \frac{1}{D_K^2}$$


#### **예시:**

- $D_K = 3, N = 256$일 때:
$$    \frac{1}{256} + \frac{1}{9} \approx 0.115$$

- 즉, **계산량이 약 11.5% 수준** → 약 **9배의 계산량 절감**

## MobileNet Architecture
### 1. 아키텍처 구성
- 총 28개의 레이어로 구성
- 첫 번째 Conv 레이어를 제외한 모든 레이어에서 Depthwise Separable Convolution 사용

![[Pasted image 20251027095553.png|400]]

### 2. Width Multiplier
- MobileNet은 채널 수 조정을 통해 모델의 크기와 연산량을 조절할 수 있도록 Width Multiplier 도입
- a 값에 따라 각 레이어의 input/output 채널 수가 a배로 축소됨(0 < a <= 1)

효과:
- FLOPs 및 파라미터 수가 약 a^2 배로 감소
- 적은 연산량을 요구하는 환경에 적합
- 


- a가 줄어들수록 
	- 정확도는 감소하지만, 연산량과 파라미터 수는 크게 감소
- 리소스가 제한된 디바이스에 맞춰 효율적인 모델 크기 조정 가능