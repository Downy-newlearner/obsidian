# 🧐 Conjugate Prior란?

## 정답 링크

https://velog.io/@jhlim2993/Conjugate-Prior

## 형식적 답

**Conjugate Prior(켤레 사전 분포)**는 베이지안 추론에서 사후 분포가 사전 분포와 같은 분포족에서 유지되도록 하는 사전 분포입니다.
장점은 계산의 용이성과 해석의 단순화입니다.
단점은 유연성의 부족으로, 모든 상황에 적합하지 않을 수 있다는 점입니다.

## AI 답변

Conjugate Prior는 베이즈 통계에서 널리 사용되는 개념입니다. 베이즈 통계에서는 모수(parameter)에 대한 사전 분포(prior distribution)와 데이터로부터 얻은 가능도 함수(likelihood function)를 결합하여 모수에 대한 사후 분포(posterior distribution)를 도출합니다.

Conjugate Prior는 사전 분포와 가능도 함수의 결합 분포(posterior distribution)가 동일한 분포족에 속하는 경우를 말합니다. 예를 들어, 베르누이 분포의 모수 θ에 대한 사전 분포가 베타 분포이면, 사후 분포 또한 베타 분포가 됩니다. 이러한 경우 베타 분포를 베르누이 분포의 θ에 대한 Conjugate Prior라고 합니다.

Conjugate Prior를 사용하면 베이즈 추론을 수학적으로 간단하게 처리할 수 있으며, 사후 분포의 계산과 해석이 용이해집니다. 그러나 모든 분포에 대해 Conjugate Prior가 존재하는 것은 아니므로, 분포의 종류에 따라 적절한 Conjugate Prior를 선택해야 합니다.

