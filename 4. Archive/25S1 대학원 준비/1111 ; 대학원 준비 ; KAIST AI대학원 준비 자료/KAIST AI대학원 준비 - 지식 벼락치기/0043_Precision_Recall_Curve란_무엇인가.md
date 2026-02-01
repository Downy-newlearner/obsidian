# 🧐 Precision Recall Curve란 무엇인가?

## 정답 링크

https://velog.io/@jhlim2993/Precision-Recall-F1-Score

## 형식적 답

3. Precision-Recall Curve의 해석
곡선의 위치:

곡선이 오른쪽 상단에 가까울수록(즉, 높은 Recall과 높은 Precision을 동시에 유지할수록) 모델의 성능이 우수합니다.
곡선이 왼쪽 하단에 가까울수록 모델의 성능이 떨어지며, 이는 모델이 양성 클래스를 잘 구분하지 못하는 것을 의미합니다.
임계값 선택:

Precision-Recall Curve를 사용하여 모델이 어떤 임계값에서 최적의 성능을 발휘하는지 판단할 수 있습니다.
특정 상황에서 Precision과 Recall 간의 균형이 중요한 경우, F1 Score와 같은 추가 지표를 고려할 수 있습니다.
4. Precision-Recall Curve와 ROC Curve의 차이
ROC Curve: **True Positive Rate (TPR)**와 False Positive Rate (FPR) 간의 관계를 시각화하며, 주로 클래스 불균형이 크지 않은 경우에 적합합니다.
Precision-Recall Curve: Precision과 Recall 간의 관계를 시각화하며, 클래스 불균형이 큰 경우에 특히 유용합니다. 양성 클래스가 적은 상황에서 더 의미 있는 성능 평가를 제공합니다.
5. Precision-Recall Curve의 용도
Precision-Recall Curve는 특히 양성 클래스를 식별하는 것이 중요한 상황에서 유용합니다:

의료 진단: 질병이 있는 환자를 식별하는 것이 중요한 경우, 높은 Recall이 중요하며, Precision-Recall Curve가 유용하게 사용됩니다.
스팸 필터링: 스팸 이메일을 정확히 탐지하는 것이 중요한 경우, Precision-Recall Curve를 통해 스팸 탐지 성능을 평가할 수 있습니다.
이상 탐지: 드문 이벤트를 탐지해야 하는 상황에서, Precision-Recall Curve가 모델의 성능을 평가하는 데 중요한 역할을 합니다.
결론적으로:

Precision-Recall Curve는 이진 분류 모델의 양성 클래스 예측 성능을 평가하기 위해 Precision과 Recall 간의 관계를 시각적으로 표현하는 도구입니다.
특히 불균형 데이터셋에서 유용하며, ROC Curve보다 양성 클래스에 대한 성능 평가에 더 적합할 수 있습니다.
이 곡선을 통해 특정 임계값에서의 모델 성능을 분석하고, Precision과 Recall 간의 트레이드오프를 평가하여 최적의 성능을 발휘하는 모델을 선택할 수 있습니다.
F1 스코어는 프리시전 리콜 조화평균임

## AI 답변

Precision Recall Curve(정밀도-재현율 곡선)은 이진 분류 문제에서 분류 모델의 성능을 평가하는 데 사용되는 그래프입니다. 이 곡선은 서로 다른 임계값(threshold)에 대한 정밀도(precision)와 재현율(recall)의 관계를 보여줍니다.

정밀도(precision)는 양성으로 예측한 샘플 중에서 실제 양성 비율을 나타내며, 재현율(recall)은 실제 양성 샘플 중에서 양성으로 올바르게 예측한 비율을 의미합니다.

Precision Recall Curve를 그리기 위해서는 다음 단계를 따릅니다:

1. 분류 모델의 예측 확률(prediction probability)을 내림차순으로 정렬합니다.
2. 서로 다른 임계값에 대해 정밀도와 재현율을 계산합니다.
3. 각 임계값에 대한 정밀도와 재현율 값을 (재현율, 정밀도) 좌표 평면에 점으로 표시합니다.
4. 이 점들을 연결하여 Precision Recall Curve를 생성합니다.

이 곡선은 분류 모델의 성능을 종합적으로 평가할 수 있게 해줍니다. 곡선이 좌상단에 가까울수록 모델의 성능이 좋다고 할 수 있습니다. 또한 곡선 아래 면적(Area Under the Precision Recall Curve, AUPRC)을 계산하여 모델 성능을 요약할 수 있습니다.

Precision Recall Curve는 불균형 데이터셋(imbalanced dataset)에서 특히 유용하게 사용됩니다. 이는 정밀도와 재현율이 불균형 데이터에 대해 더 의미 있는 평가 지표이기 때문입니다.

