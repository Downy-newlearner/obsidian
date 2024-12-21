
### 1. GAN의 한계

- 1.1 Mode Collapse 문제와 원인
    - GAN이 생성 데이터의 다양성을 보장하지 못하게 만드는 문제
    - $\because$ Generator와 Discriminator의 학습 불균형 및 손실 함수의 한계
    
- 1.2 훈련 안정성 부족 (Unstable Training)
    - GAN의 학습은 Generator와 Discriminator 간의 경쟁적 구조로 인해 매우 불안정하며, 학습이 중단되거나 수렴하지 않는 경우가 흔하다.
    - Non-Convergence 문제: G와 D가 서로 적응하면서 손실 함수가 안정적으로 수렴하지 않고, 학습이 끝없이 반복될 수 있다.
    - D가 지나치게 강하면 G가 유의미한 피드백을 받지 못하고, 반대로 G가 너무 강하면 D가 제대로 학습하지 못한다.
    
- 1.3 평가 지표의 한계 (Inception Score와 FID의 문제점)
    

**요약**: GAN은 Generator와 Discriminator가 균형을 유지하며 훈련되어야 하지만, 이 과정에서 구조적 한계가 존재한다.

---

### 2. Diffusion(DDPM)의 Intention

- 2.1 확률적 프로세스를 통한 데이터 생성 접근
- 2.2 GAN의 한계를 극복하기 위한 새로운 프레임워크
- 2.3 노이즈를 점진적으로 제거하는 역과정의 아이디어

**추가 가능 소주제**

- 2.4 Gaussian Noise의 선택적 사용 이유
- 2.5 Diffusion 모델이 기존 모델보다 직관적인 이유
- 2.6 Variational Inference 관점에서의 Diffusion

---

### 3. DDPM 동작 원리

- 3.1 Forward Process: 데이터에 노이즈 추가
- 3.2 Reverse Process: 노이즈 제거를 통한 데이터 복원
- 3.3 손실 함수와 학습 과정

**추가 가능 소주제**

- 3.4 Sampling Efficiency 개선을 위한 방법들
- 3.5 Reverse Process의 안정성을 보장하기 위한 조건
- 3.6 DDPM의 학습 시간 대비 생성 품질

---

### 4. 예제 코드

- 4.1 Forward 및 Reverse Diffusion 구현
- 4.2 PyTorch 기반의 DDPM 간단 코드
- 4.3 모델 학습 및 이미지 생성 과정

**추가 가능 소주제**

- 4.4 주요 하이퍼파라미터 설정과 조정법
- 4.5 Sampling 속도 최적화를 위한 기법
- 4.6 Pretrained 모델 활용 및 Fine-tuning

---

### 5. 사용 예시

- 5.1 Web Diffusion: 이미지 생성 웹 애플리케이션
- 5.2 Stable Diffusion: 대규모 텍스트-이미지 생성
- 5.3 HuggingFace [[diffusers 라이브러리|Diffusers]] 라이브러리 활용

**추가 가능 소주제**

- 5.4 이미지에서 텍스트로의 Diffusion 응용 사례
- 5.5 비디오 생성에서의 Diffusion 활용
