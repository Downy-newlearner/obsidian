# 🧐 Bagging 과 Boosting의 차이는?

## AI 답변

Bagging과 Boosting은 모두 앙상블 학습(Ensemble Learning) 기법입니다. 앙상블 학습이란 여러 개의 약한 학습기(weak learner)를 결합하여 강력한 예측 모델을 만드는 기법을 말합니다. 두 기법은 모델을 결합하는 방식에 차이가 있습니다.

1. Bagging (Bootstrap Aggregating)
- 원본 데이터에서 중복을 허용하여 부트스트랩 샘플을 만듭니다.
- 각 부트스트랩 샘플에서 별도의 모델을 학습시킵니다.
- 최종적으로 각 모델의 예측을 평균내어 결과를 도출합니다.
- 대표적인 예시로 Random Forest가 있습니다.
- Bagging은 분산(variance)을 줄여 과적합을 방지합니다.

2. Boosting
- 순차적으로 약한 학습기를 학습시킵니다.
- 이전 학습기의 오차를 보정하여 다음 학습기의 가중치를 조정합니다.
- 최종 모델은 가중치가 업데이트된 약한 학습기의 가중 합으로 구성됩니다.
- 대표적인 예시로 AdaBoost, Gradient Boosting 등이 있습니다. 
- Boosting은 편향(bias)과 분산을 모두 줄일 수 있습니다.

정리하자면, Bagging은 병렬적으로 모델을 결합하고 Boosting은 순차적으로 약한 학습기를 보강하는 방식입니다. 일반적으로 Boosting이 Bagging보다 예측 성능이 우수하지만, 과적합 위험이 있습니다.

