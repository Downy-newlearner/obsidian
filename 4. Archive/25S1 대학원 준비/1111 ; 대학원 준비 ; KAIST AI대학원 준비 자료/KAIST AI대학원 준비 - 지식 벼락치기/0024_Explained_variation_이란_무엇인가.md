# 🧐 Explained variation 이란 무엇인가?

## 정답 링크

https://velog.io/@jhlim2993/Variation-and-Prediction-Intervals

## 형식적 답

**Explained Variation(설명된 변동)**은 회귀 모델이 종속 변수의 변동성을 설명하는 부분을 나타내며, 모델의 예측 성능을 평가하는 데 중요한 지표입니다.
**Unexplained Variation(설명되지 않은 변동)**은 모델이 설명하지 못한 종속 변수의 변동성을 나타내며, 모델의 한계와 개선 가능성을 보여줍니다.
**결정 계수(R²)**를 통해 이 두 변동의 비율을 측정하여, 모델의 성능을 평가할 수 있습니다.

## AI 답변

Explained variation 또는 설명된 변동(variation)은 회귀분석에서 독립변수가 종속변수의 변동을 얼마나 설명하는지를 나타내는 개념입니다. 이는 회귀모형의 적합도를 평가하는 데 사용됩니다.

회귀분석에서 종속변수 Y의 전체 변동은 두 부분으로 나눌 수 있습니다.
1) 회귀모형이 설명한 변동 (explained variation)
2) 회귀모형이 설명하지 못한 변동 (unexplained variation 또는 residual variation)

Explained variation은 독립변수 X가 종속변수 Y의 변동 중 얼마나 설명했는지를 나타냅니다. 다시 말해 회귀모형에 포함된 독립변수들로 인해 설명되는 종속변수의 변동 부분을 의미합니다.

반면 unexplained 또는 residual variation은 회귀모형이 설명하지 못한 부분, 즉 오차항(error term)에 의해 설명되는 종속변수의 변동입니다.

일반적으로 explained variation의 비중이 클수록 회귀모형의 설명력이 높다고 볼 수 있습니다. 이는 R-squared 값을 통해 확인할 수 있습니다. R-squared는 전체 변동 중 explained variation이 차지하는 비율을 보여줍니다.

