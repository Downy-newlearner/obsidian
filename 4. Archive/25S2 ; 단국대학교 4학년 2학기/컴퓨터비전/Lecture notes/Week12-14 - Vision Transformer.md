자료에서는 ViT encoder를 어떻게 이미지에 적용하는지 설명하기 위해 classification을 예로 든다.
	ViT에 Classification Head(MLP Head)를 달아서 분류가 가능해지는 것이다.
자료에서 설명하는 ViT는 encoder-only 구조이며, decoder는 포함되지 않는다.

## 1. 왜 Vision Transformer를 배워야 하는가? (CNN의 한계)

CNN은 지역성(locality) 과 translation equivariance 같은 강한 [[inductive bias(귀납적 편향, 모델이 일반화를 하기 위해 사전에 내장해둔 구조적 가정)]] 덕분에 적은 데이터에서도 잘 학습되지만, 기본 연산이 "근처 픽셀" 중심이라 멀리 떨어진 객체 간 관계(장거리 의존성)를 직접 다루기 어렵다. 멀리 있는 정보는 receptive field를 키우기 위해 층을 깊게 쌓거나 dilation, FPN/skip, non-local 같은 보완이 필요하다. 이런 이유로 bias는 스케일이 커지거나 더 복잡한 패턴으로 갈 때 확장성을 제한할 수 있다.

반면 Transformer 계열은 기본 연산이 토큰 간 저역 상호작용 이라 "멀리 있는 것끼리의 관계"를 구조적으로 바로 모델링할 수 있으며, locality / translation equivariance 같은 강한 bias가 없고(weak inductive bias), 대신 global self-attention으로 관계를 데이터로부터 직접 학습한다. 그래서 매우 큰 데이터가 필요하지만, 충분한 데이터가 확보되면 더 유연하고 더 확장 가능하며 전역 의존성을 효율적으로 포착할 수 있다.



## 2. Vision Transformers의 전반적인 아키텍처

ViT는 이미지를 패치 토큰 시퀀스로 바꾼 뒤, NLP의 Transformer Encoder처럼 (LayerNorm -> Multi-Head Self-Attention -> Residual) + (LayerNorm -> MLP -> Residual) 블록을 L번 반복한다. Self-Attention은 각 토큰이 다른 모든 토큰을 참고해 업데이트되며, MLP는 토큰별 비선형 변환으로 표현력을 보강한다. 분류는 보통 최종 \[==CLS==]토큰을 MLP head에 넣어 수행하고, 탐지/분할 같은 과제는 모든 패치 토큰을 ==다운스트림 헤드==에 연결해 사용한다.




## 3. Vit Input을 위한 데이터 준비

> ViT Input = Patch embeddings + CLS 토큰 + positional embeddings


### 1. Image Patch Creation

입력 이미지가 $H * W * C$라면, 이를 $P * P$크기 패치로 나누어 총 토큰 수를 아래 개수로 만든다.
$$N = \frac{H W}{P^2}$$
예를 들어, 244 x 244 이미지를 16 x 16 패치로 나누면 N = 196

각 패치는 "이미지의 한 조각"이지만, ViT 관점에서는 시퀀스의 한 토큰이 된다. P가 작아지면 N이 커져 전역 상호작용이 더 촘촘해지지만, Self-Attention 계산량이 대략 $O(N^2)$로 증가한다.


### 2. Patch Embedding

각 패치 ($P\times P\times C$)를 펼쳐서 길이 $P^2C$벡터로 만든 다음, 학습 가능한 선형 변환으로 D차원 임베딩으로 투영한다. 결과 텐서 형태는 보통 ($N, D$)이며, 이게 Transformer Encoder의 입력 토큰들이 된다. 실무적으로는 "패치를 자르고 펼치기 + 선형 투영"을 Conv2D(kernel=P, stride=P) 한 번으로 구현하기도 하는데, 이는 수학적으로 동일한 패치 임베딩(선형 projection)이다.


### 3. Add Class Token

시퀀스 맨 앞에 학습 가능한 벡터 $\mathbf{x}_{cls}\in\mathbb{R}^{D}$를 붙여 토큰 수를 $N+1$로 만든다. Encoder 블록들을 통과하면서 $\mathbf{x}_{cls}$는 self-attention을 통해 모든 패치 토큰의 정보를 끌어모아 "전체 이미지 요약" 역할을 하게 된다. 마지막에 이 $\mathbf{x}_{cls}$만 MLP head로 보내 분류하는 방식이 표준이며, 대안으로는 \[CLS]없이 패치 토큰 평균(pooling)으로도 분류를 구성할 수 있다.

#### 자료에서 설명하는 CLS 토큰
- **“learnable token”**
- **“does not correspond to any image patch”**
- **“used as image representation for classification”**

즉, 
- CLS 토큰은 "Classification에서 쓰기 편하도록 만든 요약 슬롯(summary slot)"이다.
- 하지만 encoder 자체가 classification-only라는 의미는 아니다.


### 4. Positional Encoding

Transformer는 토큰 간 "순서/위치"를 구조적으로 모르기 때문에, 각 패치가 원래 이미지의 어디에서 왔는지 알려주는 positional embedding $\mathbf{p}_i\in\mathbb{R}^{D}$를 토큰 임베딩에 더한다:
$$\mathbf{z}_i = \mathbf{x}_i + \mathbf{p}_i$$
보통 $(N+1, D)$ 형태로 \[CLS]까지 포함해 위치 임베딩을 준비하고, 패치들을 어떤 순서(예: row-major)로 나열했는지에 맞춰 매칭한다. 위치 임베딩은 학습형(learned)또는 사인/코사인(sinusoidal) 처럼 고정형으로 설계할 수 있고, 비전에서는 2D 구조를 반영해 2D 형태로 만들거나 1D로 펼쳐서 쓰는 변형들이 존재한다.