# 🧐 Beta Distribution과 Dirichlet Distribution이란 무엇인가?

## 정답 링크

https://angeloyeo.github.io/2021/04/23/binomial_distribution.html

## 형식적 답

3. Beta Distribution과 Dirichlet Distribution의 관계
Beta Distribution은 Dirichlet Distribution의 특수한 경우입니다. Beta Distribution은 두 가지 범주(성공/실패)를 다루는 반면, Dirichlet Distribution은 다수의 범주(다양한 클래스 또는 카테고리)를 다룹니다.
Beta Distribution은 2차원 단순체에서의 확률 분포를 나타내고, Dirichlet Distribution은 
𝑘
k-차원 단순체에서의 확률 분포를 나타냅니다.
결론적으로:

**Beta Distribution(베타 분포)**은 이항 확률이나 비율과 같은 0과 1 사이의 값을 모델링하는 데 사용됩니다.
**Dirichlet Distribution(디리클레 분포)**은 다수의 범주에 속하는 확률 변수들을 모델링하는 데 사용되며, Beta Distribution의 다변량 확장입니다.

## AI 답변

베타 분포(Beta Distribution)와 디리클레 분포(Dirichlet Distribution)는 확률론과 베이지안 통계에서 중요한 역할을 하는 연속 확률 분포입니다.

1. 베타 분포(Beta Distribution):
베타 분포는 0과 1 사이의 값을 갖는 연속 확률 분포입니다. 이는 이진 사건의 성공 확률을 모델링하는 데 사용됩니다. 베타 분포는 두 개의 양의 모수 α와 β에 의해 결정됩니다. 이 분포의 확률 밀도 함수는 다음과 같습니다:

f(x; α, β) = Γ(α + β) / (Γ(α)Γ(β)) * x^(α-1) * (1-x)^(β-1)

여기서 Γ는 감마 함수입니다. 베타 분포는 베이지안 통계에서 사전 분포 및 사후 분포로 자주 사용됩니다.

2. 디리클레 분포(Dirichlet Distribution):
디리클레 분포는 베타 분포의 다변량 일반화입니다. 이는 K개의 양의 실수의 합이 1이 되도록 하는 확률 벡터를 모델링하는 데 사용됩니다. 디리클레 분포는 K개의 양의 모수 α1, α2, ..., αK에 의해 결정됩니다. 이 분포의 확률 밀도 함수는 다음과 같습니다:

f(x1, x2, ..., xK; α1, α2, ..., αK) = Γ(Σαi) / (Π Γ(αi)) * Π xi^(αi-1)

여기서 x1, x2, ..., xK는 0과 1 사이의 값을 갖고, 그 합은 1이 됩니다. 디리클레 분포는 다범주 데이터의 확률 분포를 모델링하는 데 사용됩니다. 또한, 베이지안 통계에서 다범주 사전 분포 및 사후 분포로 활용됩니다.

베타 분포와 디리클레 분포는 모두 다양한 분야에서 널리 사용되며, 특히 베이지안 통계, 기계 학습, 자연어 처리 등에서 중요한 역할을 합니다.

