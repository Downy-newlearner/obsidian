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
	output

## 결론

- 훈련을 통해 문장의 이웃들로 유사도를 측정하여 관계가 있는 벡터를 유사도가 있는 벡터가 되도록 할 수 있다.