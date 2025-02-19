---
created: 2025-02-19
tags:
  - Terminology
aliases:
  - 부스팅
reference:
---
## 부스팅이란?
- 머신러닝 앙상블 기법 중 하나로 sequential한 weak learner들을 여러 개 결합하여 예측 혹은 분류 성능을 높이는 알고리즘이다.

- 부스팅은 Additive model 중 하나이다.
	- Additive model은 비모수 회귀, 즉 함수 형태를 가정하지 않는 회귀 모형을 의미한다.
	- weak learner를 여러개 결합한 앙상블 기법인 부스팅이 어떻게 회귀식 형태를 띄게 되는지 추후 알아보자.

- 오버피팅을 막기 위해 약한 모델을 여러 개 결합시켜 그 결과를 종합한다는 게 기본적인 앙상블의 아이디어이다.
	- 약한 모델 자체는 오버피팅 될 수 있지만, 약한 모델을 여러 개 결합하면 서로의 단점을 보완하고 일반화 성능을 향상시킬 수 있다.

![[Pasted image 20250219144651.png|500]]
- 연속적인 weak learner들의 구조를 가진다. 
- 바로 직전 weak learner의 error를 반영하여 현재 weak learner를 보완한다.
	- 이 과정을 N번 하면 iteration N번 돌린 부스팅 모델이 되는 것이다.

![[Pasted image 20250219144358.png]]
