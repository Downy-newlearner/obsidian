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

## 2. Ordered Target Encoding
- 범주형 변수를 그대로 모델에 넣어주면 알아서 Ordered target encoding을 진행한다.

### Target Encoding
- 범주형 컬럼에서의 각 값의 타겟 변수 값을 평균낸 후 그 값으로 인코딩을 진행한다.
	- ![[Pasted image 20250219152219.png|250]]
	- 예를 들어 Weather 변수에서 'Cloudy'값들이 가지는 평균 타겟 값이 18.5라면 'Cloudy'는 18.5로 인코딩된다.

- 이렇게하면 타겟 값이 독립 변수에 들어가기 때문에 data leakage가 발생할 수 있다.

### Ordered Target Encoding
- Target Encoding의 data leakage를 방지하기 위한 기법이다.
- Weather 데이터의 인코딩을 위해 Weekday의 타겟 인코딩 결과를 반영한다.
- 이전 컬럼이 없는 Weekday 컬럼은 Laplace Smoothing이라는 방법을 사용한다.


## 3. Ordered Boosting
![[Pasted image 20250219152445.png|500]]
- 먼저 Train set의 row 순서를 랜덤으로 섞는 'Random Permutation'을 진행한다.
- 