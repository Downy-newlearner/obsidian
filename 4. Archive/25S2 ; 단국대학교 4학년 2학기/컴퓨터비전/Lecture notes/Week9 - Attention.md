
## 1. Attention의 필요성

Seq2Seq = 압축 방식 -> 근데 말이 압축이지 정보 흐름이 좁아져서 정보가 손실됨(병목 현상)
Attention = 검색 방식 -> 전체 단어 각각의 상태들을 "DB 처럼" 보관하는 구조

Attention은 CNN의 고정적이고 지역적인 시각 처리 방식, RNN 기반 Seq2Seq의 고정 길이 컨텍스트 벡터와 장기 의존성 문제를 극복하기 위해 등장했다. 즉, 입력 전체 중에서 중요한 부분만 선택적으로 더 집중해 처리하면 모델이 더 정확하고 효율적으로 정보를 다룰 수 있다는 아이디어가 발전한 것이며, 길이가 긴 입력에서 정보 손실과 병렬 처리의 어려움을 해결하기 위한 핵심 동기가 되었다.

[[week9 - 1) attention의 필요성 슬라이드 내용]]
### 병목의 종류

| **용어**                                | **의미**             | **Seq2Seq에서 해당?** | **Transformer에서 해결?** |
| ------------------------------------- | ------------------ | ----------------- | --------------------- |
| **정보 병목 (representation bottleneck)** | 하나의 벡터에 압축되어 정보 손실 | **있음**            | Attention이 해결         |
| **계산 병목 (computational bottleneck)**  | 병렬 처리 불가, 연산 느림    | RNN에 **있음**       | Self-Attention이 해결    |
|                                       |                    |                   |                       |


## 2. Attention의 원리(Q/K/V 매커니즘)

Attention은 Query, Key, Value 세 가지 벡터를 기반으로 작동하며, ==Query와 Key 간의 유사도(score)를 계산한 뒤 softmax로 정규화하여 Value들을 가중합==해 새로운 표현을 생성하는 방식이다. 이 과정은 모델이 "어떤 정보에 집중해야 하는가"를 학습할 수 있게 만들어주며, 다양한 입력 단위(단어, 이미지 패치 등) 간의 관계를 동적으로 파악하도록 한다.

### Q-K-V

- Query는 현재 필요한 정보를 탐색하기 위한 기준 벡터이며 Key와의 유사도 계산에 사용된다.
- Key는 Query와의 유사도를 계산하는 기준 representation으로, attention score 생성에 사용된다.
- Value는 




참고로, K는 '매칭용 정보' / V는 '출력용 정보'이다.
즉, K는 Query가 참고하여 "어디가 중요한지" 판단하여 가중치를 결정하는 기준(signal)을 제공한다. 
V는 Q, K를 통해 판단한 중요한 부분에 높은 가중치를 매기는 연산을 반영해 출력 벡터를 만드는 것이다. 
"Value에 가중치를 곱한 뒤 선형 결합하여 출력 벡터를 만든다"

Q, K -> 유사도를 계산한 뒤 가중치를 만듦
V -> 가중치를 곱한 뒤 선형 결합하여 출력벡터를 만듦

K는 Q와 dot product 되어 attention score를 만든다.
score는 softmax로 정규화되어 attention weight가 되고
이 weight가 V에 곱해져 선형 결합되어 최종 output을 만든다.

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

### K와 V는 데이터가 같은가? 동일한 입력을 쓰는가? -> NO

$$K = X W_K,\quad V = X W_V$$

K와 V는 같은 입력 X(단어 embedding 또는 패치 embedding)를 쓰지만 서로 다른 선형 변환($W_K, W_V$)를 통해 서로 다른 의미를 가진 공간으로 projection 된다.

그래서:
- 둘 다 같은 단어에서 출발하지만
- Key는 "검색을 위한 representation"
- Value는 "출력을 구성할 representation"
- 으로 완전히 역할이 구분된다.

### 그럼 왜 굳이 K와 V를 나눠서 서로 다른 projection을 하는가?

만약 K와 V가 완전히 같다면 
	"중요도를 판단하는 특징"과
	"출력으로 반영되는 특징"이
	같은  임베딩 하나로 묶여버린다.

-> 이러면 모델의 표현력이 크게 떨어진다.

그래서 X에 각 가중치($W_K, W_V$)를 곱해 
	K는 “이 단어가 네가 찾는 것과 관련 있는가?”만 판단하는 역할.
	V는 “관련 있다면 나에게서 이 내용을 가져가라”라는 역할.
		full semantic embedding에 가까움
		관련 있다고 판단되면, 실제 Value에서 정보를 가져와 output을 만든다.

### Attention의 Output은 예측 단어인가? -> No

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

Attention의 Output = =="새로운 hidden representation"==

Transformer Decoder에서 단어 예측이 일어나는 위치는 다음이다:

$$\text{logits} = \text{FFN}(h) W_{\text{vocab}} + b$$
$$\text{prediction} = \arg\max(\text{softmax(logits)})$$

즉, 
- Attention Output -> 다음 레이어로 전달되는 hidden state
- 마지막 레이어의 hidden state -> Linear layer($W_{vocab}$) -> Softmax -> 에측 단어

따라서:

> Attention Output은 "단어 예측 과정의 중간 표현(hidden state)"이다.
> 직접 단어를 출력하지 않는다.




## 3. Vision Attention 종류 (Channel / Spatial / Temporal / Branch)

Vision 분야에서는 Attention이 채널에서 중요한 feature를 강조하거나, 공간적으로 중요한 위치를 강조하거나, 시간 축(영상)에서 중요한 순간을 강조하거나, 여러 네트워크 경로 중 적합한 경로를 선택하는 형태로 발전해왔다. 즉, 시각 정보의 "무엇(채널), 어디(공간), 언제(시간), 어떤 경로(브랜치)"에 집중할지 조절하는 다양한 attention 기법이 존재한다.

Channel Attention: 어떤 채널(특징맵)이 중요한지를 판단해 중요 채널을 강조한다.
Spatial Attention: 이미지 내 중요한 위치(공간적 region)를 강조한다.
Temporal Attention: 영상처럼 시계열 데이터에서 어떤 시점이 중요한지 판단한다.
Branch Attention이 필요한 상황: 여러 네트워크 경로나 스케일 중 어떤 경로가 중요한지 선택해야 할 때 사용된다.

Vision Attention 요약: Vision Attention은 이미지에서 무엇(채널), 어디(공간), 언제(시간)이 중요한지를 동적으로 강조하는 메커니즘이다.



## 4. Encoder - Decoder와의 연결

U-Net(이미지)과 Seq2Seq(자연어) 모두 Encoder-Decoder 구조로 정보를 압축 후 복원하는데, 이 과정에서 정보 병목(bottleneck) 문제가 발생한다. ==Attention은 Decoder가 Encoder의 전체 상태(hidden states)에 직접 접근하도록 해 bottleneck을 제거==하며, Transformer와 같은 현대 모델의 기반이 되는 핵심 구성 요소로 자연스럽게 확장되었다.

![[Pasted image 20251212171424.png|500]]








## Transformer

[[Transformer는 다음 요소들로 구성된다]]



### Transformer에서 학습되는 것

- Attention projection weights
- FFN weights
- LayerNorm params
- embedding weights

