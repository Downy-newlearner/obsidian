---
created: 2025-02-12
tags:
  - Terminology
aliases: 
reference: https://everyday-tech.tistory.com/entry/%EC%9D%B8%EA%B3%BC-%EC%B6%94%EB%A1%A0%EC%9D%84-%EC%96%B4%EB%A0%B5%EA%B2%8C-%ED%95%98%EB%8A%94-%EC%9A%94%EC%86%8CCollider
---
## Collider란?
![[Pasted image 20250213203915.png|450]]
- Collider는 원인 변수와 결과 변수의 영향을 동시에 받는 변수이다.
- Collider에 의한 Non-Causal Association을 제거하기 위해서는 Collider를 통제하지 말아야 한다.
	- Collider는 원인 변수와 결과 변수의 영향을 동시에 받은 결과이므로 이를 통제하는 경우 원인, 결과 변수 간 특정 종속 관계가 생기게 된다.(Collider bias)

- Collider는 무시하면 된다!


## 새로운 고민
- 분석하고자 하는 원인 변수와 결과 변수에 대한 교란 변수와 Collider를 판별하기 위해서는 어떤 변수가 어떤 변수에 영향을 주는지 그 방향을 알아야한다.
- 그래야 교란 변수는 통제하고, Collider는 무시하는데 어떻게 그 방향을 알 수 있을까?

1. 상관 관계는 아닐듯
2. 서로 어떤 영향을 주는지 알아보기 위해서 두 변수에 대해 회귀 계수 분석을 한다면?
	- 이미 Non-Causal Association에 영향을 받은 상태라 의미없는 분석이 될 것 같다.

- 배경지식으로 각 컬럼이 어떤 컬럼에 영향을 주는지 고민해보고 원인 변수와 결과 변수(타겟 변수)에 모두 영햐