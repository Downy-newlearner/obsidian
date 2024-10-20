---
생성일: Invalid date
태그: Image Generation Model
Authors: Jonathan Ho
상태: 진행 중
---
![[Source/Denoising_Diffusion_Probabilistic_Models 2.pdf|Denoising_Diffusion_Probabilistic_Models 2.pdf]]
[[HUB/HUB/공부/공부/Diffusion Model|Diffusion Model]]
#### Image Generation Model Terms
|이름|설명|다시 봐야하는 용어|
|---|---|---|
|[[Latent Variable Models]]|잠재 변수 모델은 관찰되지 않은 숨겨진 변수를 사용하는 통계 모델입니다. 이를 통해 복잡한 데이터의 분포를 간단하게 표현할 수 있습니다.|[x]|
|[[Denoising Score Matching]]|노이즈가 포함된 데이터와 원본 데이터를 기반으로 하는 모델의 노이즈 제거 훈련 기술이다.|[ ]|
|[[Langevin Dynamics]]|물리학에서 유래한 기법으로, 랜덤한 움직임을 통해 시스템의 화학적 및 물리적 거동을 모델링하는 데 사용된다. 여기서는 이미지 생성 시 샘플링 방법으로 이용된다.|[ ]|
|[[확산(Diffusion)]]|데이터에 점진적으로 노이즈를 추가하는 과정|[ ]|
|[[역확산(Denoising)]]|점진적으로 노이즈를 제거하여 원본 데이터로 복원하는 과정|[ ]|
|[[Latent Variable(잠재변수)]]|이 변수들은 데이터 뒤에 숨겨진 구조나 패턴을 설명하기 위해 사용된다. 예를 들어, 사람의 성격, 감정 상태, 또는 특정한 규칙 등을 잠재 변수로 모델링할 수 있다. 하지만 이들은 직접 관찰할 수 없으며, 데이터와 동일한 존재가 아니다. 데이터를 설명할 뿐.|[ ]|
|[[정규분포(가우시안 분포)]]||[ ]|
  
  
# Abstract
We present high quality image synthesis results using diffusion probabilistic models,  
a class of latent variable models inspired by considerations from nonequilibrium  
thermodynamics. Our best results are obtained by training on a weighted variational  
bound designed according to a novel connection between diffusion probabilistic  
models and denoising score matching with Langevin dynamics, and our models naturally admit a progressive lossy decompression scheme that can be interpreted as a  
generalization of autoregressive decoding. On the unconditional CIFAR10 dataset,  
we obtain an Inception score of 9.46 and a state-of-the-art FID score of 3.17. On  
256x256 LSUN, we obtain sample quality similar to ProgressiveGAN.  
  
우리는 비평형 열역학의 고려사항에서 영감을 받은 잠재 변수 모델의 일종인 확산 확률 모델을 사용하여 고품질 이미지 합성 결과를 제시합니다.
  
우리의 최상의 결과는 ==확산 확률 모델(==diffusion probabilistic models)과 ==Langevin 동역학을 사용한 노이즈 제거 점수 매칭== 사이의 새로운 연결고리에 따라 설계된 ==가중치 변분 경계==를 이용하여 훈련함으로써 얻어졌습니다.
  
우리의 모델은 자연스럽게 ==자기 회귀 디코딩==의 일반화로 해석될 수 있는 점진적인 손실 압축 방식을 허용합니다.
  
무조건적인 CIFAR10 데이터셋에서는 9.46의 Inception 점수와 3.17의 최첨단 FID 점수를 얻었습니다. 256x256 LSUN에서 우리는 ProgressiveGAN과 유사한 샘플 품질을 얻었습니다.
  
  
## Mile1: diffusion probabilistic models(확산 확률 모델)
확산 확률 모델(diffusion probabilistic models)은 이미지 생성 및 변환 작업에 사용되는 통계적 모델의 한 종류이다.
  
샘플링은 주어진 확률 분포 또는 모델로부터 무작위적인 데이터 포인트를 생성하는 행위를 뜻하며, Langevin 동역학에서는 이러한 샘플링 과정을 통해 데이터를 생성하는 데 활용됩니다.
## Mile2: Langevin Dynamics(랑주뱅 동역학)
score function을 기반으로 하는 SDE를 활용하는 diffusion model에서 샘플링을 하는 방법으로 널리 사용된다.
  
**랑주뱅 동역학이 어떻게 유도되는가?**