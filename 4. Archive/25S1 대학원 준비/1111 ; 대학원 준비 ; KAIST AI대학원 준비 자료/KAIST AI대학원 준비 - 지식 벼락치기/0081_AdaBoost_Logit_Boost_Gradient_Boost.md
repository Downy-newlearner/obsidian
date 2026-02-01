# 🧐 AdaBoost / Logit Boost / Gradient Boost

## AI 답변

AdaBoost, LogitBoost, 그리고 GradientBoost는 모두 앙상블 학습(Ensemble Learning) 기법의 부스팅(Boosting) 방법론에 속합니다. 이들은 약한 학습기(Weak Learner)들을 순차적으로 통합하여 강력한 예측 모델을 구축하는 방식입니다.

1. AdaBoost (Adaptive Boosting)
- 가장 오래된 부스팅 알고리즘 중 하나로, 1995년 Freund와 Schapire에 의해 제안되었습니다.
- 잘못 분류된 샘플에 더 큰 가중치를 부여하여 다음 약한 학습기가 잘못 분류된 샘플에 집중할 수 있도록 합니다.
- 주로 의사결정트리(Decision Tree)를 약한 학습기로 사용합니다.

2. LogitBoost
- AdaBoost의 확장 버전으로, 1999년 Friedman 등에 의해 제안되었습니다.
- 로지스틱 회귀(Logistic Regression)를 약한 학습기로 사용합니다.
- 이진 분류와 다중 클래스 분류 모두에 적용 가능합니다.

3. GradientBoost
- 1999년 Friedman에 의해 제안된 일반화된 부스팅 알고리즘입니다.
- 손실 함수의 그래디언트(Gradient)를 최소화하는 방향으로 약한 학습기를 추가합니다.
- 의사결정트리, 선형 모델 등 다양한 모델을 약한 학습기로 사용할 수 있습니다.
- XGBoost, LightGBM 등 최신 구현체가 있습니다.

이들 알고리즘은 약한 학습기들의 조합을 통해 강력한 예측 모델을 구축할 수 있으며, 특히 GradientBoost는 최신 기술과 결합되어 다양한 분야에서 높은 성능을 보여주고 있습니다.

