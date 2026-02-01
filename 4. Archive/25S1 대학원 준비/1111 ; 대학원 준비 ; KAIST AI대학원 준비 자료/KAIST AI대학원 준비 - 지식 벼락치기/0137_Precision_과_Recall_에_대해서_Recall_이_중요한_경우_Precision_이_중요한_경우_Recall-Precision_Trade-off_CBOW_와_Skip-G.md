# Precision 과 Recall 에 대해서
Recall 이 중요한 경우
Precision 이 중요한 경우
Recall-Precision Trade-off
CBOW 와 Skip-Gram
Skip-Gram
Negative Sampling
OOV 문제
AdamW

## 정답 링크

https://www.youtube.com/watch?v=Qk_yP976WBg&list=PL_iJu012NOxdt7VSZK0sE2YvltT7NOlHH&index=12

## AI 답변

1. Recall이 중요한 경우:
Recall은 관련 항목을 얼마나 잘 포착하는지를 나타냅니다. 따라서 Recall이 중요한 경우는 모든 관련 항목을 찾아내는 것이 중요한 상황입니다. 예를 들어, 질병 진단에서는 가능한 모든 증상을 놓치지 않고 포착하는 것이 매우 중요합니다. 또한, 보안 시스템에서 위협 요소를 놓치지 않는 것이 중요합니다.

2. Precision이 중요한 경우:
Precision은 반환된 결과가 얼마나 관련성이 높은지를 나타냅니다. 따라서 Precision이 중요한 경우는 정확한 결과만을 얻는 것이 중요한 상황입니다. 예를 들어, 웹 검색 엔진에서는 관련성이 높은 결과만을 제공하는 것이 중요합니다. 또한, 스팸 필터링에서는 정확히 스팸 메일만을 걸러내는 것이 중요합니다.

3. Recall-Precision Trade-off:
일반적으로 Recall을 높이면 Precision은 낮아지고, Precision을 높이면 Recall은 낮아지는 Trade-off 관계가 있습니다. 이는 관련 항목을 많이 포착하려면 비관련 항목도 함께 포착할 가능성이 높아지기 때문입니다. 따라서 상황에 따라 적절한 균형을 잡는 것이 중요합니다.

4. CBOW (Continuous Bag-of-Words) 와 Skip-Gram:
CBOW와 Skip-Gram은 Word2Vec 모델의 두 가지 아키텍처입니다. CBOW는 주변 단어들을 입력으로 받아 중심 단어를 예측하는 모델이며, Skip-Gram은 중심 단어를 입력으로 받아 주변 단어들을 예측하는 모델입니다. 일반적으로 Skip-Gram이 CBOW보다 성능이 좋은 것으로 알려져 있습니다.

5. Skip-Gram:
Skip-Gram 모델은 중심 단어를 입력으로 받아 주변 단어들을 예측합니다. 이를 통해 단어 벡터를 학습하며, 유사한 단어들은 벡터 공간 상에서 가까이 위치하게 됩니다. Skip-Gram은 CBOW보다 성능이 좋은 것으로 알려져 있습니다.

6. Negative Sampling:
Negative Sampling은 Word2Vec 모델에서 사용되는 기술로, 계산 효율성을 높이기 위해 고안되었습니다. 모든 단어 쌍에 대해 학습하는 대신, 실제 단어 쌍과 일부 임의의 부정적인 단어 쌍(negative sample)을 사용하여 학습합니다. 이를 통해 계산 비용을 줄일 수 있습니다.

7. OOV (Out-of-Vocabulary) 문제:
OOV 문제는 사전에 정의된 어휘에 없는 단어가 입력되었을 때 발생하는 문제입니다. 이를 해결하기 위한 방법으로는 문자 단위 모델 사용, 미리 정의된 UNK(Unknown) 토큰 사용 등이 있습니다.

8. AdamW:
AdamW는 Adam 최적화 알고리즘의 변형으로, 가중치 감소(weight decay) 정규화를 적용한 버전입니다. Adam 알고리즘은 학습률 조절을 통해 수렴 속도를 높이지만, 가중치 감소 정규화가 적용되지 않아 일반화 성능이 떨어질 수 있습니다. AdamW는 이를 해결하기 위해 가중치 감소 정규화를 추가하여 일반화 성능을 향상시킵니다.

