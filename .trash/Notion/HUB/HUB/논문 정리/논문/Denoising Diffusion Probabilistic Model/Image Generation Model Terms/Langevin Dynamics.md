---
설명: 물리학에서 유래한 기법으로, 랜덤한 움직임을 통해 시스템의 화학적 및 물리적 거동을 모델링하는 데 사용된다. 여기서는 이미지 생성 시 샘플링 방법으로 이용된다.
다시 봐야하는 용어: false
---
> [!info] Langevin dynamics 설명 (Langevin equation 설명)  
> Langevin dynamics는 복잡한 시스템에서 입자들의 움직임을 시뮬레이션하기 위한 방법으로, score function을 기반으로 하는 SDE를 활용하는 diffusion model에서 샘플링을 하는 방법으로 널리 사용된다.  
> [https://process-mining.tistory.com/210](https://process-mining.tistory.com/210)  
|   |   |   |   |
|---|---|---|---|
|용어|한국어 직역|뜻|예시/비고|
|Fokker-Planck Equation|포커-플랑크 방정식|확률 밀도 함수의 변화를 시간에 따라 기술하는 미분 방정식.|확률밀도함수가 시간이 흐르면서 stochastic process를 거치는데 이 떄 어떻게 변하는지를 표현하는 미분방정식이다.|
|Probability Density Function|확률 밀도 함수|특정 값이 특정 구간에 속할 확률을 나타내는 함수.||
|Stochastic Process|확률 과정|확률적 성질을 가지며 시간이 지남에 따라 변화하는 과정.||
|Stationary Distribution|정상 분포|시간이 흐른 후에도 변하지 않는 확률 분포.|최종 정상 분포가|
|SDE (Stochastic Differential Equation)|확률 미분 방정식|난수를 포함한 미분 방정식으로, 시스템의 동적 변화를 묘사.||
|Individual Sample Path|개별 샘플 경로|특정 샘플(경로)이 시간이 지남에 따라 어떻게 변화하는지를 나타내는 경로.||
|Probability Distribution|확률 분포|특정 사건의 가능한 결과들이 발생할 확률을 나타내는 함수.||
|Solutions of SDEs|SDE의 해|확률 미분 방정식(SDE)의 해(n, solution); 시스템의 상태 변화를 설명.||
|Stochastic|추측 통계학의|특정 시스템이나 프로세스의 변화를 설명할 때 무작위적인 요소가 포함됨을 의미합니다. 즉, 이러한 프로세스는 예측할 수 없는 랜덤한 변화가 발생하며, 이는 확률 분포와 관련하여 모델링됩니다.||
|확률변수||특정 확률 실험에서 발생 가능한 결과를 수치화하여 나타낸 변수. 즉, 확률실험에서 어떤 값을 취할 수 있는 변수를 의미한다.|주사위를 던질 떄의 확률 변수는 1부터 6까지 6개 존재하는 것이다.|
|확률함수||확률변수가 가질 수 있는 모든 값에 대해 해당 값이 나올 확률을 나타내는 함수를 말한다. 이 함수는 주로 확률질량함수 또는 확률밀도함수로 나타내어진다.||
|확률분포||확률변수가 가질 수 있는 모든 값에 대한 확률을 나타내는 분포를 의미한다. 이 분포는 주로 이산확률변수의 경우 확률질량함수로, 연속확률변수의 경우 확률밀도함수로 나타내어진다.|확률변수가 확률함수를 통해서 그 함숫값(확률)들을 확률 분포로 나타내는 것이다.|
|||||
|||||