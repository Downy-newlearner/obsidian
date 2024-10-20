---
책 이름: 독학
설명: 목적 함수, 최적화 문제에서 변수가 최소화 또는 최대화해야 하는 함수이다. 일례로 경사 하강법의 대상이 목적 함수인 것이다.
챕터/날짜: Diffusion Model
---
![[Source/image 10.png|image 10.png]]
다음과 같은 식을 비용함수로 사용한다.
- **MSE(Mean Squared Error, 평균 제곱 오차):** $\frac{1}{N}\sum_{i=1}^{N}(yi−y^i)^2$﻿
- **MAE(Mean Absolute Error, 평균 절대 오차):** $\frac{1}{N}\sum_{i=1}^{N}∣yi−y^i∣$﻿
- **Binary Cross-entropy (a.k.a logloss) :** −_N_1​⋅∑_i_=1_N_​(_yi_​⋅log(_y_^​_i_​)+(1−_yi_​)⋅log(1−_y_^​_i_​))
- **Multinomial-logloss :** −_N_1​⋅∑_i_=1_N_​∑_k_=1_K_​(_yi_,_k_​⋅log(_y_^​_i_,_k_​)), K 개 범주
- 목적함수로 손실함수의 평균을 사용하거나 sum을 해주는 값을 사용하는 이유는?
    - 알고리즘의 Vectorization 결과라고 할 수 있다.
    - 하나의 관측치로 학습을 반복하는 것은 하드웨어적으로, 그리고 이론적으로 어려움에 빠질 수 있다.
    - 따라서 **전체 데이터(Full-batch)** 또는 **부분 데이터(mini-batch)**를 한 번의 학습(**1 epoch**)에 사용한다.
    - 이때, 모델의 가중치들이 어떤 결과를 나타내는지 하나의 충분 통계량이 필요하다. 그래서 평균을 사용해서 하나의 값으로 변형하는 것이다.