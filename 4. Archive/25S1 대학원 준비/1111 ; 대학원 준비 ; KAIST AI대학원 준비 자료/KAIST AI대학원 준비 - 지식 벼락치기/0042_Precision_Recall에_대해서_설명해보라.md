# 🧐 Precision Recall에 대해서 설명해보라

## 정답 링크

https://velog.io/@jhlim2993/Precision-Recall-F1-Score

## 형식적 답

5. Precision과 Recall의 활용
의료 진단: Recall이 중요한 경우, 질병 환자를 놓치는 것(음성으로 잘못 분류하는 것)은 매우 위험할 수 있습니다. 따라서 높은 Recall이 필요합니다.
스팸 필터링: Precision이 중요한 경우, 정당한 이메일을 스팸으로 잘못 분류하는 것은 사용자에게 불편을 줄 수 있습니다. 따라서 높은 Precision이 필요합니다.
결론적으로:

**Precision(정밀도)**은 모델이 양성으로 예측한 사례 중 실제로 양성인 사례의 비율을 나타내며, 양성 예측의 정확성을 평가합니다.
**Recall(재현율)**은 실제 양성 사례 중에서 모델이 올바르게 예측한 비율을 나타내며, 양성 사례의 포착 능력을 평가합니다.
Precision과 Recall은 종종 트레이드오프 관계에 있으며, 특정 응용 분야에서 어떤 지표가 더 중요한지를 고려하여 모델을 평가해야 합니다. F1 Score는 Precision과 Recall의 균형을 평가하는 데 유용한 지표입니다.

## AI 답변

Precision(정밀도)과 Recall(재현율)은 기계학습 및 정보검색 분야에서 모델의 성능을 평가하는 중요한 지표입니다.

1. Precision(정밀도)
- Precision은 모델이 긍정(Positive)으로 예측한 것 중에서 실제 긍정인 비율을 나타냅니다.
- Precision = TP / (TP + FP)
  - TP(True Positive): 실제 긍정을 긍정으로 예측한 경우
  - FP(False Positive): 실제 부정을 긍정으로 잘못 예측한 경우

2. Recall(재현율)
- Recall은 실제 긍정 샘플 중에서 모델이 긍정으로 예측한 비율을 나타냅니다.
- Recall = TP / (TP + FN)
  - TP(True Positive): 실제 긍정을 긍정으로 예측한 경우  
  - FN(False Negative): 실제 긍정을 부정으로 잘못 예측한 경우

일반적으로 Precision과 Recall 사이에는 트레이드오프(trade-off) 관계가 있습니다. Precision을 높이려면 Recall이 낮아지고, Recall을 높이려면 Precision이 낮아지게 됩니다. 이 두 지표를 동시에 만족시키는 것이 어려운 경우가 많습니다.

따라서, 적절한 Precision과 Recall의 균형을 찾는 것이 중요합니다. 이를 위해 F1 Score와 같은 단일 지표를 활용하기도 합니다. F1 Score는 Precision과 Recall의 가중 조화 평균으로, 0과 1 사이의 값을 가집니다.

