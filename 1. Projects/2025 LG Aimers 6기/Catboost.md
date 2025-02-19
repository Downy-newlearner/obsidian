---
created: 2025-02-19
tags:
  - Terminology
aliases: 
reference:
---
## 특징
- 범주형 변수로 이루어진 데이터셋에서 예측 성능이 우수하다.
- [[Boosting]] 기반의 모델이다.
- 특이한 Categorical feature(범주형 변수) 처리
	1. Categorical feature combination
	2. 범주형 변수를 encoding할 필요 없음(알아서 target encoding을 해준다.)
- Ordered Target Encoding
- Ordered Boosting

## 1. Categoricla Feature Combination: 특이한 범주형 변수 처리
- 데이터의 두 컬럼에서 매치되는 값이 항상 같다고 가정하자. 
	- 예를 들어 A컬럼의 값이 a1이면 B컬럼의 값이 항상 b1이고, A컬럼의 값이 a2이면 B컬럼의 값이 항상 b2인 상황이다.
- 그렇다면 컬럼 하나를 삭제하여 dimension을 자동으로 줄인다.

