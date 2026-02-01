### $\bar{\alpha}_t$에 대한 설명

#### 1. 정의

- $\bar{\alpha}_t$는 **Diffusion Model**에서 노이즈 스케줄링을 나타내는 누적 계수입니다.
- 이 계수는 timestep $t$까지 노이즈가 추가된 정도를 조절하는 데 사용됩니다.

#### 2. 수식

$\bar{\alpha}_t$는 timestep $t$에서의 $\alpha_t$ 값들의 누적 곱(product)으로 정의됩니다:

$\bar{\alpha}_t = \prod_{s=1}^t \alpha_s$

여기서:

- $\alpha_s$는 timestep $s$에서의 노이즈 감소(또는 유지) 비율을 나타내는 개별적인 스케줄 파라미터입니다.
- $\alpha_t$ 값은 보통 $\beta_t$ (노이즈 분산 스케줄)의 보완적 형태로 설정됩니다: $\alpha_t = 1 - \beta_t$

#### 3. 역할

- $\bar{\alpha}_t$는 데이터를 denoising하거나 forward process를 진행할 때, **원본 데이터 $x_0$와 노이즈 $\epsilon$의 상대적 비중**을 조정합니다.
- Forward process에서 $x_t$는 다음과 같이 표현됩니다: 
	$x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1 - \bar{\alpha}_t} \epsilon$
- 여기서:
    - $\sqrt{\bar{\alpha}_t}$는 clean 데이터 $x_0$의 기여도를 조절합니다.
    - $\sqrt{1 - \bar{\alpha}_t}$는 노이즈 $\epsilon$의 기여도를 조절합니다.

#### 4. 노이즈 스케줄의 영향

- $\bar{\alpha}_t$는 $\beta_t$ 값에 따라 달라지며, 일반적으로 $\beta_t$는 선형, 제곱, 또는 다른 형태의 증가 스케줄로 설정됩니다.
- $t$가 커짐에 따라 $\bar{\alpha}_t$는 점점 감소하고, $1 - \bar{\alpha}_t$는 증가합니다. 이는 시간이 지날수록 더 많은 노이즈가 데이터에 추가됨을 의미합니다.

#### 5. 요약

$\bar{\alpha}_t$는 timestep $t$까지의 누적 노이즈 수준을 나타내며, Forward 및 Reverse Process에서 clean 데이터와 노이즈의 균형을 조절하는 핵심 파라미터입니다.