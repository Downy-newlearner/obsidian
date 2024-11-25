### [[1. GAN의 한계]]

**기존 소주제**

- 1.1 Mode Collapse 문제와 원인
	- 

- 1.2 훈련 안정성 부족 (Unstable Training)
- 1.3 평가 지표의 한계 (Inception Score와 FID의 문제점)

**추가 가능 소주제**

- 1.4 GAN 훈련에서 발생하는 Discriminator와 Generator의 경쟁적 구조 문제
- 1.5 고해상도 이미지 생성에서 발생하는 제약
- 1.6 데이터 부족 상황에서의 성능 저하

---

### 2. Diffusion(DDPM)의 Intention

**기존 소주제**

- 3.1 확률적 프로세스를 통한 데이터 생성 접근
- 3.2 GAN의 한계를 극복하기 위한 새로운 프레임워크
- 3.3 노이즈를 점진적으로 제거하는 역과정의 아이디어

**추가 가능 소주제**

- 3.4 Gaussian Noise의 선택적 사용 이유
- 3.5 Diffusion 모델이 기존 모델보다 직관적인 이유
- 3.6 Variational Inference 관점에서의 Diffusion

---

### 3. DDPM 동작 원리

**기존 소주제**

- 4.1 Forward Process: 데이터에 노이즈 추가
- 4.2 Reverse Process: 노이즈 제거를 통한 데이터 복원
- 4.3 손실 함수와 학습 과정

**추가 가능 소주제**

- 4.4 Sampling Efficiency 개선을 위한 방법들
- 4.5 Reverse Process의 안정성을 보장하기 위한 조건
- 4.6 DDPM의 학습 시간 대비 생성 품질

---

### 4. 예제 코드

**기존 소주제**

- 5.1 Forward 및 Reverse Diffusion 구현
- 5.2 PyTorch 기반의 DDPM 간단 코드
- 5.3 모델 학습 및 이미지 생성 과정

**추가 가능 소주제**

- 5.4 주요 하이퍼파라미터 설정과 조정법
- 5.5 Sampling 속도 최적화를 위한 기법
- 5.6 Pretrained 모델 활용 및 Fine-tuning

---

### 5. 사용 예시

**기존 소주제**

- 6.1 Web Diffusion: 이미지 생성 웹 애플리케이션
- 6.2 Stable Diffusion: 대규모 텍스트-이미지 생성
- 6.3 HuggingFace Diffusers 라이브러리 활용

**추가 가능 소주제**

- 6.4 이미지에서 텍스트로의 Diffusion 응용 사례
- 6.5 비디오 생성에서의 Diffusion 활용