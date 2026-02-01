## 깊은 네트워크의 한계 및 챌린지
- 깊은 네트워크는 좋은 성능을 약속할 것만 같았지만 그렇지만은 않았다.

1. Vanishing/Exploding Gradients
	- 딥러닝에서 역전파를 통해 가중치를 업데이트 할 때, gradient가 점점 작아져서 사라지거나(vanishing), 너무 커져서 폭발하는(exploding) 문제가 생길 수 있다.
	- Gradient가 너무 작아지면 앞쪽 레이어들은 학습이 거의 되지 않고, 너무 커지면 가중치가 불안정하게 크게 변하면서 학습이 망가진다.
	- 이로 인해 네트워크는 학습이 매우 느려지거나, 아예 멈춰버리는 문제가 발생할 수 있다.

2. Saturation of Accuracy
	- 층을 더 많이 쌓을수록 훈련 오류(training error) 자체가 높아지는 경우가 있다. 즉, 단순히 테스트 오류 뿐만 아니라 학습 자체가 어려워지는 것이다.
	- 이 현상은 "degradation problem(성능 저하 문제)"로 알려져있다. 모델이 너무 깊어지면 오히려 정확도가 떨어질 수 있다.(최적화 실패, optimization failure)

3. Intuition(직관)
	- 우리의 직관대로라면, 얕은 네트워크보다 깊은 네트워크가 더 나은 성능을 내야할 것 같지만, 층을 많이 추가한, 일반적인 네트워크(plain network)는 오히려 더 나쁜 성능을 보인다.
	- 이는 깊은 네트워크가 단순히 더 많은 표현력을 가진다고 해서 항상 더 좋은 성능을 보장하지 않는다는 중요한 교훈을 보여준다.

## Degradation Problem을 이해하기
- 얕은 네트워크가 이미 잘 학습되었다고 가정할 때, 해당 네트워크의 복사본을 만들고, 그 위에 identity mapping(출력 = 입력)만 수행하는 레이어를 이어 덧붙이면 더 깊은 네트워크를 쉽게 만들 수 있다.
- 이론적으로는 이렇게 만든 네트워크가 얕은 네트워크보다 나쁠 이유가 없다. 적어도 같은 성능을 내야한다.

하지만 실제로는:
- 성능이 오히려 떨어진다. 이는 오버피팅이나 그래디언트 소실 문제가 아니라, SGD가 Identity mapping을 제대로 학습하지 못하기 때문이다.
- 깊은 네트워크가 단순히 입력을 그대로 통과시키는 것 같은 "trivial"한 작업조차 학습하지 못할 수 있다. 비선형 활성화 함수들 때문에 신호가 왜곡되기 때문이다.
- ==문제는 깊이 자체가 아니라, 깊은 비선형 네트워크가 identity mapping을 학습하기 어렵다는 점이다.==
	- SGD는 랜덤 초기화된, 비선형 함수가 많은 깊은 네트워크에서 '그냥 입력을 그대로 복사하는 것'조차 학습하기 힘들다. 이는 네트워크 구조 자체가 identity를 가정하지 않으며, SGD가 그런 해를 잘 찾지 못하기 때문이다.


## 매핑 학습에서 잔차 학습으로의 전환
- 매핑 학습이란 전체 함수를 학습하는 방식이다.
- 입력과 출력 사이의 전체 매핑을 학습하는 대신, 입력에서 얼마나 보정해야 하는지를 학습하도록 문제를 재구성한 방식이다.
- 기존의 $H(x)$를 직접 학습하는 방식에서, 이미 알고 있는 $x$를 기준으로 "얼마나 바꿔야 하는가?" 즉, $F(x) = H(x) - x$를 학습하며, 최종 출력은 $F(x) + x$로 구성하는 방식으로 한다.
- 이러한 방식은 수치 최적화에서의 preconditioning(사전조건화) 개념과 유사하다. 즉, 문제를 재구성하여 학습 알고리즘이 더 쉽게 수렴하도록 만드는 것이다.

### 잔차 학습의 직관적 이해
- 잔차 함수 $F(x)$는 입력값에 대한 작은 보정(delta)이라고 생각할 수 있다. 입력과 정답이 거의 비슷한 경우, 네트워크는 단순히 그 차이만 학습하면 된다.
- Skip connection은 입력을 그대로 다음 블록으로 전달하는 "기본 경로(default path)"역할을 하며, 네트워크가 굳이 불필요한 변환을 학습할 필요를 없앤다.
- 만약 입력이 거의 정답에 가깝다면 $F(x)$는 작은 보정만 수행하고, 큰 변화가 필요한 경우에는 $F(x)$가 더 복잡한 변환을 담당하게 된다. 이 구조는 네트워크가 상황에 따라 학습 난이도를 조절할 수 있게 한다.(어떤 경우에서든 기존 네트워크보다 상대적으로 효율적인 경로로 학습이 가능하다.)

### Residual Learning의 의의
- 깊은 네트워크는 이론적으로 강력하지만, 실제로는 Degradation Problem이 발생하여 최적화가 어렵다는 문제가 있었다.(Gradient 소실, 학습 불안정, 훈련 오류 증가) 이러한 현상은 BatchNorm 등의 보정 기법을 쓰더라도 해결되지 않았다.
- Residual Learning은 이러한 문제를 해결하기 위해 skip connection을 도입하여 gradient가 앞쪽까지 직접 전달될 수 있도록 경로를 제공하여 막힘없이 흐르도록 하였고, identity mapping을 쉽게 학습할 수 있도록 만들어 optimizer의 수렴을 더욱 쉽게 했다.
- 이 구조는 ResNet, ResNeXt, Faster R-CNN, Mask R-CNN 등 다양한 최신 비전 모델의 핵심 기반이 되었으며, 100층이 넘는 초심층 네트워크도 안정적으로 학습할 수 있게 했다.

## ResNet 소개
### High-level overview
#### 1. Initial layer
- 입력 이미지는 먼저 7x7 크기의 필터와 stride 2를 사용하는 컨볼루션 층을 거치며, 이는 큰 영역의 특징을 빠르게 요약하고 해상도를 절반으로 줄인다.
- 그 뒤 3x3 크기의 Max Pooling이 적용되어 주요 특징만 남기고 공간적 크기를 한 번 더 축소한다.
#### 2. Four Stages of Residual Blocks
- 이후 네 개의 Residual Block Stage로 구성되어 있으며, 각각의 스테이지는 Conv2_x, Conv3_x, Conv4_x, Conv5_x로 구분된다.
- 스테이지가 진행될수록 공간 해상도는 절반으로 줄어들고, 채널 수는 두배로 증가한다.
- 예를 들어, Conv2_x의 출력 채널 수가 64라면 그 다음은 128, 그 다음은 256, 그 다음은 512가 된다.
- 대부분의 합성곱 연산은 이 Residual Block 내부에서 수행되며, 네트워크의 깊이는 이 블록의 개수에 따라 결정된다. 예를 들어 ResNet-50은 대부분의 층이 이 블록 안에 포함된다.

#### 3. Global Average Pooling(GAP)
- 마지막 Residual Block의 출력을 전역 평균 풀링(GAP)으로 요약하여, 2D feature map을 1D 벡터 형태로 변환한다.
- 이는 전체 공간의 정보를 하나의 대표값으로 집약함으로써 파라미터 수를 줄이고 과적합을 방지한다.

#### 4. Fully Connected layer + Softmax
- GAP 결과는 완전연결층(FC)으로 전달되어 각 클래스에 대한 점수를 계산하며, 마지막 Softmax를 통해 최종 분류 확률을 출력한다.

### 아키텍처 안에는 뭐가 있을까?
#### 1. Residual Block
- 잔차 학습의 기본 단위로, 네트워크는 전체 함수 $H(x)$를 직접 학습하는 대신 $F(x) = H(x) -x$를 학습하고, 최종 출력은 $F(x) + x$로 구성된다.
- 이는 학습 난이도를 줄이고, gradient가 잘 흐르도록 해줌으로써 깊은 네트워크에서도 안정적인 학습이 가능하다.

#### 2. Skip Connection
- 입력 $x$를 다음 층으로 직접 전달하는 경로로, identity mapping 또는 projection mapping 방식이 사용된다.
- 이 연결 덕분에 gradient가 소실되지 않고 초깃값까지 잘 도달할 수 있으며, 학습 중 정보 손실을 줄여준다.

#### 3. Bottleneck Block
- 3개의 Convolution으로 구성된 블록으로, 순서대로 1x1 -> 3x3 -> 1x1 convolution이 사용된다.
- 첫 번째 1x1 conv는 차원을 줄이고, 두 번째, 3x3 conv에서 실제 연산을 수행하며, 마지막 1x1 conv로 차원을 복원한다.
- 연산량을 줄이면서도 깊은 네트워크 구성이 가능하도록 효율을 높인 구조이다.

#### 4. BatchNorm + ReLU
- 각 convolution 연산 후에는 항상 Batch Normalization과 ReLU가 따라붙는다.
- BatchNorm은 내부 covariate shift를 줄여 학습을 빠르고 안정적으로 만들어주고, ReLU는 비선형성을 부여하여 모델의 표현력을 향상시킨다.


- 이 구성 요소들은 모두 초심층 신경망이 안정적으로 학습되기 위한 구조적 장치들로 설계된 것이다.

## Residual Block 소개
### 1. Residual Block이란?
- Residual Block은 ResNet의 핵심 구성 단위로, deep network에서 layer를 더 쌓을수록 오히려 성능이 나빠지는 degradation problem을 해결하기 위해 설계되었다.
- 기존 방식은 전체 함수 $H(x)$를 직접 학습하려고 했지만, Residual Block은 $F(x) = H(x) - x$라는 잔차 함수를 학습하고, 이를 $H(x) = F(x) + x$로 재구성한다.
- 이렇게 하면 네트워크는 전체 변환이 아닌 "차이"만 학습하면 되므로 학습이 쉬워지고 안정적이다.

### 2. Residual Block의 기본 구조
$$y = F(x, \{W_i\}) + x$$
-  $x$: 입력 feature map
- $F(x, \{W_i\})$: 2~3개의 convolution으로 구성된 잔차 함수
- $y$: 출력 feature map

- 핵심 개념은 전체 변환이 아니라 변화해야 할 부분만 선택적으로 학습하게 만든다는 점이다.

### 3. 입력을 다시 더하는 이유
- 이 방식은 두 가지 장점을 갖는다.

#### 1. 변화에만 집중
- 네트워크는 입력과 출력의 차이만 학습하면 되므로, 불필요한 연산을 피하고 최적화를 쉽게 한다.
- 특히 깊은 네트워크에서 효과적이다.
- ResNet이라는 이름도 여기서 유래되었다.
	- Residual = $H(x) - x$
	- 네트워크는 이 잔차를 줄이는 것을 학습한다.

#### 2. 수렴 안정성 향상
- 학습이 잘 되어갈수록 출력 $H(x)$는 입력 $x$와 가까워지고, 따라서 $F(x) -> 0$이 된다.
- 이는 학습을 안정화시키고, 필요한 최소한의 업데이트만 수행하게 도와준다.

#### 3. 구현의 단순함
- 구조 변경 없이 입력과 출력을 shortcut으로 연결하는 방식이기 때문에 간단하게 적용 가능하다.
- 추가 파라미터도 없으며, 연산량 또한 거의 증가하지 않는다.
- 결과적으로 Residual Block은 성능과 구현 효율성 모두를 만족시키는 구조이다.

## Skip(Shortcut) Connection 소개
### 1. Skip Connection의 개념
- Skip Connection(또는 Shortcut Connection)은 입력을 중간 연산 과정을 거치지 않고 다음 블록으로 직접 전달하는 연결 구조를 말한다.
- 이 연결은 gradient가 소실되지 않고 앞쪽 레이어까지 잘 전달되도록 하는 핵심 역할을 하며, Residual Block의 안정적인 학습을 가능하게 한다.

### 2. 1x1 Convolution의 개념
- 1x1 convolution은 커널의 공간 크기가 1x1인 합성곱 연산으로, 입력의 공간 크기($W*H$)는 유지하면서 채널 수($D$)만 조정한다.
- 즉, 입력의 모든 픽셀 위치마다 채널 방향으로 가중합을 계산하여 특징의 조합이나 압축, 확장을 수행한다.

### 3. 1x1 Convolution의 주요 목적

| 목적                | 설명                                                             |
| ----------------- | -------------------------------------------------------------- |
| 채널 조정             | 공간 크기는 그대로 두면서 채널 수를 늘리거나 줄인다.                                 |
| 계산 효율 향상          | 연산량이 많은 3x3이나 5x5 conv 이전에 채널 수를 줄여 전체 계산량을 줄인다.               |
| 비선형성 추가           | ReLU와 함께 사용하면 모델의 표현력이 향상된다.                                   |
| Bottleneck 설계의 핵심 | ResNet의 Bottleneck Block(1x1 -> 3x3 -> 1x1)에서 차원 축소와 복원을 담당한다. |

### 4. 1x1 Convolution의 연산 효율 예시
- 직접 5×5 convolution을 사용하는 경우:
    
    $28 \times 28 \times 32 \times 5 \times 5 \times 192 \approx 120M \text{ operations}$
    
- 1×1 conv로 먼저 채널을 192 → 16으로 줄인 뒤 5×5 convolution 수행 시:
    
    $(28 \times 28 \times 16 \times 1 \times 1 \times 192) + (28 \times 28 \times 32 \times 5 \times 5 \times 16) \approx 12.4M$
    
- 즉, 약 10배 이상 계산량 절감이 가능하며, 이는 ResNet이 깊으면서도 계산 효율을 유지할 수 있는 이유이다.

### 5. Skip Connection의 종류
- 입력과 출력의 차원이 다를 때는 두 가지 방식으로 차원을 맞춘다.
	1. Identity Mapping with Padding
	2. Projection Mapping


## Bottleneck Block 소개
### Residual Block의 두 가지 종류
- ResNet에서는 네트워크 깊이에 따라 서로 다른 구조의 Residual Block을 사용한다.

### 1. Basic Residual Block (ResNet-18, ResNet-34에서 사용)
- 구조: 2개의 3x3 convolution으로 구성
- Shortcut 연결:
	- ==대부분 Identity Mapping을 사용==
	- 하지만 아래 조건에서는 Projection Mapping(1x1 conv)을 사용해야함:
		- 채널 수가 달라질 때
		- Spatial resolution이 줄어들 때. 예를 들어 stride가 2일 때.

### 2. Bottleneck Block (ResNet-50, 101, 152에서 사용)
 - 구조: 1x1 -> 3x3 -> 1x1 convolution으로 구성된 3-layer block
 - Shortcut 연결:
	 - ==대부분 Projection Mapping을 사용함==
	 - 이유:
		 - Bottleneck 구조는 내부적으로 차원을 축소했다가 복원하는 과정이 포함되어 있어, 입력과 출력의 크기가 자주 다름
		 - 또한 downsampling(stride=2)이 정기적으로 발생


요약
- Basic Block 단순하고 얕은 네트워크에 적합, Bottleneck Block은 깊고 복잡한 네트워크에서도 계산 효율을 유지할 수 있도록 설계됨.
- Bottleneck 구조는 차원을 줄였다가 다시 복원하면서 계산량은 줄이고 표현력은 유지한다.
- Shortcut은 구조에 따라 identity 또는 projection 방식으로 결정된다.

## ResNet에서 Gradient Vanishing이 발생하지 않는 이유

$$\frac{\partial L}{\partial x_1} = \frac{\partial L}{\partial x_L} \cdot \left( 1 + \frac{\partial}{\partial x_1} \sum_{i=1}^{L-1} F(x_i, W_i) \right)$$

- 위 수식은 ResNet에서 출력층으로부터 첫 번째 레이어까지 gradient가 얼마나 잘 전달되는지를 나타내는 계수이다.
- 일반적인 deep network에서는 이 값이 점점 작아지면서 곱해지는 gradient가 0에 가까워지기 때문에 gradient vanishing이 발생한다.

- 여기서 1이 매우 중요하다.
- 덧셈 항이라서, 아무리 $\frac{\partial}{\partial x_1} \sum_{i=1}^{L-1} F(x_i, W_i) )$가 작거나 -1에 가까워져도, 전체 값이 완전이 0이 되지 않는다.
- 다시 말해, 완전한 gradient 소실이 구조적으로 차단된다.

- 물론 ReLU는 forward에서 0이면, 역전파 시 gradient도 0이 되긴 한다.
	- 하지만 지금 이야기하는 건 ReLU의 출력이 0이 되어서 gradient가 끊기는 경우가 아니라, gradient 자체가 사라지거나 폭발하는 현상을 다루고 있는 것이다.
	- ReLU 얘기는 다른 맥락의 gradient vanishing이다.

## Batch Normalization
### 1. Batch Normalization이란?
- BN은 각 층의 입력 분포를 정규화하여 학습을 안정화시키고, 네트워크가 더 빠르고 효율적으로 학습되도록 돕는 기법이다.
- 학습 과정에서 입력 분포가 계속 변하지 않도록 제어하여, deep network의 불안정한 gradient 흐름을 완화한다.

### 2. 왜 필요한가?
- 딥러닝 모델은 다음 두 가지 문제로 인해 학습이 불안정해진다.

#### 1. Gradient Vanishing / Exploding
- 깊은 네트워크에서 역전파 중 gradient가 너무 작아지거나 커지면 학습이 제대로 이루어지지 않는다.

####  2. Internal Covariate Shift
- 학습 도중 이전 레이어의 파라미터가 변함에 따라 각 레이어의 입력 분포가 계속 바뀌는 현상.
- 이로 인해 학습 속도가 느려지고, 최적화가 어려워진다.

### 3. Gradient 문제와 BN의 역할
- 일반적인 해결책으로는 ReLU 사용, 초기화 조정, learning rate 축소 등이 있었지만 이는 임시방편 수준이었다.
- BN은 학습 과정 전체를 안정화시키는 근본적인 해결책으로 작용한다.
- 각 레이어의 입력을 정규화하여 입력 분포를 일정하게 유지하고, 학습이 초기값에 덜 민감해지고, gradient 흐름이 일정하게 유지되어 학습이 빠르고 안정적으로 진행된다.

### 4. BN의 학습 안정화 효과
- 입력 정규화 효과
	- 입력 데이터의 분포가 일정하게 유지되어 gradient가 안정적으로 흐른다.
- 학습 속도 향상
	- 활성화 값이 너무 크거나 작지 않게 조정되어, 최적화가 빠르게 수렴한다.
- 손실 곡면 평탄화 효과(Reshape the loss surface)
	- Normalization을 통해 손실 곡면(loss function)이 부드럽고 완만해져, Optimizer가 local minima에 빠질 확률이 줄어든다.
	- 결과적으로, global optimum에 더 쉽게 도달할 수 있다.

### 5. Internal Covariate Shift
- Covariate Shift: 입력 데이터 분포가 외부 요인(데이터셋 변경)에 의해 변하는 형상
- Internal Covariate Shift: 학습 중 이전 레이어의 파라미터 변화로 인해 각 레이어의 입력 분포가 계속 변하는 현상
- BN은 각 미니배치 단위로 입력을 정규화하여 이 변화를 줄이고, 학습이 훨씬 빠르고 안정적으로 진행되도록 만든다.

### 정리
Batch Normalization은 단순히 normalization 기법이 아니라,
- gradient 소실과 폭발을 방지하고,
- 내부 분포의 변화를 완화하며,
- loss surface를 평탄화하여 딥러닝의 학습 안정성을 획기적으로 높이는 핵심 요소이다.