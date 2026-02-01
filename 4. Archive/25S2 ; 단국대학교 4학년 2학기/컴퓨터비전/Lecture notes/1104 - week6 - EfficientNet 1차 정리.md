Lecture materials: 2025-2_ComputerVision_week6(p.17-)

## SE Block
traditional convolutions's kernel is mixed up all feature like patterns and 질감 across channels.
==But, MBConv의 depthwise convolution은 채널별로 적용된다.==
	no interaction across channels -> 어떤 채널이 중요한, 덜 중요한 특징을 포함하고 있는지 알 수 있다.
	do not capture relationships between channels
	-> 그래서 SE 블록이 중요하다.(?) - 인과관계 확인하기

스퀴즈는 각 채널이 대표 값 하나로 축소되도록 한다. -> globally 얼마나 중요한지에 대한 값

**여기서의 Attention layer과 transformer의 attention 기법의 상관성(?)**


## EfficientNet의 Key components
1. ==MBConv==
	- Mobile Inverted Bottleneck Convolution(역병목 구조)
	- 네트워크의 핵심 연산 블록
	- MobileNetV2에서 처음 도입된 개념을 효율적으로 확장한 것이다.
2. ==SE block==
	- MBConv 안에 포함되어, 채널 간 중요도를 학습해서 "어떤 특징을 강조할지"를 결정하는 모듈이다.
	- 이 블록은 네트워크가 '무엇을 볼 것인가(What to focus on)'를 스스로 배우게 해준다.
3. ==Swish activation==


## MBConv(Mobile Inverted Bottleneck Convolution)

### MBConv의 구조와 역할
MBConv는 "Inverted Bottleneck"을 사용하여 적은 연산으로도 풍부한 표현력을 유지한다.

1. ==Expansion==(1x1 conv): 입력 채널 수를 먼저 확장시켜 더 많은 특성 추출 가능
	- 같은 공간 위치 (h,w)에서 모든 입력 채널을 선형 결합하여 새로운 채널 벡터를 만든다.
	- 채널 복제가 아니고 채널 혼합 + 재표현이다.
	- 진짜 역할은 "공간 연산을 하기 전에 특징을 더 풍부한 채널 공간으로 재배치하는 것"
2. ==Depthwise Convolution==(3x3): 각 채널별로 독립적으로 공간 특징 추출(연산량 크게 절감)
	- 일반 Conv는 공간 연산 + 채널 혼합을 동시에
	- Depthwise Conv는 공간 연산만
	- 채널 혼합은 나중에 1x1 Conv로 따로 처리
3. ==SE Block==(Squeeze & Excitation): 채널 간 중요도를 학습하여 정보 강조/억제
4. ==Projection==(투영, 1x1 conv): 채널 수를 다시 줄여 출력
5. ==Residual Connection==(optional): 입력과 출력이 같을 경우 skip 연결 -> gradient 흐름 개선

확장 -> 깊이별 합성곱 -> 채널 attention -> 축소

- 공간 특징 추출은 Depthwise Conv가 담당
- 특징 조합, 변환은 1x1 Conv가 담당

![[Pasted image 20251214221531.png|400]]

### 장점
- 연산 효율성: Depthwise separable convolution을 사용해 표준 합성곱 대비 약 8-9배 적은 FLOPs로 계산 가능
- 정보 손실 최소화: Expansion으로 풍부한 특징을 만들고 Projection으로 압축 -> 연산량 대비 정보 유지
- 채널 주의(SE): 중요한 채널에 가중치를 부여해 정확도 향상
- Residual 연결: 기울기 손실(gradient vanishing) 방지로 안정된 학습 가능

### Expansion
1×1 합성곱은 공간(spatial) 특징을 뽑는 게 아니라, “채널을 섞는(channel mixing) 연산” 
단, 물리적으로 각 채널을 서로 섞어서 뒤섞는다는 뜻이 아니라, 입력 채널들의 선형 결합(linear combination)을 통해 새로운 채널을 만든다는 뜻이다.

즉, 각 출력 채널은 모든 입력 채널의 값을 가중합(weighted sum) 으로 만드는 것이다.

같은 (h, w) 위치의 채널 벡터 $\mathbf{x}\in\mathbb{R}^{C_{\text{in}}}$에 같은 가중행렬 $W_e\in\mathbb{R}^{C_{\text{in}}\times (tC_{\text{in}})}$을 곱해서 $\mathbf{y}=\mathbf{x}W_e\in\mathbb{R}^{tC_{\text{in}}}$로 채널 차원만 확장하는 거지. 그래서 “1×1 공간의 특징”이라는 말은 부정확하고, 한 픽셀의 채널 조합을 바꾸는 선형변환이라고 이해하면 돼.

- MBConv의 Expansion(1×1) 단계: 채널을 $C\rightarrow tC$로 늘려 표현력을 키움
- 그 다음 Depthwise 3×3이 공간 필터링을 담당(채널별로 공간 특징 추출)
- 이후 SE, 그리고 Projection(1×1) 로 채널을 다시 줄임
    

즉, 1×1은 채널 섞기(선형 결합), 3×3 depthwise가 공간 특징이라는 역할 분담이 핵심이야. 슬라이드에도 depthwise/pointwise의 구분과 1×1이 채널을 섞는 단계임이 나와 있어.

그리고 MBConv가 실제로 “Expand → Depthwise → SE → Project(1×1)” 순서임도 명시돼 있어.

> 직관: 각 픽셀을 하나의 “채널 벡터”라고 보면, Expansion 1×1은 그 벡터 차원을 키우는 MLP 한 층과 같고, Projection 1×1은 차원을 줄이는 선형층과 같아. 공간은 건드리지 않아.

### EfficientNet에서 MBConv를 사용하는 이유
이 블록은 모바일, 임베디드 환경에서 효율성과 정확도를 모두 확보하기 위해 도입되었다.
EfficientNet은 MobileV2의 아이디어를 계승하되, 여기에 SE 블록과 Swish 활성함수를 결합해 더 높은 성능을 달성함.

| **항목** | **MobileNetV1**          | **MobileNetV2 (MBConv 도입)**  | **EfficientNet**                  |
| ------ | ------------------------ | ---------------------------- | --------------------------------- |
| 핵심 구조  | Depthwise Separable Conv | Inverted Bottleneck (MBConv) | MBConv + SE + Swish               |
| 채널 주의  | 없음                       | 없음                           | 있음 (SE block)                     |
| 활성 함수  | ReLU                     | ReLU6                        | Swish                             |
| 효율성    | 높음                       | 더 높음                         | 최고 수준 (Compound Scaling + MBConv) |

## SE Block
SE block은 채널 단위의 Attention 매커니즘으로, 
중요한 특징은 강조하고 불필요한 특징은 억제해 EfficientNet의 효율성과 정확도를 동시에 높이는 핵심 구성요소이다.


### SE Block의 구조
"Squeeze -> Excitation" 두 단계로 구성된다. (쭉 짜서(GAP) 요약 -> FC + Activation function으로 활성화)

| **단계**            | **연산**                                               | **역할**                                    |
| ----------------- | ---------------------------------------------------- | ----------------------------------------- |
| **Squeeze**       | 전역 평균 풀링(Global Average Pooling)                     | 한 채널의 전체 공간 정보를 하나의 값으로 요약 → 채널별 요약 벡터 생성 |
| **Excitation**    | 두 개의 FC(Fully Connected) Layer와 비선형 활성함수(Swish/ReLU) | 각 채널의 중요도를 학습 (0~1 사이의 가중치 생성)            |
| **Recalibration** | 채널별 가중치를 곱해 중요도 반영                                   | 중요한 채널은 강조하고, 덜 중요한 채널은 억제                |
"이미지의 모든 채널을 보고, 중요한 채널에는 불을 켜고 덜 중요한 채널은 어둡게 하는 과정"

### SE Block의 역할
- 기존 CNN은 공간적 패턴(픽셀 위치 관계)에는 강했지만, 채널간 관계(특징맵 간 상호작용)는 고려하지 못했다.
- SE block은 이 한계를 보완해 아래 효과를 얻는다.
1. 채널별 의존 관계 학습 -> 네트워크가 "어떤 특징이 더 중요한지"를 이해
2. 정보 재가중 -> 불필요한 특징을 억제하고 중요한 정보 강조
3. 성능 향상 -> 추가 파라미터는 적지만 Top-1 정확도 향상 (ResNet, EfficientNet 등에서 입증)

### 수식적 요약
1. **Squeeze:**
    $z_c = \frac{1}{H \times W} \sum_{i=1}^H \sum_{j=1}^W x_{c}(i, j)$
    → 채널 $c$의 평균값 $z_c$ 계산
    
2. **Excitation(활성화):**
	Excitation의 전체 과정을 Attention(채널별 중요도(가중치) 벡터를 만든는 과정)이라고도 부른다.
	FC + 활성함수 + 시그모이드가 포함된다.
	
    $s = \sigma(W_2 \cdot \delta(W_1 z))$ (SE Attention Machanism)
    
    - $W_1$, $W_2$: 두 개의 FC layer
	    - 첫 번째 FC는 채널 간 관계를 요약 및 차원 축소
	    - 두 번째 FC는 다시 원래 차원으로 확장
    - $\delta$: ReLU
	    - SE block의 기본 형태(SENet 방식, 2018)에서는 ReLU를 사용하고, EfficientNet(2019)에서는 ReLU대신 Swish를 사용한다.
    - $\sigma$: sigmoid (0~1로 정규화)
    
3. **Scale:**
    $\tilde{x}_c = s_c \cdot x_c$
    → 원래 특징맵 $x_c에$ 가중치 $s_c$ 곱하기

### EfficientNet에서의 장점
| **항목**      | **설명**                            |
| ----------- | --------------------------------- |
| **정확도 향상**  | 작은 모델에서도 채널 간 주의 덕분에 표현력 향상       |
| **연산량 효율적** | 추가되는 파라미터 수가 매우 적음                |
| **모듈화 쉬움**  | MBConv 블록 내부에 삽입되어 재사용 용이         |
| **결합 효과**   | Swish + SE 조합으로 더 부드럽고 안정적인 학습 가능 |
EfficientNet의 SE block은 모든 MBConv 뒤에 붙어있으며, 이 덕분에 모델은 "가벼우면서도 똑똑한 시각적 주의(attention)"를 얻게 된다.


## GAP: Global Average Pooling

### 어디에서 처음 쓰였을까?
ResNet에서 처음 주류로 채택되어, 이후 MobileNet, EfficientNet 등 대부분의 경량/현대 CNN에 기본적으로 사용됨.

### Average Pooling vs Max Pooling 비교
| **구분**      | **Average Pooling**                   | **Max Pooling**                       |
| ----------- | ------------------------------------- | ------------------------------------- |
| **동작 방식**   | 커널 영역의 평균값 계산                         | 커널 영역의 최댓값 선택                         |
| **특징 보존**   | 전체적인 패턴 유지 (평탄화)                      | 가장 강한 특징만 강조                          |
| **노이즈 민감도** | 노이즈에 덜 민감 (평균화 효과)                    | 노이즈에 민감 (한 점에 좌우됨)                    |
| **정보 손실**   | 정보 손실 적음 (부드럽게 유지)                    | 세부 정보 일부 손실 (과감하게 선택)                 |
| **활성 맵 성향** | 부드럽고 연속적인 feature map                 | 날카롭고 sparse한 feature map              |
| **적합한 경우**  | 전체적인 패턴 중요할 때 (object classification) | 국소적인 강한 특징 중요할 때 (object detection 등) |
- Max Pooling: “가장 눈에 띄는 특징” 강조
- Average Pooling: “전체적인 형태나 분포”를 반영

### EfficientNet에서 왜 Max Pooling 대신 Average Pooling을 썼을까?
EfficientNet은 classification (이미지 분류) 에 최적화된 모델

그래서 아래 이유로 Average Pooling을 사용함

1. GAP(Global Average Pooling)으로 부드러운 특징 요약
    
    → 전체 feature map의 평균을 내어 “전체 물체의 존재 확률”을 반영.
    → 특정 위치의 강한 activation에만 의존하지 않음.
    
1. Overfitting 감소
    
    → Max Pooling은 특정 강한 feature에 과도하게 반응할 수 있어서, 데이터 편향 가능성이 높음.
    → Average Pooling은 여러 위치의 정보를 골고루 반영해 일반화 성능이 좋음.
    
1. SE block과의 궁합
    
    → SE block의 Squeeze 단계에서 Global Average Pooling(GAP) 사용.
    → 이는 채널 전체를 요약해 “전체 문맥(Context)” 을 보는 역할.
    → 만약 Global Max Pooling을 쓰면, 한 점에 집중해서 문맥을 잃게 돼.
    


📍**결론:**
> EfficientNet은 물체 전체의 문맥(Context)을 반영하는 분류 모델이므로

> GAP(=Average Pooling 기반) 을 사용해 안정적이고 일반화된 특징 요약을 선택한 거야.