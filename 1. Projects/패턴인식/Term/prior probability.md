---
created: 2024-11-29
tags: 
aliases:
  - 사전 확률
reference:
---
베이즈 통계학에서 사용되는 개념이다.
주어진 데이터나 증거를 고려하기 전에 어떤 사건이 발생할 확률을 나타낸다.
즉, 사건에 대한 기존의 지식이나 믿음을 바탕으로 설정된 확률이다.

### 1. 사건에 대한 사전 정보
예를 들어, 질병에 걸린 사람들의 확률을 알고 싶을 때, 이 질병의 발생률(예: 1%의 사람만 이 질병에 걸린다)이 prior probability이다. 이 확률은 데이터나 새로운 정보 없이도 알고 있는 정보에 기반한 확률이다.

### 2.  베이즈 정리에서의 역할
베이즈 정리는 주어진 사전 확률(prior probability)로 후행 확률(posterior probability)를 계산한다.

$P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)}$

여기서:

- $P(θ)$는 prior probability이다.
- $P(D | θ)$는 주어진 파라미터 θ에서 데이터 D가 발생할 확률이다.
- $P(θ | D)$는 posterior probability로, 데이터 D를 고려한 후의 확률이다.
- $P(D)$는 데이터 D가 발생할 전체 확률이다.

### 요약:

- **사전에 알고 있는 정보**:
    - $P(\theta)$ (Prior Probability): 모델 파라미터 θ\thetaθ에 대한 사전 정보
    - P(D∣θ)$P(D | \theta)$ (Likelihood): 주어진 θ\thetaθ에서 데이터 DDD가 발생할 확률 (사전 지식)
- **베이즈 정리 후에 알게 될 정보**:
    - $P(\theta | D)$ (Posterior Probability): 새로운 데이터 DDD를 반영하여 갱신된 모델 파라미터 θ\thetaθ에 대한 확률
    - $P(D)$ (Evidence): 데이터 DDD가 발생할 전체 확률 (베이즈 정리의 계산에서 필요한 값)

### 3. 예시
- 질병 A에 대한 prior probability가 5%라고 한다면, 이는 질병 A에 걸릴 확률이 5%라는 의미입니다.
- 만약 어떤 사람이 질병 A의 증상을 보였다고 할 때, 이 증상이 나타났을 때 그 사람이 실제로 질병 A에 걸릴 확률을 posterior probability로 계산하게 됩니다. 그 계산에는 prior probability와 새로운 증거가 반영됩니다.

