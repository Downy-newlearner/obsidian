**Week10–11 = 
“Seq2Seq → Attention → Self-Attention → Multi-Head → Transformer 완성 구조 → Positional Encoding → 왜 Transformer가 최고의 모델인가”**

## 1. Seq2Seq

Seq2Seq 모델은 RNN 기반의 인코더-디코더 구조로, 인코더가 입력 시퀀스를 순차적으로 읽으며 하나의 고정된 벡터(context vector)로 압축하고, 디코더는 이 벡터를 초기 상태로 받아 다음 단어를 하나씩 생성한다. 이 방식은 번역, 요약 등 다양한 시퀀스 변환 작업을 가능하게 했지만, 입력이 길어질수록 중요한 정보가 압축 과정에서 사라지는 information bottleneck, 그리고 디코더가 인코더 내부 상태에 직접 접근할 수 없어 특정 시점의 정보를 세밀하게 활용하지 못하는 한계가 존재한다.

### Teacher Forcing이란?

Teacher forcing은 디코더가 다음 토큰을 예측할 때, 이전에 모델이 예측한 토큰 대신 정답 토큰을 입력으로 넣어주는 훈련 기법이다.

즉, 디코더 입력을 다음처럼 한다:
- 일반적 추론: $y_{t-1} = \text{model output}$
- teacher forcing 훈련:  $y_{t-1} = \text{ground truth token}$

이 기법이 필요한 이유:
- 초기에 모델 예측이 매우 틀릴 때, 그 결과를 계속 입력하면 오차가 누적됨
- 정답 토큰을 사용하면 학습 속도 증가 + 안정적인 수렴

### 디코더가 time step t에서 hidden state를 생성할 때 필요한 정보

> 이전 디코더 hidden state + 이전 출력 token embedding

encoder 마지막 hidden state(context vector)는 디코더 초기 state에만 사용된다.
이후 반복 계산에서는 사용되지 않는다.

## 2. Attention

Attention은 디코더가 출력 단어를 생성할 때 인코더의 전체 hidden state를 모두 참고하고, 그중 어떤 부분이 현재 필요 정보인지 가중치를 통해 선택하는 매커니즘이다. 이를 통해 Seq2Seq의 고정된 컨텍스트 백터 의존을 제거하고, 매 시점마다 "필요한 부분만 집중해서" 정보를 가져오게 하여 긴 문장의 의존성 문제를 크게 줄인다. 결국 Attention은 모델이 입력의 다양한 위치에서 정보를 상황에 따라 동적으로 검색할 수 있도록 하여 성능과 안정성을 크게 향상시킨다.

### Attention 매커니즘의 효율이 높은 이유

가중합을 통해 gradient가 여러 경로로 분산되기 때문이다.

각 token이 여러 token을 참조해 gradient 경로가 다중화되고, 이는 RNN 대비 훨씬 안정적인 학습을 제공한다.

## 3. Self-Attention

Self-Attention은 입력 시퀀스 내부의 모든 토큰이 서로를 바라보며 관계를 계산하는 구조로, RNN처럼 순서대로 처리하지 않아도 시퀀스 전체 패턴을 한 번에 분석할 수 있다. 각 토콘은 Query, Key, Value 벡터로 변환되어 다른 모든 토큰과의 유사도를 계산하고, 이를 기반으로 중요한 정보는 크게 반영하고 덜 중요한 정보는 약하게 반영해 새로운 표현을 형성한다. 이러한 구조는 long-range dependency를 자연스럽게 포착하고 병렬 계산이 간으해 RNN 기반 모델보다 훨씬 빠르고 안정적인 특징 표현을 제공한다.

### Self-Attention의 출력이 "contextualized representation"이라 불리는 이유

각 토큰이 주변 토큰의 Value 정보를 weighted sum으로 섞어 표현하기 때문이다. 그래서 "문맥화된 표현"이라고 부른다.
	-> 물론 모든 토큰의 Value 정보를 사용하지만 주변 토큰의 정보에는 높은 가중치를 주도록 설계되어있어 위 설명은 틀린 표현이 아니다. 오히려 일반적으로 설명하는 방식이다.


## 4. Multi-Head Attention

Multi-Head Attention은 Self-Attention을 여러 개 병렬로 수행하는 방식으로, 각 헤드(head)가 서로 다른 의미적 공간(semantic)에서 패턴을 학습한다. 예를 들어 하나의 헤드는 문법적 구조에 집중하고 다른 헤드는 의미적 유사성을 포착하는 식으로, 여러 시각적,언어적 관계를 동시에 고려할 수 있게 만든다. 이후 이 헤드들의 출력을 결합해 정보를 통합함으로써 단일 Self-Attention보다 훨씬 풍부한 표현 능력을 갖게 된다.

### 서로 다른 Semantic Subspace를 만드는 법

서로 다른 Semantic Subspace는 $W_Q, W_K, W_V$를 헤드마다 별도로 둠으로써 자연스럽게 형성된다.

모델이 loss를 최소화하려고 학습하는 과정에서 서로 다른 $W_Q, W_K, W_V$를 가진 헤드들은 서로 겹치지 않는 유용한 특징을 자동으로 찾아 분리하여 사용한다.

결과적으로:
- 어떤 head는 문장의 syntactic 관계를 잘 포착하고
- 어떤 head는 long-range dependency를 잘 보고
- 어떤 head는 특정 종류의 단어쌍을 중심적으로 본다

이런 식으로 기능적 분화(functional specialization)가 자연스럽게 일어난다.

## 5. Transformer 완성 구조

Transformer는 RNN의 순차적 처리 과정을 완전히 제거하고, Self-Attention과 Position-wise Feed-Forward Network를 층층히 쌓아 인코더와 디코더를 구성한 모델이다. 인코더는 입력 정보를 다층 Self-Attnetion을 통해 요약하고, 디코더는 이전에 생성된 단어와 인코더 출력(인코더의 모든 hidden state의 출력)에 대해 Masked Self-Attention 및 Cross-Attention을 수행하여 다음 토큰을 예측한다. 이러한 구조는 완전 병렬화가 가능해 학습 속도가 빠르고, 깊고 넓은 모델 확장이 용이해 성능이 크게 향상되었다.

### 디코더는 한 스텝에서 아래의 두 Attention을 모두 수행한다.

1. Masked Self-Attention
- 디코더 내부에서 "과거 생성 토큰끼리" 서로 참고
- 미래 토큰 차단(causal amsk)
	-> 디코더 내부에서 자기 자신끼리 관계 파악 / 미래 토큰 못 보도록 mask
	-> 디코더 내부의 문맥==(지금까지 생성한 단어들) 이해==

[[Masked Self-Attention 적용법 차이 - 훈련, 추론]]

2. Cross-Attention
- 디코더가 "인코더 출력 전체"를 참고
- Q는 디코더, K/V는 인코더
	-> 디코더가 인코더 전체 hidden states를 바라봄 / 인코더가 입력에서 추출한 정보들을 선택적으로 가져옴
	-> ==원문(입력 문장 또는 입력 이미지 patch들) 정보 반영==

3. Feed-Forward Network

### 두 Attention은 구체적으로 어떻게 연결되는가?

**Step 1: Masked Self-Attention**

$$\text{dec\_self} = \text{SelfAttention}(Q=dec, K=dec, V=dec, \text{mask=causal})$$

**Step 2: Cross-Attention**

$$\text{dec\_cross} = \text{Attention}(Q=\text{dec\_self}, K=\text{enc\_output}, V=\text{enc\_output})$$


**Step 3: Feed-Forward Network**

$$\text{dec\_ffn} = \text{FFN}(\text{dec\_cross})$$

이 과정이 여러 레이어 반복됨.


### Self-Attention이 먼저 적용되고 FFN이 나중에 적용되는 이유

Self-Attention으로 전역 문맥을 먼저 통합한 후 FFN으로 비선형 변환을 적용해야 효과가 크기 때문이다.
Self-Attention으로 token 간 관계를 먼저 정리해야 FFN이 유의미한 변환을 수행할 수 있다.

전역 패턴 -> 비선형 변환 순서가 Transformer의 핵심이다.

###  Residual Connection이 중요한 이유

Residual은 deep network에서 gradient 흐름을 안정화하는 핵심 기술이다.
Transformer는 매우 깊기 때문에 필수적이다.


## 6. Positional Encoding

Self-Attention은 입력 토큰 사이의 순서를 알 수 없기 때문에, Transformer는 각 토큰이 시퀀스의 어느 위치에 있는지를 알려주는 Positional Encoding을 입력 벡터에 더해준다. 이 인코딩은 일정한 규칙성을 가지는 사인/코사인 함수 기반 표현 또는 학습 가능한 임베딩으로 구성되며, 모델이 "앞뒤 관계", "거리", "반복 패턴" 등 순서적 정보를 효과적으로 이해하도록 돕는다. 이로 인해 순서를 잃어버린 Self-Attention 구조가 자연스럽게 시퀀스 구조를 학습할 수 있다.

### Positional Encoding이 사인/코사인 기반 비학습 방식으로 설계된 이유

sin/cos는 서로 다른 주파수의 조합으로 절대 위치 뿐 아니라, 상대 거리까지 자연스럽게 표현할 수 있어 시퀀스 길이가 달라도 패턴을 유지한다.

### Positional Encoding이 Generalization에 기여하는 이유

sin/cos는 주기 함수라 unseen length에서도 동일한 방식으로 위치 패턴을 구성할 수 있기 때문이다.



## 7. 왜 Transformer가 최고의 모델인가?

Transformer는 RNN의 병목을 완전히 해결해 모든 토큰을 병렬로 처리하며, Self-Attention을 통해 long-ranse dependency를 가장 안정적으로 효율적으로 학습할 수 있다. 또한 대규모 데이터에서 성능이 지속적으로 향상되는 스케일링 특성, 구조의 단순함으로 인한 확장성(ViT, LLM 등), 다양한 모달리티(NLP, Vision, Audio, 멀티모달)까지 통합 가능한 유연성 덕분에 현대 딥러닝 분야의 사실상 표준 아키텍처로 자리 잡았다.




