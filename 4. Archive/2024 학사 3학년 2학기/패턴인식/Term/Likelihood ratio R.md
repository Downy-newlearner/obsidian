---
created: 2024-11-04 00:57
tags: 
aliases:
  - Likelihood ratio
---
**Likelihood Ratio $R$**:  
두 클래스 간의 상대적 가능성을 평가하여 샘플이 어느 클래스에 속할 가능성이 더 큰지 결정하는 데 사용한다.

**핵심 디테일**:  
- $R$은 특정 샘플 $x$가 두 클래스 중 한 클래스 $C_i$에 속할 가능성을 다른 클래스 $C_j$에 대한 가능성과 비교한다.
- $R = \frac{P(C_i|x)}{P(C_j|x)} = \frac{P(C_i)p(x|C_i)}{P(C_j)p(x|C_j)}$와 같은 형식으로 계산하며, $R > 1$이면 샘플이 클래스 $A$에 속할 가능성이 더 높다고 판단하여 클래스 $A$를 선택한다. 반면 $R \leq 1$이면 클래스 $B$를 선택한다.

**요약**:  
Likelihood Ratio $R$은 ==샘플이 두 클래스 중 어느 쪽에 속할 가능성이 더 큰지 평가하여 최적의 클래스를 선택하는 기준으로 사용된다.==