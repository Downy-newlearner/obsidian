---
created: 2025-03-16
tags:
  - Terminology
aliases: 
reference: https://youtu.be/sY4YyacSsLc?si=5D6s4RIC-stStv9R
---
## one-hot encoding은 유사도가 없다.

- 모든 벡터간의 각도는 90도, 거리는 모두 같다. 유사도를 표현할 수 없다.

## 임베딩을 하면 거리로 각 벡터간의 유사도를  표현할 수 있다
비슷한 위치에 있는 단어를 이웃이라고한다.

skip gram
![[Pasted image 20250316024135.png]]

neighbor를 타겟이라고 한다.


![[Pasted image 20250316024215.png]]
딥러닝에 들어가는 건 word가 아니라 encoding value이다.

![[Pasted image 20250316024311.png]]

레이어는 총 3개가 있다.
	input
	hidden
	output'


## Loss 함수

Word2Vec의 손실 함수는 사용되는 학습 방식에 따라 달라집니다. Word2Vec에는 주로 CBOW(Continuous Bag of Words)와 Skip-Gram 두 가지 학습 방식이 있는데, 각 방식의 손실 함수는 다음과 같습니다:

### Skip-Gram 모델

- **목표**: 주어진 중심 단어로부터 주변 단어 예측.
- **손실 함수**:
    - Skip-Gram은 중심 단어를 기준으로 주변 단어를 예측하는 확률을 최대화하는 방식으로 학습합니다.
    - 주로 네거티브 샘플링(Negative Sampling)이나 층마다 내적을 사용하는 소프트맥스(Hierarchical Softmax) 기법을 활용합니다.
    - 네거티브 샘플링의 경우, 손실 함수는 다음과 같이 표현됩니다: [ \text{Loss} = -\log(\sigma(v'_{w_O} \cdot v_{w_I})) - \sum_{i=1}^{k} \log(\sigma(-v'_{w_{N_i}} \cdot v_{w_I})) ]
    - 여기서 (v_{w_I})는 입력 단어의 벡터, (v'_{w_O})는 출력 단어의 벡터, (v'_{w_{N_i}})는 네거티브 샘플 단어의 벡터, ($\sigma$)는 시그모이드 함수입니다.

### CBOW 모델

- **목표**: 주변 단어들로부터 중심 단어 예측.
- **손실 함수**:
    - 하나의 중심 단어를 예측하기 위해 주변 단어들의 임베딩 벡터를 평균화한 값을 사용합니다.
    - CBOW도 마찬가지로 네거티브 샘플링 또는 하이어라키컬 소프트맥스를 사용하여 손실을 계산합니다.
    - 이 방식의 손실 함수는 Skip-Gram과 유사하지만 입력과 출력의 방향이 반대입니다.

두 방식 모두 네거티브 샘플링을 통해 계산 비용을 줄이고, 더 효율적인 학습을 가능하게 합니다.

GoodBad

13,455ms

4,250t

476t

  

Auto-clear

Draggable item message_5nmngzmb was dropped over droppable area message_5nmngzmb

## 결론

- 훈련을 통해 문장의 이웃들로 유사도를 측정하여 관계가 있는 벡터를 유사도가 있는 벡터가 되도록 할 수 있다.