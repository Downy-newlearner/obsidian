---
태그:
  - CV
  - Image Generation
---
#### 딥러닝&파이썬 용어 정리
| 책 이름 | 챕터/날짜           | 이름                                    | 설명                                                                                                                                                       |
| ---- | --------------- | ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 독학   | Diffusion Model | [[결합 분포(joint distribution)]]         | 두 개 이상의 확률 변수의 분포를 나타내는 개념으로, 여러 확률 변수가 동시에 어떤 값을 가질 확률을 설명한다.                                                                                           |
| 독학   | Diffusion Model | [[이미지가 가우시안 분포를 따른다는 것은]]             | 각 픽셀은 R, G, B 값으로 각각 0~255 사이의 값을 갖는다. 이 때 R, G, B 각각을 서로 독립적으로 보아 모든 픽셀의 R 값이 가우시안 분포를 따르고, G값, B값도 가우시안 분포를 따른다는 것이다.                                  |
| 독학   | Diffusion Model | [[variational inference(변분 추론)]]      | 이후 타임스텝으로 근사하기 위해 사용하는 베이지 추론 기법 중 하나로, 효율적이고 실용적이라는 특징이 있다. 후방 분포를 직접 계산하는 것이 아니라 그저 후방분포를 근사하는 간단한 분포를 설정한다는 아이디어를 통해 효율성과 실용성을 챙기는 것이다.               |
| 독학   | Diffusion Model | [[parameterized Markov chain]]        | 마르코프 체인의 전이 확률이 특정한 매개변수들에 의해 조정되고 결정된다는 것을 의미한다. 그리고 이 매개변수들은 모델의 훈련 과정에서 최적화된다.                                                                        |
| 독학   | Diffusion Model | [[Conditional]]                       | “Conditional”이라는 용어가 붙은 이미지 생성형 모델 아키텍처는 특정 조건이나 입력에 따라 생성할 결과물이 결정된다는 의미이다.                                                                             |
| 독학   | Diffusion Model | [[Objective function, Cost function]] | 목적 함수, 최적화 문제에서 변수가 최소화 또는 최대화해야 하는 함수이다. 일례로 경사 하강법의 대상이 목적 함수인 것이다.                                                                                    |
| 독학   | Diffusion Model | [[브이랩]]                               | Virtual Lab 가상환경에서 실험을 수행할 수 있도록 도와주는 시스템                                                                                                                |
| 독학   | Diffusion Model | [[robust learning]]                   | 다양한 환경이나 조건에서도 강력한 성능을 유지할 수 있도록 모델을 학습하는 방법. 데이터의 노이즈, 잡음, 이상치에 대한 강인성을 강조하며 이런 불확실성에서도 안정적이고 신뢰성 있는 예측 모델을 만드는 것이 목표인 학습 방법이다.                         |
| 독학   | Diffusion Model | [[Noise Scheduler]]                   | Diffusion Process에서 노이즈가 추가되는 정도를 조절한다. 예시로 linuer noise scheduler는 시간이 지날 수록 더 많은 노이즈가 추가되도록 한다.                                                        |
| 독학   | Diffusion Model | [[Markov chain]]                      | 각 전이의 단계는 현재 상태에만 의존한다는 메모리리스 속성을 가진다. 즉 현재 데이터 포인트(상태)에서 노이즈를 추가하여 다음 데이터 포인트(다음 상태)가 생성된다. 이 과정은 여러 단계에 걸쳐 진행되며, 각 단계가 가우시안 전이로 이루어지게 된다.              |
| 독학   | Diffusion Model | [[Gaussian transition]]               | Diffusion model에서 데이터의 변환 과정이 가우시안(정규) 분포를 따르는 것과 관련이 있습니다. 확산 모델은 노이즈를 점진적으로 추가하거나 제거하여 데이터를 생성합니다. 이 과정에서 각 단계는 가우시안 분포를 통해 정의된 전이 과정을 따릅니다.           |
| 독학   | Diffusion Model | [[Diffusion Model]]                   | 주로 데이터를 생성하거나 모사하는 데 사용되는 수학적 또는 컴퓨터 과학적 모델을 의미한다. 이 모델은 확산의 원리를 기반으로 하여, 데이터를 점진적으로 "노이즈"와 함께 변화시키고, 그 과정을 역으로 수행하여 원래 데이터를 복원하거나 새로운 데이터를 생성하는 데 사용된다. |
| 독학   | Diffusion Model | [[deep generative model]]             |                                                                                                                                                          |
  
  
  
## Q1
![[Source/image 14.png|image 14.png]]
  
1. **Diffusion Model의 Reverse Process 수식 설명**:
    - 첫 번째 식 $( p_\theta(x_{0:T}) := p(x_T) \prod_{t=1}^{T} p_\theta(x_{t-1} | x_t) )$﻿은 최종적인 데이터 $( x_0 )$﻿까지의 확률을 표현합니다. 이때 $( p(x_T) )$﻿는 초기 상태 $( x_T )$﻿와 관련된 확률이며, 두 번째 부분은 각 단계에서 다음 상태에서 이전 상태로의 전이 확률을 곱하는 형태로 모델을 만들고 있습니다.
    - 두 번째 식 $p_\theta(x_{t-1} | x_t) := \mathcal{N}(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$﻿ 은 특정 상태 $x_t$﻿ 에서 이전 상태 $x_{t-1}$﻿ 로의 전이를 가우시안 분포로 모델링합니다. 여기서 $\mu_\theta(x_t, t)$﻿와 $\Sigma_\theta(x_t, t)$﻿는 각각 평균과 분산을 나타내며, 이는 $x_t$﻿와 시간 $t $﻿에 의존합니다.
2. **:= 기호의 의미**:
    - := 기호는 "정의된다"는 의미로 사용됩니다. 즉, 왼쪽의 식이 오른쪽의 식으로 정의된다는 것을 나타냅니다. 예를 들어, $p_\theta(x_{0:T}) := p(x_T) \prod_{t=1}^{T} p_\theta(x_{t-1} | x_t)$﻿ 는 $p_\theta(x_{0:T})$﻿ 가 어떻게 정의되는지를 보여줍니다.
3. N(a; b)**에서 ';'의 역할**:
    - $N(a; b)$﻿ 는 정규분포를 나타내는 기호에서 a 는 위치(평균), b 는 분산으로 해석될 수 있습니다. ';'는 일반적으로 "주어진 조건"을 분리하는 역할을 합니다. 여기서 $N(x_{t-1}; \mu_\theta(x_t, t), \Sigma_\theta(x_t, t))$﻿는 변수 $x_{t-1}$﻿가 평균 $\mu_\theta(x_t, t)$﻿와 분산$ \Sigma_\theta(x_t, t)$﻿를 갖는 정규분포를 따른다는 의미입니다.
  
  
## 디퓨전 모델 - 강의1
랜덤 노이즈에서 시작해서 한 단계씩 샘플링 과정을 통해 제너럴한 이미지를 발생시킨다.
  
Diffusion Process, Denoising Process 이렇게 두 과정으로 이루어진다.
  
노이즈가 추가될 때 딥러닝으로 어느 부분에 추가됐는지 학습한다.
학습이 완료된 모델을 통해 완전 노이즈로부터 이미지를 생성할 수 있게 된다.
  
노이즈 스케줄러에 따라 노이즈 추가 정도를 조절해야하므로 시간 정보가 Neural network 안으로 들어가야한다.
시간 정보는 인코딩하여 뉴럴 네트워크 안으로 들인다.(인코딩에는 sin, cos 함수를 사용한다.)
  
![[Source/image 1 6.png|image 1 6.png]]
단계별로 노이즈가 추가되고, 제거되는 것으로 보이지만 간단한 수학을 이용하여 노이즈 추가/제거를 예측해 여러 단계를 건너뛸 수 있다.
하지만 노이즈를 제거하는 과정에서 예측을 통해 여러 단계를 건너뛰어버리면 완성 이미지가 모호할 수 밖에 없다.
그러므로 모호한 완성 이미지로부터 뉴럴 네트워크를 통해 몇 단계 이전 이미지(노이즈가 포함된 이미지)를 계산 및 생성하고 다시 이로부터 덜 모호한 완성 이미지를 만든다. 이 왔다갔다하는 과정을 여러번 반복해서 제너럴한 이미지를 생성할 수 있다. →
  
## 디퓨전 모델 - 강의2

> [!info] Diffusion Model 수학이 포함된 tutorial  
> DDPM, DDIM, ADM-G, NCSN, Score-based models, 그리고 여러 모델들의 흐름과 수학을 총정리 했습니다.  
> [https://www.youtube.com/watch?v=uFoGaIVHfoE&t=136s](https://www.youtube.com/watch?v=uFoGaIVHfoE&t=136s)  
  
### Physical intuition
![[Source/image 2 7.png|image 2 7.png]]
연기가 확산되는 상황에서 처음 연기의 모습은 알기 어렵지만 시간이 많이 지났을 때의 연기의 모습은 고르게 분포되어 uniform 한 상태일 것임을 알 수 있다.
그렇다면 딥러닝을 이용하여 Uniform한 상태에서 다시 처음 상태로 되돌릴 수 있다면? << 이것이 디퓨전 모델의 physical intuition이다.
  
분자가 활성될 때 , 작은 sequence 안에서는 forward와 reverse 모두 가우시안일 수 있다.(물리적으로 그렇다.)
  
디퓨전 모델은 이미지에서 노이즈를 점차 추가하여 최종적으로 가우시안 노이즈에 가까운 노이즈맵을 만들고
이 노이즈 맵에서 reverse denoising 과정을 통해 이미지를 생성하는 것이다.
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0004.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0005.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0006.jpg]]
향수를 뿌렸을 때 처음에는 분자가 한 곳에 밀집해 있지만, 시간이 지나면서 분자가 공간에 퍼지게 되면 전체 시스템의 엔트로피가 증가하게 된다.
향수 분자가 공기 중으로 확산되는 과정에서 분자들이 더 높은 농도에서 낮은 농도로 이동하면서 공간에 고르게 분포하려고 하며, 확산의 원리에 따른 것이다.
충분한 시간이 지나면 향수 분자가 공간에 균일하게 분포하게 되며, 이는 시스템이 열역학적 평형 상태에 도달했음을 의미한다. 이러한 평형 상태에서 분자의 이동은 계속 이루어지지만, 전체적으로는 농도가 일정하게 유지된다.
  
향수 분자가 확산되는 과정을 아주 짧은 단위의 time sequence로 불연속적이게 잘라서 본다면 각 분자의 다음 위치(forward)는 가우시안 분포를 따를 수 있다.
왜냐하면 각 분자의 다음 위치는 무작위로 결정되며, 이 무작위성은 일반적으로 가우시안 분포(정규 분포)를 따른다.
이에 따라 이전 위치(reverse)도 가우시안 분포를 따를 수 있다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0007.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0008.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0009.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0010.jpg]]
Forward process에서 각 스텝은 가우시안 커널을 통과하여 다음 스텝으로 이동한다. 그저 함수(커널)를 통과시키면 되는 과정이라 쉬운 과정이다.
$K(x) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{x^2}{2\sigma^2}\right)$﻿
가우시안 커널을 통과하는건 각 픽셀 하나하나이다.
예를 들어 255*255 사이즈의 이미지에 가우시안 분포를 따르는 노이즈를 추가한다면, 65025개의 각 픽셀의 픽셀값에 가우시안 분포를 따르는 노이즈 값(무작위)을 추가한다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0011.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0012.jpg]]
이 식은 확률 분포를 나타내는 것으로, 특히 가우시안(정규) 분포에 관련이 있습니다. 여기서 \(N\)은 정규 분포를 의미하며, 그 인자는 아래와 같습니다:
- $x_t$﻿: 변량 또는 랜덤 변수
- $\sqrt{1 - \beta_t} x_{t-1}$﻿: 정규 분포의 평균값 (mean)
- $\beta_t$﻿: 정규 분포의 분산 (variance)와 관련된 파라미터
- $I$﻿: 단위 행렬 (identity matrix)
이 식은 특정 시점 \(t\)의 상태 \(x_t\)가 이전 상태 \(x_{t-1}\)에 기반하여 정의된 정규 분포를 따른다는 것을 나타냅니다. 일반적으로 이러한 표현은 시계열 모델이나 상태 공간 모델에서 사용됩니다.
  
$\beta_t$﻿는 0에 가까운 0.0001같은 값이다. 그러므로 $\sqrt{1 - \beta_t}$﻿는 1에 가까운 값이다.
이는 이전 값을 아주 조금 감소시킨다는 의미를 갖는다.
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0013.jpg]]
$\beta_t$﻿는 매우 작은 값이다.
이전 스텝에서 다음 스텝으로 갈 때 노이즈를 조금 조금씩 입힌다.
joint distribution으로 1:T를 나타낸다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0014.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0015.jpg]]
조금씩 노이즈를 더할 것인데, 혹시 한 번에 여러 스텝을 갈 수 있지 않을까? << 이것이 DDPM의 핵심
가우시안 커널들이 연속적으로 이루어지기때문에 타임스텝 t를 한 번에 정의할 수 있다.  
  
$x_t$﻿를 $x_0$﻿에서 바로 정의할 수 있는 식을 준비했다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0016.jpg]]
$x_0$﻿에서 노이즈를 계속 가해서 가우시안 노이즈에 가까운 $x_T$﻿를 만든다.
가지고있는 이미지($x_0$﻿)을 가지고 $x_t$﻿를 구할 수 있다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0017.jpg]]
목표로 하는 것은 Denoising, 즉 reverse step이다.
reverse step 하나하나도 역시나 매우 작은 변화만을 가져오며, 에서 언급했듯이, reverse step 역시 가우시안 분포를 띈다는 근거하에, 각 reverse step을 가우시안으로 가정한다.
  
이때 x_T의 평균이 0이라는 것은 [0,255]의 픽셀값을 [-1,1]로 정규화했을 때의 이야기이다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0018.jpg]]
중요한 것은. reverse process도 가우시안으로 모델링할 수 있고, 이 때의 평균과 분산이 가장 궁금한 것이 된다.
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0019.jpg]]
리버스 프로세스를 정의했고, 알아야하는 것은 가우시안의 평균과 분산이다. 까지 온 것이다.
이제는 어떻게 학습을 할 것인가? variational upper bound를 이용한다.
마치 VAE에서 식을 전개하느 것 처럼 $p_\theta(x_0)$﻿에 대한 negative log likelihood를 수식적으로 정의를 하고 이의 엘보를 구해서 Loss term을 만든다.
  
최종적으로 두 번째 줄 수식과 같은 Loss term이 나온다는 것을 알 수 있다.
우리는 단순히 세 가지 텀의 KL Divergence 텀과 마지막 텀을 이용하여 Loss를 최소화시킴으로써 평균을 구하는 것을 목표로 하고 있다.
이;것은 regression과 거의 동일한 모습을 보인다.
  
$P(H | D) = \frac{P(D | H) \cdot P(H)}{P(D)}$﻿
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0020.jpg]]
결과적으로 q와 p를 normal distribution으로 가정했기 때문에 둘 사이의 KL을 가우시안 분포 간의 대한 KL로 만들 수 있고, 평균 사이의 차이에 분산을 나누는 형태로 표현이 가능하다.
$x_t$﻿를 $x_0$﻿을 가지고 표현할 수 있다.
최종적으로 알고싶은 것은 reverse process(가우시안 분포)의 평균이다.
그 평균을 구하기위해 수식을 정리하다보니 3번째 수식이 나온 것이고, 여기에서 $\epsilon_\theta(x_t, t)$﻿에 대해서만 알면 더이상 이 수식에서 모르는 것이 없음을 알 수 있다.
[[마지막 수식]]
마지막 수식이 최종 로스를 나타낸다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0021.jpg]]
coefficient인 $\lambda_t$﻿를 1로 설정하는게 좋았다는 논문 결과가 있다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0022.jpg]]
가우시안 모델의 평균을 예측하기 위해서 식을 쓰다보니, 각 스텝 사이의 노이즈를 예측하면 된다는 결론이 나왔고, 그걸 통해서 로스를 학습시켜 노이즈를 predict하는 네트워크를 학습하게 된다.
즉 매 스텝마다 가우시안 노이즈를 하나 샘플링을 하고 그걸 이미지에 타임스텝 t에 맞게 넣어 노이즈를 더하게 되고, 모델은 노이즈가 어떻게 더해졌는지 학습한다
  
샘플링할 때는 mean과 var를 기반으로 수식을 전개해서 학습한 것이기 때문에, 평균을 기반으로 샘플링을 하는 모습이다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0023.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0024.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0025.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0026.jpg]]
t가 변할 때 $\beta_t$﻿는 어떻게 변하는가?
t가 0에 가까워질 수록 새로운 노이즈가 추가되면 안되기 때문에 $\beta_t$﻿는 0에 수렴되게 된다,
각 타임스텝ㅁ바다 해야할 일이 달라지는데 , 노이즈가 얼마나 추가될지에 대한 변수가 베타 t이므로 이는 곧 네트워크에게 얼만큼의 영역에서 어떤 일을 하라고 간접적으로 말하는 것과 같다. 결과적으로는 0.005부터 시작해서 0으로 가까워지도록 보통 $\beta_t$﻿를 스케줄링 해놓는다.
U-Net
타임스텝 t 는 네트워크에게 인풋으로ㅓ 들어온 이미지가 얼만큼의 노이즈가 끼어있는지 알려줄 수 있는 수단이다.
X_t라는 인풋이 들어왔을 때 어떤 노이즈가 씌워진 것인지 네트워크가 predict를 해야하기 때문에, 타임스텝 t가 굉장히 중요한 요소이고 이 t를 숫자로 넣어버리면 안되므로, 인베딩을 해주는데, sin / cos을 가지고 하는 positional encoding이라고 생각하면 된다.
positional encoding을 한 번 해놓고 FC Layer 몇 번 통과해서 U-Net 사이사이에 일일히 concet해주는 형태로 네트워크가 구성되어있다.
t가 해주는 역할을 네트워크에게 인풋으로 들어온 이미지가 몇 번째 타임스테[ㅂ인지 알려주는 것이고, 우리가 결국 원하는 게 각각 타임스텝에 대한 리버스이므로, 보통 타입스텝은 1000번 정도로 설정된다
T는 1000정도로 설정되어있다는 것인데, 각각의 reverse process를 각 모델로 구성하면 너무 많은 모델이 필요하므로 타임스텝 t를 넣어 타임스텝에 해당되는 가우시안 커널을 모델이 predict 할 수 있도록 만든 것이다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0027.jpg]]
### q의 정의(forward process)
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0028.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0029.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0030.jpg]]
각 스텝이 이어져있다는 전제 하에 작성된 수식들
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0031.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0032.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0033.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0034.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0035.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0036.jpg]]
negative log likelihood → 베이즈 룰(joint distribution과 조건부 확률로 표현)
→ VAE에서 엘보를 만들 때 식 전개하는 것과 유사(빨간색 부분이 expectation이 q에 걸려있기 때문에 KL D로 빠져나오면서 0보다 크게 되고, 부등호로 표현할 수 있다.
1. 부등식이 생김
2. 노테이션만 살짝 바꿈, 두 개의 식이 분자와 분모에 그대로 있음을 확인할 수 있다.
3. 그래서 markov chain property 때문에 5번 식으로 넘어갈 수 있음
4. 로그를 이용해 항을 나눈 모습
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0037.jpg]]
1. t = 1인 모습을 따로 빼놓음
2. 파란색 부분이 오른쪽에 작성된 markov chain, 베이즈 룰에 의해 가장 아래 식으로 전개가 된다.
3. 로그에 의해 두 텀으로 나뉨
4. 시그마를 정리해서 간단히 정리됨
5. 식정리를 하여 KLD 텀처럼 나타나고
KLD 텀인 상태로 최종 식을 만들 수 있다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0038.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0039.jpg]]
q가 왜 이렇게 표현될 수 있나?
다음 페이지
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0040.jpg]]
베이즈 룰로 식을 분해하면 각 식은 가우시안 분포로 가정했기 때문에, 식정리 후 평균과 분산을 구한 것이다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0041.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0042.jpg]]
$\mu_\theta$﻿는 타임스텝 t의 리버스 프로세스가 가우스 디퓨전 커널이다 라고 생각했을 때 과연 그 가우시안은 어떻게 모델링할 것인가에서 평균이라고 생각하면 된다. 이때의 var도 learnable하지만 DDPM에서는 학습하지 않는다. 그저 $\beta_t$﻿와 동일하게 사용했다.
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0043.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0044.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0045.jpg]]
weighting은 로스 앞에 붙어있는 값들인데, DDPM에서는 1로 사용했다. 논문마다 다르게 설정하곤 함.
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0046.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0047.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0048.jpg]]
DDIM은 Non-Markovian으로 하려는 시도를 한 것이다.
그런데 Loss가 오리지널 디퓨전 모델과 똑같이 따라간다.
샘플링만 DDIM의 방식을 가져간다는 장점이 있다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0049.jpg]]
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0050.jpg]]
DDIM에서는 전반적인 프로세스를 새로 정의한다
DDPM(Denoising Diffusion Probabilistic Models)과 DDIM(Denoising Diffusion Implicit Models)은 모두 확산 기반 생성 모델이지만, 각자의 특징과 장단점이 있습니다.
### DDPM의 특징
- **샘플링 과정**: DDPM은 순차적으로 노이즈를 추가하는 과정과 그 반대로 노이즈를 제거하는 과정을 거칩니다. 이 과정에서 여러 단계의 샘플링을 필요로 하며, 각 단계에서 데이터의 샘플을 생성합니다.
- **정확성**: 모델의 출력을 높이기 위해 많은 샘플링 단계가 필요합니다. 보통 1000단계 이상의 샘플링이 요구됩니다.
- **수학적 기초**: 각 단계에서의 변화를 명확하게 다루는 확률적 접근 방식을 기반으로 합니다.
### DDIM의 특징
- **샘플링 효율성**: DDIM은 노이즈 제거 과정을 더 효율적으로 사용할 수 있도록 하여, 더 적은 샘플링 단계(보통 25-50단계)로도 같은 품질의 이미지를 생성할 수 있습니다.
- **비가역성**: DDIM은 생성 과정에서의 변동성을 감소시키고, 더 나은 예측을 제공하는 방향으로 정의되므로, 샘플링이 더 빠르고 효과적입니다.
- **모듈성**: DDIM은 기존 DDPM의 결과를 더 잘 활용할 수 있게 설계되어 있어, pretrained 스코어 네트워크와의 호환성도 좋습니다.
### DDPM과 DDIM의 장단점
|   |   |   |
|---|---|---|
|요소|DDPM|DDIM|
|**장점**|- 높은 품질의 이미지 생성|- 적은 샘플링 단계로 높은 품질의 이미지 생성|
||- 이론적으로 강력한 기반|- 더 빠르고 효율적인 샘플링|
||- 다양한 형식의 데이터에 적합|- 기존 DDPM 모델을 쉽게 활용 가능|
|**단점**|- 긴 샘플링 시간 (많은 단계 필요)|- 이론적으로 DDPM보다 덜 엄밀할 수 있음|
||- 모델 훈련과 샘플링이 복잡할 수 있음|- 두 번째 모듈로 인해 오작동 가능성|
### 결론
DDPM과 DDIM은 각각 특성과 장단점이 있어, 특정 용도와 데이터셋에 따라 적절한 선택을 할 수 있습니다. DDIM은 효율성과 속도가 중요한 실용적인 상황에서 더 유리하며, DDPM은 높은 이미지 품질과 이론적 근거가 필요한 상황에서 유리합니다.
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0051.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0052.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0053.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0054.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0055.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0056.jpg]]
Score-based Generative Modeling은 Diffusion model과 같다.
아래에서 두 모델의 관계를 알 수 있다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0057.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0058.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0059.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0060.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0061.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0062.jpg]]
DDPM은 general한 SDE의 특이 케이스이다.(또 다른 케이스로 NCSN 모델이 있다.)
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0063.jpg]]
1982년의 한 논문에서 forward SDE에 대해 reverse SDE를 정의하는 법을 정의했다.
여기서 정의된 reverse SDE의 drift term 안에 Score function이 존재한다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0064.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0065.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0066.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0067.jpg]]
결국 핵심은 $x_0$﻿을 통해서 $x_t$﻿를 정의할 수 있다.
결과적으로는 DDPM에서 학습한 방식과 동일하게 된다.
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0068.jpg]]
DDPM에서 DDIM으로 넘어갈 때 Random을 제거하면서 Deterministic하게 만들 ㅜㅅ 있었는데, 여기서도 마찬가지다 그것을 Probability Flow ODE라고 부른다.
Stocastic한 값을
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0069.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0070.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0071.jpg]]
  
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0072.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0073.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0074.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0075.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0076.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0077.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0078.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0079.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0080.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0081.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0082.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0083.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0084.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0085.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0086.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0087.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0088.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0089.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0090.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0091.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0092.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0093.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0094.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0095.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0096.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0097.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0098.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0099.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0100.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0101.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0102.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0103.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0104.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0105.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0106.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0107.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0108.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0109.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0110.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0111.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0112.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0113.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0114.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0115.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0116.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0117.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0118.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0119.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0120.jpg]]
![[Diffusion%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_page-0121.jpg]]
  
  
  
## 강의3

> [!info] Stable Diffusion 논문 리뷰  
> 최근에 Text to Image 생성 모델이 많은 관심을 받고 있는데요  
> [https://www.youtube.com/watch?v=7fBQDaJkcSU&t=1s](https://www.youtube.com/watch?v=7fBQDaJkcSU&t=1s)  
  
![[Source/image 3 6.png|image 3 6.png]]
  
Pixel 공간이 아닌, Latent space에서 Denoising을 진행하면서 수백개으 ㅣGPU가 필요한 컴퓨팅 코스트를 줄임
Stable Diffusion Models을 Latent Diffusion Models이라고 부른다.(LDMs)
모델 복잡성 감소, 세부적인 표현능력 상승
아키텍처 상에 Cross-Attention을 사용함으로써, 다른 도메인(Text, Audio ..)을 함께 모델상에서 사용 가능
  
원래 디퓨전 모델이 노이즈를 주입할 때 신경망을 사용하지 않고 정해진 함수를 사용한다는 로직이다.
  
  
## 세미나 준비를 위한 수식 이해
DDPM
VAE([https://woongchan789.tistory.com/11](https://woongchan789.tistory.com/11))
정보량이란? - Information Entropy의 내용([[정보 엔트로피(Information Entrophy)]])