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

베이즈 정리는 주어진 사전 확률(prior probability)로 후행 확률(posterior probability)를 계산한다.

$P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)}$

여기서:

- $P(θ)$는 prior probability입니다.
- P(D | θ)는 주어진 파라미터 θ에서 데이터 D가 발생할 확률입니다.
- P(θ | D)는 posterior probability로, 데이터 D를 고려한 후의 확률입니다.
- P(D)는 데이터 D가 발생할 전체 확률입니다.
### 1. **사건에 대한 사전 정보**

- 예를 들어, 질병에 걸린 사람들의 확률을 알고 싶을 때, **이 질병의 발생률**(예: 1%의 사람만 이 질병에 걸린다)이 **prior probability**입니다. 이 확률은 데이터나 새로운 정보 없이도 알고 있는 정보에 기반한 확률입니다.

### 2. **베이즈 정리에서의 역할**

- 베이즈 정리는 주어진 증거(데이터)를 바탕으로 **posterior probability**(후행 확률)를 업데이트하는 방법입니다. 이때, **prior probability**는 데이터가 없을 때의 "초기 확률"로 시작합니다. 이후 새로운 데이터를 반영하여 **posterior probability**를 계산하게 됩니다.
    
- **베이즈 정리의 공식**은 다음과 같습니다:
    
    P(θ∣D)=P(D∣θ)P(θ)P(D)P(\theta | D) = \frac{P(D | \theta) P(\theta)}{P(D)}
    
    여기서:
    
    - P(θ)P(\theta)는 **prior probability**입니다.
    - P(D∣θ)P(D | \theta)는 주어진 파라미터 θ\theta에서 데이터 DD가 발생할 확률입니다.
    - P(θ∣D)P(\theta | D)는 **posterior probability**로, 데이터 DD를 고려한 후의 확률입니다.
    - P(D)P(D)는 데이터 DD가 발생할 전체 확률입니다.

### 3. **예시**

- 질병 A에 대한 prior probability가 5%라고 한다면, 이는 질병 A에 걸릴 확률이 5%라는 의미입니다.
- 만약 어떤 사람이 **질병 A의 증상**을 보였다고 할 때, 이 증상이 나타났을 때 그 사람이 실제로 질병 A에 걸릴 확률을 **posterior probability**로 계산하게 됩니다. 그 계산에는 **prior probability**와 새로운 증거가 반영됩니다.

### 4. **Prior의 중요성**

- **Prior probability**는 때로 매우 중요한 정보를 제공합니다. 특히 데이터가 부족하거나 신뢰할 수 없을 때, 사전 지식이나 과거 경험을 기반으로 하는 prior가 핵심적인 역할을 할 수 있습니다.
- 그러나 prior를 설정할 때 **주관적인 판단**이 개입될 수 있으므로, 신중하게 설정해야 합니다.

### 결론

**Prior probability**는 관찰하기 전, 혹은 증거가 없을 때 **어떤 사건이나 상태에 대해 가지고 있는 믿음**이나 **예상되는 확률**입니다. 이 확률은 새로운 데이터나 증거에 따라 **posterior probability**로 갱신됩니다.