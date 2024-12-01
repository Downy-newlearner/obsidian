---
Lecture date: 2024-11-18
tags:
---
![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0001.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0002.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0003.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0004.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0005.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0006.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0007.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0008.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0009.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0010.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0011.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0012.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0013.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0014.jpg]]
샘플이 많이 발생한 지점의 확률이 높을 것이라는 추론에서 시작.
샘플이 발생하면 그 지역에 커널을 씌운다.(아래 figure들 참고)
	삼각형 또는 가우시안 커널을 가장 많이 사용한다.

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0015.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0016.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0017.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0018.jpg]]
샘플 충분해야함
계산량 많음
윈도우 사이즈에 art 요소가 있다

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0019.jpg]]
pdf를 추정하지 말고, sample만 갖고 바로 추정해보자.

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0020.jpg]]
사용하는 distance가 다양하다.

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0021.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0022.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0023.jpg]]
## Adaptive Decision Boundaries Modeling

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0024.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0025.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0026.jpg]]
### Adaptive decision boundary algorithm(example 풀어보기)

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0027.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0028.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0029.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0030.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0031.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0032.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0033.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0034.jpg]]
## Adaptive Discriminant Functions

클래스가 n개라면 n개의 decision function을 모두 정의한다.
그 후 샘플이 하나 들어오면, 그 샘플을 모든 decision function에 집어넣어, 가장 값이 큰 쪽으로 decision을 내리는 방법이다.

이 방법을 사용했는데 틀린다면, w들을 서로 조절한다.
조절하는 방식은 다음과 같다.
	원래 답이 i클래스인데 j클래스로 분류가 됐다면, j클래스의 w는 줄여주고, i클래스의 w는 늘려준다.
![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0035.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0036.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0037.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0038.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0039.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0040.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0041.jpg]]
## Minimum Squared Error Discriminant Functions
한 개의 discriminant 모델을 정한다.
트레인 샘플이 v개가 있다고 가정하면, 이 v개의 샘플들을 D에 집어넣어 값을 얻어낸다.
desired value와 얻은 값의 차이를 squared 시킨다.(오차를 제곱하여 더할 때 오차가 서로 상쇄되지 않도록 한다.)

w들을 미분해서 w모두 0이 되도록하는 값을 찾아가는 것이다.
![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0042.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0043.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0044.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0045.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0046.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0047.jpg]]
미분 후 연립해서 $w_0, w_1, w_2$를 구해 Decision boundary를 구한다.

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0048.jpg]]

![[[강의노트]Ch4_NonparametricDecisionMaking(수정) (1)_page-0049.jpg]]

*요약*
classification 방법은 통계적 방법을 이용했을 때, 베이지안 클래시파이어를 이용한다.
이 때의 확률 값은 
	1. 잘 알려진 RV function을 이용하는 방법과, 
	2. 샘플들 자체를 이용하는 방법(윈도우를 씌워 모델링), 
	3. 또는 이런 확률 추정을 하지 않고 nearest neighbor 샘플만 이용하는 방법도 있고, 
	4. iteration 방법을 통해서 decision boundary를 찾아가는 adaptive decision boundary.
adaptive discriptive function도 있고
전체 평균 에러를 최소화 하는 방법으로 DB를 찾는 min squared error 방식이 있다.