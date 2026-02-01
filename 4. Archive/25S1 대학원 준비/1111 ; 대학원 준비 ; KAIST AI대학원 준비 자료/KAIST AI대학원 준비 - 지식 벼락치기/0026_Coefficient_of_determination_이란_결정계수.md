# 🧐 Coefficient of determination 이란? (결정계수)

## 정답 링크

https://velog.io/@jhlim2993/Variation-and-Prediction-Intervals

## 형식적 답

평균 대비 어느정도 모델이 효과가 좋은지, 단점 유의하지 않은 변수가 추가되어도 항상 증가해서 보정하는 것이 필요 변수만큼 작게해줌

## AI 답변

결정계수(Coefficient of determination, R^2)는 회귀모델의 적합도를 나타내는 지표입니다. 0과 1 사이의 값을 갖게 되며 1에 가까울수록 회귀모델이 데이터를 잘 적합한다는 것을 의미합니다.

구체적으로 결정계수는 종속변수의 총 변동 중에서 회귀모델에 의해 설명된 변동의 비율을 나타냅니다. 즉, 결정계수가 0.7이라면 종속변수 변동의 70%가 회귀모델에 의해 설명된다는 뜻입니다.

결정계수는 다음과 같이 계산됩니다.

R^2 = 1 - (SSE/SST)
      = SSR/SST

여기서 SSE는 오차제곱합(Error Sum of Squares), SST는 총제곱합(Total Sum of Squares), SSR은 회귀제곱합(Regression Sum of Squares)을 나타냅니다.

결정계수는 회귀모델의 설명력을 판단하는 데 유용하지만, 예측 성능 자체를 직접적으로 나타내지는 않습니다. 또한 독립변수가 많아질수록 결정계수 값이 커지는 경향이 있어 주의해야 합니다. 이를 보완하기 위해 수정된 결정계수(Adjusted R^2) 등을 사용하기도 합니다.

