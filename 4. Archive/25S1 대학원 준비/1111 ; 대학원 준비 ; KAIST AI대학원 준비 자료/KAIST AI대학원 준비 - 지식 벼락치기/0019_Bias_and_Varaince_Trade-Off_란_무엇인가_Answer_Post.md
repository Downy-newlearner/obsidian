# 🧐 Bias and Varaince Trade-Off 란 무엇인가? [Answer Post]

## 정답 링크

https://jrc-park.tistory.com/268

## 형식적 답

https://velog.io/@jhlim2993/Bias-and-Variance-Trade-Off

## AI 답변

Bias(편향)와 Variance(분산) 트레이드오프는 머신러닝 모델의 성능과 일반화 능력을 결정하는 중요한 개념입니다. 이는 모델의 복잡도와 관련이 있습니다.

1. Bias(편향)
- 모델이 데이터의 패턴을 제대로 학습하지 못하여 발생하는 오류
- 과소적합(Underfitting)의 원인이 됨
- 모델이 지나치게 단순할 때 발생

2. Variance(분산) 
- 모델이 훈련 데이터에 과도하게 최적화되어 새로운 데이터에 대한 일반화 능력이 낮아지는 현상
- 과대적합(Overfitting)의 원인이 됨
- 모델이 지나치게 복잡할 때 발생

Bias-Variance 트레이드오프는 모델의 복잡도를 조절하여 Bias와 Variance 사이의 적절한 균형을 찾는 것입니다.

- 모델이 단순할수록 Bias는 높고 Variance는 낮음
- 모델이 복잡할수록 Bias는 낮고 Variance는 높음

이상적인 모델은 Bias와 Variance가 모두 낮아야 하며, 이를 위해서는 적절한 모델 복잡도와 정규화 기법 등을 활용해야 합니다. 과소적합과 과대적합을 피하고 일반화 성능을 높이는 것이 목표입니다.

